# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/datatypes/keypoint_pair.fbs".

# You can extend this class by creating a "KeypointPairExt" class in "keypoint_pair_ext.py".

from __future__ import annotations

from collections.abc import Sequence
from typing import TYPE_CHECKING, Any, Union

import pyarrow as pa
from attrs import define, field

from .. import datatypes
from .._baseclasses import (
    BaseBatch,
)
from .keypoint_pair_ext import KeypointPairExt

__all__ = ["KeypointPair", "KeypointPairArrayLike", "KeypointPairBatch", "KeypointPairLike"]


def _keypoint_pair__keypoint0__special_field_converter_override(x: datatypes.KeypointIdLike) -> datatypes.KeypointId:
    if isinstance(x, datatypes.KeypointId):
        return x
    else:
        return datatypes.KeypointId(x)


def _keypoint_pair__keypoint1__special_field_converter_override(x: datatypes.KeypointIdLike) -> datatypes.KeypointId:
    if isinstance(x, datatypes.KeypointId):
        return x
    else:
        return datatypes.KeypointId(x)


@define(init=False)
class KeypointPair(KeypointPairExt):
    """**Datatype**: A connection between two [`datatypes.KeypointId`][rerun.datatypes.KeypointId]s."""

    def __init__(self: Any, keypoint0: datatypes.KeypointIdLike, keypoint1: datatypes.KeypointIdLike) -> None:
        """
        Create a new instance of the KeypointPair datatype.

        Parameters
        ----------
        keypoint0:
            The first point of the pair.
        keypoint1:
            The second point of the pair.

        """

        # You can define your own __init__ function as a member of KeypointPairExt in keypoint_pair_ext.py
        self.__attrs_init__(keypoint0=keypoint0, keypoint1=keypoint1)

    keypoint0: datatypes.KeypointId = field(converter=_keypoint_pair__keypoint0__special_field_converter_override)
    # The first point of the pair.
    #
    # (Docstring intentionally commented out to hide this field from the docs)

    keypoint1: datatypes.KeypointId = field(converter=_keypoint_pair__keypoint1__special_field_converter_override)
    # The second point of the pair.
    #
    # (Docstring intentionally commented out to hide this field from the docs)


if TYPE_CHECKING:
    KeypointPairLike = Union[KeypointPair, Sequence[datatypes.KeypointIdLike]]
else:
    KeypointPairLike = Any

KeypointPairArrayLike = Union[
    KeypointPair,
    Sequence[KeypointPairLike],
]


class KeypointPairBatch(BaseBatch[KeypointPairArrayLike]):
    _ARROW_DATATYPE = pa.struct([
        pa.field("keypoint0", pa.uint16(), nullable=False, metadata={}),
        pa.field("keypoint1", pa.uint16(), nullable=False, metadata={}),
    ])

    @staticmethod
    def _native_to_pa_array(data: KeypointPairArrayLike, data_type: pa.DataType) -> pa.Array:
        return KeypointPairExt.native_to_pa_array_override(data, data_type)
