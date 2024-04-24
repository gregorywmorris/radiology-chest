#!/bin/bash

# Navigate to the directory containing the .tar.gz files
cd ./data

# Delete all .tar.gz files
echo "Deleting .tar.gz files..."
find . -type f -name '*.tar.gz' -delete

echo "Deletion completed."
