from _typeshed import Incomplete, SupportsLenAndGetItem

from antlr4.atn.ATN import ATN as ATN
from antlr4.error.Errors import IllegalStateException as IllegalStateException
from antlr4.RuleContext import RuleContext as RuleContext

class PredictionContext:
    EMPTY: Incomplete
    EMPTY_RETURN_STATE: int
    globalNodeCount: int
    id = globalNodeCount
    cachedHashCode: Incomplete
    def __init__(self, cachedHashCode: int) -> None: ...
    def __len__(self) -> int: ...
    def isEmpty(self): ...
    def hasEmptyPath(self): ...
    def getReturnState(self, index: int): ...
    def __hash__(self): ...

def calculateHashCode(parent: PredictionContext, returnState: int): ...
def calculateListsHashCode(parents: list[PredictionContext], returnStates: list[int]): ...

class PredictionContextCache:
    cache: Incomplete
    def __init__(self) -> None: ...
    def add(self, ctx: PredictionContext): ...
    def get(self, ctx: PredictionContext): ...
    def __len__(self) -> int: ...

class SingletonPredictionContext(PredictionContext):
    @staticmethod
    def create(parent: PredictionContext, returnState: int): ...
    parentCtx: Incomplete
    returnState: Incomplete
    def __init__(self, parent: PredictionContext, returnState: int) -> None: ...
    def __len__(self) -> int: ...
    def getParent(self, index: int): ...
    def getReturnState(self, index: int): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class EmptyPredictionContext(SingletonPredictionContext):
    def __init__(self) -> None: ...
    def isEmpty(self): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

class ArrayPredictionContext(PredictionContext):
    parents: Incomplete
    returnStates: Incomplete
    def __init__(self, parents: list[PredictionContext], returnStates: list[int]) -> None: ...
    def isEmpty(self): ...
    def __len__(self) -> int: ...
    def getParent(self, index: int): ...
    def getReturnState(self, index: int): ...
    def __eq__(self, other): ...
    def __hash__(self): ...

def PredictionContextFromRuleContext(atn: ATN, outerContext: RuleContext | None = None): ...
def merge(
    a: PredictionContext,
    b: PredictionContext,
    rootIsWildcard: bool,
    mergeCache: dict[tuple[Incomplete, Incomplete], SingletonPredictionContext] | None,
): ...
def mergeSingletons(
    a: SingletonPredictionContext,
    b: SingletonPredictionContext,
    rootIsWildcard: bool,
    mergeCache: dict[tuple[Incomplete, Incomplete], SingletonPredictionContext] | None,
): ...
def mergeRoot(a: SingletonPredictionContext, b: SingletonPredictionContext, rootIsWildcard: bool): ...
def mergeArrays(
    a: ArrayPredictionContext,
    b: ArrayPredictionContext,
    rootIsWildcard: bool,
    mergeCache: dict[tuple[Incomplete, Incomplete], SingletonPredictionContext] | None,
): ...
def combineCommonParents(parents: SupportsLenAndGetItem[PredictionContext]): ...
def getCachedPredictionContext(
    context: PredictionContext, contextCache: PredictionContextCache, visited: dict[PredictionContext, PredictionContext]
): ...
def getAllContextNodes(
    context: PredictionContext,
    nodes: list[Incomplete] | None = None,
    visited: dict[PredictionContext, PredictionContext] | None = None,
): ...
