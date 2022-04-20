import os, uuid, sys
from azure.storage.filedatalake import DataLakeServiceClient
from azure.identity import CertificateCredential

def initialize_storage_account_ad(storage_account_name, client_id, certificate_path, tenant_id):
    try:  
        global service_client
        credential = CertificateCredential(tenant_id, client_id, certificate_path)
        service_client = DataLakeServiceClient(account_url="{}://{}.dfs.core.windows.net".format(
            "https", storage_account_name), credential=credential)
    except Exception as e:
        print(e)


def create_blob_inventory():
    try:
        file_systems = service_client.list_file_systems()

        for file_system in file_systems:
            file_system_size = calculate_file_system_size(file_system)
            print(f"{file_system.name}: {file_system_size}")  
        

    except Exception as e:
        print(e)


def calculate_file_system_size(file_system):
    try:
        file_system_client = service_client.get_file_system_client(file_system=file_system)
        paths = file_system_client.get_paths()

        file_system_size = 0 

        for path in paths:
            file_size = get_blob_size(file_system_client, path)
            file_system_size += file_size

        return file_system_size  

    except Exception as e:
     print(e)


def get_blob_size(file_system_client, file_path):
    try:
        file_client = file_system_client.get_file_client(file_path=file_path)
        return file_client.get_file_properties().size
    
    except Exception as e:
        print(e) 


if __name__ == '__main__':
    client_id = ""
    tenant_id = ""
    certificate_path = "" # path to a certificate file in PEM or PKCS12 format, including the private key
    storage_account_name = ""

    initialize_storage_account_ad(storage_account_name, client_id, certificate_path, tenant_id)
    create_blob_inventory()