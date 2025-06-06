from collections.abc import Mapping

from ._typing import *
from .colors import Colormap, Normalize

class __getattr__:
    LUTSIZE = ...

class ColormapRegistry(Mapping):
    def __init__(self, cmaps) -> None: ...
    def __getitem__(self, item: str): ...
    def __iter__(self): ...
    def __len__(self) -> int: ...
    def __call__(self): ...
    def register(self, cmap: Colormap, *, name: str = ..., force: bool = ...) -> None: ...
    def unregister(self, name: str) -> None: ...

def register_cmap(name: str = ..., cmap: Colormap = ..., *, override_builtin: bool = ...) -> None: ...
def get_cmap(name: Colormap | str | None = ..., lut: int | None = ...) -> Colormap: ...
def unregister_cmap(name: str) -> Colormap | None: ...

class ScalarMappable:
    def __init__(self, norm: Normalize | None = ..., cmap: str | Colormap = ...) -> None: ...
    callbacksSM = ...
    def to_rgba(self, x, alpha=..., bytes=..., norm=...) -> tuple[float, float, float, float]: ...
    def set_array(self, A: ArrayLike | None) -> None: ...
    def get_array(self): ...
    def get_cmap(self) -> Colormap: ...
    def get_clim(self) -> tuple: ...
    def set_clim(self, vmin: float = ..., vmax: float = ...) -> None: ...
    def get_alpha(self) -> float: ...
    def set_cmap(self, cmap: Colormap | str | None) -> None: ...
    @property
    def norm(self) -> Normalize: ...
    @norm.setter
    def norm(self, norm: Normalize) -> None: ...
    def set_norm(self, norm: Normalize | None): ...
    def autoscale(self) -> None: ...
    def autoscale_None(self) -> None: ...
    def changed(self) -> None: ...
