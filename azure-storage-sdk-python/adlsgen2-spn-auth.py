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


def list_directory_contents(file_system, directory_path):
    try:
        file_system_client = service_client.get_file_system_client(file_system=file_system)
        paths = file_system_client.get_paths(path=directory_path)

        for path in paths:
            print(path.name + '\n')

    except Exception as e:
     print(e)
 

if __name__ == '__main__':
    client_id = ""
    tenant_id = ""
    certificate_path = "" # path to a certificate file in PEM or PKCS12 format, including the private key
    storage_account_name = ""
    file_system = ""
    directory_path = ""

    initialize_storage_account_ad(storage_account_name, client_id, certificate_path, tenant_id)
    list_directory_contents(file_system, directory_path)