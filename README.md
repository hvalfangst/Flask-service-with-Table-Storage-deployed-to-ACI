# Flask service with Azure Table Storage deployed to ACI

Python REST service developed with Flask deployed to Azure Container Instances. 
The application utilizes Azure Table Storage as means of persistence. 
Deployment is achieved by GitHub Actions Workflow script enabling CI/CD. 
Resources provisioned with Terraform.

## Requirements

* x86-64
* Linux/Unix
* [Python](https://www.python.org/downloads/)
* [Docker](https://www.docker.com/products/docker-desktop/)

## Creating resources

The shell script 'up' allocates Azure resources with Terraform.

## Deleting resources

The shell script 'down' deallocates Azure resources.

## Running Flask app locally 

The shell script 'run' configures and runs our Flask application.

## Guide

### 1. Provision Azure Resources

- Run the 'up' script to provision Azure resources.

### 2. Access Azure Portal

- Open your browser and navigate to the Azure Portal.

### 3. Container Registry Setup

- Go to the newly provisioned Container Registry named 'hvalfangstcontainerregistry'.
- Click on 'Access keys' under the 'Settings' section.
- Copy the registry name and password for future use.

### 4. Microsoft Entra ID Setup

- Navigate to 'Microsoft Entra ID' using the search bar.
- Click on 'Add' and choose 'App registration'.
- Set name to 'hvalfangst-flask-table-storage', account option to 'Single tenant', and click 'Register'.
- Go to the overview of the newly created app registration 'hvalfangst-flask-table-storage'.
- Copy values associated with Application (client) ID and Directory (tenant) ID for future use.
- Navigate to 'Certificates & secrets' under 'Manage'.
- Click 'Add credential' under 'Federated credentials'.
- Choose the scenario: 'GitHub Actions deploying Azure resources'.
- Set GitHub account name and Repo name.
- Set Entity type to 'Environment' and the associated value to 'Production'.
- Set a fitting name under Credential detail name.

### 5. Subscription Setup

- Navigate to your subscription, which holds your provisioned resource group.
- Copy your subscription ID for future use.
- Click on 'Add' under 'Access control (IAM)' and pick 'role assignment'.
- Choose the role 'Contributor' under 'Privileged administrator roles'.
- Navigate to the 'Members' section and click 'Select members'.
- Search for the app registration 'hvalfangst-flask-table-storage' and assign the role.

### 6. GitHub Repository Secrets

- Open the 'Settings' tab of your GitHub repository.
- Click on 'Actions' under 'Security' -> 'Secrets and variables'.
- Create the following repository secrets:
    - ACR_USERNAME: Value copied in step #3
    - ACR_PASSWORD: Value copied in step #3
    - AZURE_CLIENT_ID: Value copied in step #4
    - AZURE_TENANT_ID: Value copied in step #4
    - AZURE_SUBSCRIPTION_ID: Value copied in step #5

### 7. Deploy Workflow

The GitHub Actions workflow will automatically build, package, and deploy new versions of the app to your Azure environment on repository pushes.