#!/bin/sh

# Exits immediately if a command exits with a non-zero status
set -e

echo "Logging in to Azure..."
az login;

echo "Initializing Terraform..."
terraform -chdir=infra init;

echo "Planning Azure resource provisioning..."
terraform -chdir=infra plan;

echo "Applying planned Azure resource provisioning..."
terraform -chdir=infra apply;