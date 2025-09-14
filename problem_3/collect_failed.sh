#!/bin/bash

mkdir -p failed_subdirectories

find . -path ./failed_subdirectories -prune -o -type f -name "STATUS_FAILED" -print | while read filepath; do
    dirpath=$(dirname "$filepath")
    dirname=$(basename "$dirpath")
    cp -r "$dirpath" "failed_subdirectories/$dirname"
done

echo "✅ Done: All failed subdirectories copied to 'failed_subdirectories/'"

