# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from inductiva.client.paths.storage_dir_name.delete import DeleteDirectory
from inductiva.client.paths.storage_size.get import GetStorageSize
from inductiva.client.paths.storage_contents.get import ListStorageContents


class StorageApi(
        DeleteDirectory,
        GetStorageSize,
        ListStorageContents,
):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    pass