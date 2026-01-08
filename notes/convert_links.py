import os
import re

# Map of Term -> Relative Path (from project root)
# Updated to include .md extension for better MyST compatibility
LINK_MAP = {
    "Aggregation": "/notes/appendix/Aggregation.md",
    "ConsumptionFunction": "/notes/consumption/ConsumptionFunction.md",
    "EntrepreneurPF": "/notes/investment/EntrepreneurPF.md",
    "Envelope": "/notes/consumption/Envelope.md",
    "HallJorgenson": "/notes/investment/HallJorgenson.md",
    "MathFacts": "/notes/appendix/MathFactsList.md",
    "Math Facts": "/notes/appendix/MathFactsList.md",
    "PerfForesightCRRA": "/notes/consumption/PerfForesightCRRA.md",
    "RandomWalk": "/notes/consumption/RandomWalk.md",
    "Portfolio-CRRA": "/notes/asset_pricing/Portfolio-CRRA.md",
    "Portfolio-Multi-CRRA": "/notes/asset_pricing/Portfolio-Multi-CRRA.md",
    "CRRA-RateRisk": "/notes/consumption/CRRA-RateRisk.md",
    "iAndCashFlow": "/notes/investment/iAndCashFlow.md",
    "qModel": "/notes/investment/qModel.md",
    "Equiprobable": "/notes/appendix/Equiprobable.md"
}

ROOT_DIR = "/mnt/c/Users/alujan/GitHub/econ-ark/dsge/notes"

def process_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()
    
    original_content = content
    
    for term, link_path in LINK_MAP.items():
        # Regex: Look for 'Term section' NOT preceded by '['
        pattern = r'(?<!\[)\b' + re.escape(term) + r'\s+[sS]ection\b'
        
        def replacement(match):
            matched_text = match.group(0)
            return f"[{matched_text}]({link_path})"
            
        content = re.sub(pattern, replacement, content)
        
        # Also clean up previous conversion if it missed .md (e.g. if run twice)
        # Look for [Term section](/path/without/extension) and fix it
        # This is a bit specific, but safer to just re-run the main replacement on original text?
        # Actually, simpler: if the script is re-run, the first regex `(?<!\[)` will skip already converted links.
        # We need a separate pass to fix existing links that might be missing .md if I ran the previous script.
        
        # Regex to find links that I might have created and append .md if missing
        # Pattern: [Term section](/path/to/file) -> check if ends with .md
        clean_link_path = link_path.replace('.md', '') # Path without extension
        
        # Replace [text](path) with [text](path.md)
        # We look for exactly the path we know we inserted.
        existing_link_pattern = re.escape(f"({clean_link_path})") + r'(?!\.md)'
        # But this needs to be inside () of a link. 
        # Simpler: replace `](path)` with `](path.md)`
        
        content = content.replace(f"]({clean_link_path})", f"]({link_path})")


    if content != original_content:
        print(f"Modifying {filepath}")
        with open(filepath, 'w') as f:
            f.write(content)

for root, dirs, files in os.walk(ROOT_DIR):
    for file in files:
        if file.endswith(".md"):
            process_file(os.path.join(root, file))
