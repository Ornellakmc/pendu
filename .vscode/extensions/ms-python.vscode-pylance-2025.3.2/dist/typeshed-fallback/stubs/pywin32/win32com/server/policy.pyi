from _typeshed import Incomplete
from abc import ABC, abstractmethod

S_OK: int
IDispatchType: Incomplete
IUnknownType: Incomplete
regSpec: str
regPolicy: str
regDispatcher: str
regAddnPath: str

def CreateInstance(clsid, reqIID): ...

class BasicWrapPolicy(ABC):
    def __init__(self, object) -> None: ...
    def _InvokeEx_(self, dispid, lcid, wFlags, args, kwargs, serviceProvider) -> tuple[Incomplete]: ...
    @abstractmethod
    def _invokeex_(self, dispid, lcid, wFlags, args, kwargs, serviceProvider) -> tuple[Incomplete]: ...

class MappedWrapPolicy(BasicWrapPolicy):
    _dispid_to_func_: dict[int, str]
    def _invokeex_(self, dispid, lcid, wFlags, args, kwargs, serviceProvider) -> tuple[Incomplete]: ...

class DesignatedWrapPolicy(MappedWrapPolicy): ...
class EventHandlerPolicy(DesignatedWrapPolicy): ...

class DynamicPolicy(BasicWrapPolicy):
    def _invokeex_(self, dispid, lcid, wFlags, args, kwargs, serviceProvider) -> tuple[Incomplete]: ...

DefaultPolicy = DesignatedWrapPolicy

def resolve_func(spec): ...
def call_func(spec, *args): ...

DISPATCH_METHOD: int
DISPATCH_PROPERTYGET: int
DISPATCH_PROPERTYPUT: int
DISPATCH_PROPERTYPUTREF: int
DISPID_EVALUATE: int
DISPID_NEWENUM: int
DISPID_PROPERTYPUT: int
DISPID_STARTENUM: int
DISPID_VALUE: int
