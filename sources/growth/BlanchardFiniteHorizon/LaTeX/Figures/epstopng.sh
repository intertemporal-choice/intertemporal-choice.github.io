#!/bin/sh
# Usage: epstojpg file.eps file.jpg

BBOX=~/Downloads/bbox.ps

INPUT_FILE=$1
OUTPUT_FILE=$2

# Convert eps to jpeg
gs   -q -dNOPAUSE -dBATCH -r300 -sDEVICE=jpeg -dJPEGQ=100 \
      -dGraphicsAlphaBits=4 -dTextAlphaBits=4 \
      -sOutputFile=$OUTPUT_FILE -c "/showpage { } def " -f $INPUT_FILE \
      -c "systemdict /showpage get exec quit"

mogrify -trim -resize 150% $OUTPUT_FILE
