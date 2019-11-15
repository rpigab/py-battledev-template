#!/usr/bin/env bash

set -eu

for f in ./data/input*.txt; do
    filename=$(basename -- "$f")
    filename="${filename%.*}"
    num=$(echo "$filename" | grep -o -E '[0-9]+' | head -1 | sed -e 's/^0\+//')
    printf "FILE #%s: %s\n" "${num}" "$f"
    outfile="./data/result${num}.out"
    ./src/main.py < "$f" > "$outfile" 2>/dev/null
    diff "$outfile" "./data/output${num}.txt" | sed 's/^/\t/'
    printf "END FILE #%s\n\n" "${num}"
done
