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


class InductivaHostInfo(schemas.DictSchema):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.

    Info about the Inductiva server hosting the executer.
    """

    class MetaOapg:
        required = {
            "hostname",
            "host_type",
        }

        class properties:

            class host_type(schemas.EnumBase, schemas.StrSchema):

                class MetaOapg:
                    enum_value_to_name = {
                        "inductiva-hardware": "INDUCTIVAHARDWARE",
                    }

                @schemas.classproperty
                def INDUCTIVAHARDWARE(cls):
                    return cls("inductiva-hardware")

            hostname = schemas.StrSchema
            __annotations__ = {
                "host_type": host_type,
                "hostname": hostname,
            }

    hostname: MetaOapg.properties.hostname
    host_type: MetaOapg.properties.host_type

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["host_type"]
    ) -> MetaOapg.properties.host_type:
        ...

    @typing.overload
    def __getitem__(
        self, name: typing_extensions.Literal["hostname"]
    ) -> MetaOapg.properties.hostname:
        ...

    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema:
        ...

    def __getitem__(self, name: typing.Union[typing_extensions.Literal[
        "host_type",
        "hostname",
    ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["host_type"]
    ) -> MetaOapg.properties.host_type:
        ...

    @typing.overload
    def get_item_oapg(
        self, name: typing_extensions.Literal["hostname"]
    ) -> MetaOapg.properties.hostname:
        ...

    @typing.overload
    def get_item_oapg(
            self, name: str
    ) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]:
        ...

    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal[
        "host_type",
        "hostname",
    ], str]):
        return super().get_item_oapg(name)

    def __new__(
        cls,
        *_args: typing.Union[
            dict,
            frozendict.frozendict,
        ],
        hostname: typing.Union[
            MetaOapg.properties.hostname,
            str,
        ],
        host_type: typing.Union[
            MetaOapg.properties.host_type,
            str,
        ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict,
                               frozendict.frozendict, str, date, datetime,
                               uuid.UUID, int, float, decimal.Decimal, None,
                               list, tuple, bytes],
    ) -> 'InductivaHostInfo':
        return super().__new__(
            cls,
            *_args,
            hostname=hostname,
            host_type=host_type,
            _configuration=_configuration,
            **kwargs,
        )
