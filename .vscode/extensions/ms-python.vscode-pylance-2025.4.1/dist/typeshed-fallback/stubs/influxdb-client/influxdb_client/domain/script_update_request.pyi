from _typeshed import Incomplete

class ScriptUpdateRequest:
    openapi_types: Incomplete
    attribute_map: Incomplete
    discriminator: Incomplete
    def __init__(self, description: Incomplete | None = None, script: Incomplete | None = None) -> None: ...
    @property
    def description(self): ...
    @description.setter
    def description(self, description) -> None: ...
    @property
    def script(self): ...
    @script.setter
    def script(self, script) -> None: ...
    def to_dict(self): ...
    def to_str(self): ...
    def __eq__(self, other): ...
    def __ne__(self, other): ...
