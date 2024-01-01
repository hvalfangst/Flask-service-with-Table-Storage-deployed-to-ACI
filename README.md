# Flask service with Azure Table Storage deployed to ACI

Python REST service developed with Flask deployed to Azure Container Instances. 
The application utilizes Azure Table Storage as means of persistence. 
Deployment is achieved by GitHub Actions Workflow script enabling CI/CD. 
Resources provisioned with Terraform.

## Requirements

* x86-64
* Linux/Unix
* [Python](https://www.python.org/downloads/)

## Creating resources

The shell script 'up' allocates Azure resources with Terraform.

## Deleting resources

The shell script 'down' deallocates Azure resources.

## Running Flask app locally 

The shell script 'run' configures and runs our Flask application.