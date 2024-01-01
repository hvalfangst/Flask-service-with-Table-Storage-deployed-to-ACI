import json
import os

from azure.core.credentials import AzureNamedKeyCredential

config_json = ""
access_key = ""
account_name = "hvalfangststorageaccount"
table_name = "hvalfangststoragetable"
endpoint = f"https://{account_name}.table.core.windows.net"
partition_key = "Heroes"
filter_query_all_heroes = "PartitionKey eq 'Heroes'"


def get_credential() -> AzureNamedKeyCredential:
    config_file_path = os.environ.get("CONFIG_FILE_PATH")

    if config_file_path is None:
        raise ValueError("Environment variable CONFIG_FILE_PATH is not set.")

    with open(config_file_path, "r") as config_file:
        global config_json, access_key
        config_json = json.load(config_file)
        access_key = config_json["credential"]["key"]
        return AzureNamedKeyCredential(account_name, access_key)