#!/bin/bash

# Find all yaml files in conf/ and create corresponding output directories
for config in conf/*.yaml; do
    if [ -f "$config" ]; then
        # Extract config name without path and extension
        config_name=$(basename "$config" .yaml)
        # Create output directory if it doesn't exist
        mkdir -p "outputs/${config_name}"
    fi
done
