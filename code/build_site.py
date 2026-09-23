"""Run `myst build --execute` against a Jupyter server started here.

MyST can launch its own server and waits 20 seconds for it to print its token on stderr.
On this book that wait times out on every build, although the same command starts a
server in about 3 seconds on its own: the build reports "Jupyter server did not respond"
and leaves the server running. MyST documents the route used here instead, which starts
the server first and passes its address in JUPYTER_BASE_URL and JUPYTER_TOKEN.

Usage: uv run python code/build_site.py [myst build options]   (default: --html --strict)
"""

import logging
import os
import secrets
import socket
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

logging.basicConfig(level=logging.INFO, format="%(message)s", force=True)
log = logging.getLogger(__name__)

ROOT = Path(__file__).resolve().parent.parent
DEFAULT_ARGS = ["--html", "--strict"]
STARTUP_SECONDS = 60


def free_port() -> int:
    with socket.socket() as s:
        s.bind(("127.0.0.1", 0))
        return s.getsockname()[1]


def server_is_up(url: str, token: str) -> bool:
    try:
        with urllib.request.urlopen(f"{url}/api/status?token={token}", timeout=2):
            return True
    except (urllib.error.URLError, OSError):
        return False


def wait_for_server(proc: subprocess.Popen, url: str, token: str) -> None:
    deadline = time.monotonic() + STARTUP_SECONDS
    while not server_is_up(url, token):
        if proc.poll() is not None:
            raise SystemExit(f"Jupyter server exited with code {proc.returncode}")
        if time.monotonic() > deadline:
            raise SystemExit(f"Jupyter server not up after {STARTUP_SECONDS} s")
        time.sleep(0.5)


def main(myst_args: list[str]) -> int:
    port, token = free_port(), secrets.token_hex(16)
    url = f"http://127.0.0.1:{port}"
    server = subprocess.Popen(
        [
            sys.executable,
            "-m",
            "jupyter_server",
            "--no-browser",
            f"--ServerApp.root_dir={ROOT}",
            f"--ServerApp.port={port}",
            "--ServerApp.port_retries=0",
            f"--IdentityProvider.token={token}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    try:
        wait_for_server(server, url, token)
        log.info("Jupyter server up at %s", url)
        env = {**os.environ, "JUPYTER_BASE_URL": url, "JUPYTER_TOKEN": token}
        command = ["myst", "build", "--execute", *(myst_args or DEFAULT_ARGS)]
        return subprocess.run(command, cwd=ROOT, env=env, check=False).returncode
    finally:
        server.terminate()
        try:
            server.wait(timeout=30)
        except subprocess.TimeoutExpired:
            server.kill()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
