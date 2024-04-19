#!/bin/bash

# Navigate to the directory containing the .tar.gz files
cd ./data

# Loop through each .tar.gz file
for file in *.tar.gz; do
    # Check if the file exists and is a regular file
    if [ -f "$file" ]; then
        # Extract the file
        echo "Extracting $file..."
        tar -xzf "$file"
    else
        echo "$file is not a regular file or does not exist."
    fi
done

echo "Extraction completed."
