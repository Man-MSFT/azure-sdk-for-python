# coding: utf-8

# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

"""
FILE: sample_list_tags_async.py

DESCRIPTION:
    This sample demonstrates listing the tags for an image in a repository with anonymous pull access.
    Anonymous access allows a user to list all the collections there, but they wouldn't have permissions to
    modify or delete any of the images in the registry.

USAGE:
    python sample_list_tags_async.py

    Set the environment variables with your own values before running the sample:
    1) CONTAINERREGISTRY_ENDPOINT - The URL of you Container Registry account

    This sample assumes your registry has a repository "library/hello-world".
"""
import asyncio
import os
from dotenv import find_dotenv, load_dotenv
from azure.containerregistry.aio import ContainerRegistryClient
from samples.sample_utilities import load_registry, get_authority, get_audience, get_credential


class ListTagsAsync(object):
    def __init__(self):
        load_dotenv(find_dotenv())
        self.endpoint = os.environ.get("CONTAINERREGISTRY_ENDPOINT")
        self.authority = get_authority(self.endpoint)
        self.audience = get_audience(self.authority)
        self.credential = get_credential(
            self.authority, exclude_environment_credential=True, is_async=True
        )

    async def list_tags(self):
        load_registry()
        # Instantiate an instance of ContainerRegistryClient    
        async with ContainerRegistryClient(self.endpoint, self.credential, audience=self.audience) as client:
            manifest = await client.get_manifest_properties("library/hello-world", "latest")
            print("Tags of " + manifest.repository_name + ": ")
            # Iterate through all the tags
            for tag in manifest.tags:
                print(tag)


async def main():
    sample = ListTagsAsync()
    await sample.list_tags()


if __name__ == "__main__":
    asyncio.run(main())
