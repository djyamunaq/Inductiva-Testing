# coding: utf-8
"""
    InductivaWebAPI

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: 0.1.0
    Generated by: https://openapi-generator.tech
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from inductiva.client import schemas  # noqa: F401


class User(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    class MetaOapg:
        required = {
            "bucket_name",
            "email",
        }

        class properties:
            email = schemas.StrSchema
            bucket_name = schemas.StrSchema
            is_admin = schemas.BoolSchema
            __annotations__ = {
                "email": email,
                "bucket_name": bucket_name,
                "is_admin": is_admin,
            }

    bucket_name: MetaOapg.properties.bucket_name
    email: MetaOapg.properties.email

    @typing.overload
    def __getitem__(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["bucket_name"]
    ) -> MetaOapg.properties.bucket_name:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["is_admin"]
    ) -> MetaOapg.properties.is_admin:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "email",
        "bucket_name",
        "is_admin",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
            self, name: typing_extensions.Literal["email"]
    ) -> MetaOapg.properties.email:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["bucket_name"]
    ) -> MetaOapg.properties.bucket_name:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["is_admin"]
    ) -> typing.Union[MetaOapg.properties.is_admin, schemas.Unset]:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "email",
        "bucket_name",
        "is_admin",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        bucket_name: typing.Union[
            MetaOapg.properties.bucket_name,
            str,
        ],
        email: typing.Union[
            MetaOapg.properties.email,
            str,
        ],
        is_admin: typing.Union[MetaOapg.properties.is_admin, bool,
                               schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'User':
        return super().__new__(
            cls,
            *_args,
            bucket_name=bucket_name,
            email=email,
            is_admin=is_admin,
            _configuration=_configuration,
            **kwargs,
        )
