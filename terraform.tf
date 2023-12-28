terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "3.49.0"
    }
  }
}

provider "azurerm" {
  features {}
}

resource "azurerm_resource_group" "hvalfangst" {
  name     = "hvalfangstresourcegroup"
  location = "West Europe"
}

resource "azurerm_storage_account" "hvalfangst" {
  name                     = "hvalfangststorageaccount"
  resource_group_name      = azurerm_resource_group.hvalfangst.name
  location                 = azurerm_resource_group.hvalfangst.location
  account_tier             = "Standard"
  account_replication_type = "LRS"
}

resource "azurerm_storage_table" "hvalfangst" {
  name                 = "hvalfangststoragetable"
  storage_account_name = azurerm_storage_account.hvalfangst.name
}