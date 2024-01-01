#!/bin/sh

# Exits immediately if a command exits with a non-zero status
set -e

echo "Retrieving storage account keys..."
az storage account keys list -g hvalfangstresourcegroup -n hvalfangststorageaccount > result.json;

echo "Setting up application environment..."
python setup.py;

echo "Starting Flask server..."
python python/main.py