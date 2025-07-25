# DO NOT EDIT! This file was auto-generated by crates/build/re_types_builder/src/codegen/python/mod.rs
# Based on "crates/store/re_types/definitions/rerun/components/colormap.fbs".

# You can extend this class by creating a "ColormapExt" class in "colormap_ext.py".

from __future__ import annotations

from collections.abc import Sequence
from typing import Literal, Union

import pyarrow as pa

from .._baseclasses import (
    BaseBatch,
    ComponentBatchMixin,
)

__all__ = ["Colormap", "ColormapArrayLike", "ColormapBatch", "ColormapLike"]


from enum import Enum


class Colormap(Enum):
    """
    **Component**: Colormap for mapping scalar values within a given range to a color.

    This provides a number of popular pre-defined colormaps.
    In the future, the Rerun Viewer will allow users to define their own colormaps,
    but currently the Viewer is limited to the types defined here.
    """

    Grayscale = 1
    """
    A simple black to white gradient.

    This is a sRGB gray gradient which is perceptually uniform.
    """

    Inferno = 2
    """
    The Inferno colormap from Matplotlib.

    This is a perceptually uniform colormap.
    It interpolates from black to red to bright yellow.
    """

    Magma = 3
    """
    The Magma colormap from Matplotlib.

    This is a perceptually uniform colormap.
    It interpolates from black to purple to white.
    """

    Plasma = 4
    """
    The Plasma colormap from Matplotlib.

    This is a perceptually uniform colormap.
    It interpolates from dark blue to purple to yellow.
    """

    Turbo = 5
    """
    Google's Turbo colormap map.

    This is a perceptually non-uniform rainbow colormap addressing many issues of
    more traditional rainbow colormaps like Jet.
    It is more perceptually uniform without sharp transitions and is more colorblind-friendly.
    Details: <https://research.google/blog/turbo-an-improved-rainbow-colormap-for-visualization/>
    """

    Viridis = 6
    """
    The Viridis colormap from Matplotlib

    This is a perceptually uniform colormap which is robust to color blindness.
    It interpolates from dark purple to green to yellow.
    """

    CyanToYellow = 7
    """
    Rasmusgo's Cyan to Yellow colormap

    This is a perceptually uniform colormap which is robust to color blindness.
    It is especially suited for visualizing signed values.
    It interpolates from cyan to blue to dark gray to brass to yellow.
    """

    @classmethod
    def auto(cls, val: str | int | Colormap) -> Colormap:
        """Best-effort converter, including a case-insensitive string matcher."""
        if isinstance(val, Colormap):
            return val
        if isinstance(val, int):
            return cls(val)
        try:
            return cls[val]
        except KeyError:
            val_lower = val.lower()
            for variant in cls:
                if variant.name.lower() == val_lower:
                    return variant
        raise ValueError(f"Cannot convert {val} to {cls.__name__}")

    def __str__(self) -> str:
        """Returns the variant name."""
        return self.name


ColormapLike = Union[
    Colormap,
    Literal[
        "CyanToYellow",
        "Grayscale",
        "Inferno",
        "Magma",
        "Plasma",
        "Turbo",
        "Viridis",
        "cyantoyellow",
        "grayscale",
        "inferno",
        "magma",
        "plasma",
        "turbo",
        "viridis",
    ],
    int,
]
ColormapArrayLike = Union[ColormapLike, Sequence[ColormapLike]]


class ColormapBatch(BaseBatch[ColormapArrayLike], ComponentBatchMixin):
    _ARROW_DATATYPE = pa.uint8()
    _COMPONENT_TYPE: str = "rerun.components.Colormap"

    @staticmethod
    def _native_to_pa_array(data: ColormapArrayLike, data_type: pa.DataType) -> pa.Array:
        if isinstance(data, (Colormap, int, str)):
            data = [data]

        pa_data = [Colormap.auto(v).value if v is not None else None for v in data]  # type: ignore[redundant-expr]

        return pa.array(pa_data, type=data_type)
