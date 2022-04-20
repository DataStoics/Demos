# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
# Docs: https://docs.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0&tabs=http
#pylint: disable=undefined-variable
"""Demonstrates using the GraphClient to make HTTP Requests to Microsoft Graph"""
from dis import dis
import json
from pprint import pprint

# Any azure-identity TokenCredential class will work the same.
from azure.identity import ClientSecretCredential

from msgraph.core import GraphClient

credential = ClientSecretCredential(
    client_id='',
    client_secret='',
    tenant_id=''
)
client = GraphClient(credential=credential)


def get_all_users():
    """
    Retrieve a list of user objects.
    ---
    Permission type: Application
    Permissions (from least to most privileged): User.Read.All, User.ReadWrite.All, Directory.Read.All, Directory.ReadWrite.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/user-list?view=graph-rest-1.0&tabs=http
    """
    result = client.get('/users')
    pprint(result.json())


def get_user_by_upn(upn):
    """
    Retrieve the properties and relationships of user object.

    Permission type: Application
    Permissions (from least to most privileged): User.Read.All, User.ReadWrite.All, Directory.Read.All, Directory.ReadWrite.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/user-get?view=graph-rest-1.0&tabs=http
    """
    result = client.get(f'/users/{upn}')
    pprint(result.json())


def get_all_groups():
    """
    List all the groups in an organization, including but not limited to Microsoft 365 groups.
    ---
    Permission type: Application
    Permissions (from least to most privileged): GroupMember.Read.All, Group.Read.All, Directory.Read.All, Group.ReadWrite.All, Directory.ReadWrite.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/group-list?view=graph-rest-1.0&tabs=http
    """
    result = client.get('/groups')
    pprint(result.json())


def get_group_by_id(id):
    """
    Get the properties and relationships of a group object.
    ---
    Permission type: Application
    Permissions (from least to most privileged): GroupMember.Read.All, Group.Read.All, Directory.Read.All, Group.ReadWrite.All, Directory.ReadWrite.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/group-get?view=graph-rest-1.0&tabs=http
    """
    result = client.get(f'/groups/{id}')
    pprint(result.json())


def create_group(description, displayName, mailNickname, owners, members):
    """
    Create a new group as specified in the request body.
    ---
    Permission type: Application
    Permissions (from least to most privileged): Group.Create, Group.ReadWrite.All, Directory.ReadWrite.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/group-post-groups?view=graph-rest-1.0&tabs=http
    """
    body = {
        "description": description,
        "displayName": displayName,
        "groupTypes": [],
        "mailEnabled": False,
        "mailNickname": mailNickname,
        "securityEnabled": True,
        "owners@odata.bind": owners,
        "members@odata.bind": members
    }

    result = client \
        .post('/groups',
              data=json.dumps(body),
              headers={'Content-Type': 'application/json'}
              )
    pprint(result.status_code)


def get_all_service_principals():
    """
    Retrieve a list of servicePrincipal objects.
    ---
    Permission type: Application
    Permissions (from least to most privileged): Application.Read.All, Application.ReadWrite.All, Directory.Read.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/serviceprincipal-list?view=graph-rest-1.0&tabs=http
    """
    result = client.get('/servicePrincipals')
    pprint(result.json())


def get_service_principal_by_id(id):
    """
    Get the properties and relationships of a group object.
    ---
    Permission type: Application
    Permissions (from least to most privileged): Application.Read.All, Application.ReadWrite.All, Directory.Read.All
    ---
    Docs: https://docs.microsoft.com/en-us/graph/api/serviceprincipal-get?view=graph-rest-1.0&tabs=http
    """
    result = client.get(f'/servicePrincipals/{id}')
    pprint(result.json())


if __name__ == '__main__':
    # Users API
    get_all_users()
    get_user_by_upn('upn')
    # Groups API
    get_all_groups()
    create_group(
        description="Demo - Create AD Group",
        displayName="demoADGroup",
        mailNickname="demoADGroup",
        owners=["https://graph.microsoft.com/v1.0/users/<object_id>"],
        members=[
            "https://graph.microsoft.com/v1.0/users/<object_id>",  # User
            "https://graph.microsoft.com/v1.0/servicePrincipals/<object_id>"  # Service Principal
        ]
    )
    get_group_by_id('6cd20bec-3635-4a19-8a1d-2eb461b5cfb6')
    # ServicePrincipal API
    get_all_service_principals()
    get_service_principal_by_id(
        ''
    )  # Object Id from Enterprise Application section
