import json
from azure.core.credentials import AzureNamedKeyCredential

config_json = ""
access_key = ""
account_name = "hvalfangststorageaccount"
table_name = "hvalfangststoragetable"
endpoint = f"https://{account_name}.table.core.windows.net"
partition_key = "Heroes"
filter_query_all_heroes = "PartitionKey eq 'Heroes'"


def get_credential() -> AzureNamedKeyCredential:
    with open("python/config.json", "r") as config_file:
        global config_json, access_key
        config_json = json.load(config_file)
        access_key = config_json["credential"]["key"]
        return AzureNamedKeyCredential(account_name, access_key)