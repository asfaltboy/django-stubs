from typing import Any, Iterable, List, Optional, Type, Union

from django import forms as forms

class SimpleArrayField(forms.CharField):
    base_field: forms.Field = ...
    delimiter: str = ...
    min_length: Optional[Union[int, str]] = ...
    max_length: Optional[Union[int, str]] = ...
    def __init__(
        self,
        base_field: forms.Field,
        *,
        delimiter: str = ...,
        max_length: Optional[Any] = ...,
        min_length: Optional[Any] = ...,
        **kwargs: Any
    ) -> None: ...
    def to_python(self, value: Optional[Iterable]) -> List: ...
    def validate(self, value: Optional[Iterable]) -> None: ...
    def run_validators(self, value: Optional[Iterable]) -> None: ...

class SplitArrayWidget(forms.Widget):
    template_name: str = ...
    widget: forms.Widget = ...
    size: int = ...
    def __init__(self, widget: Union[forms.Widget, Type[forms.Widget]], size: int, **kwargs: Any) -> None: ...
    def value_from_datadict(self, data: Dict[str, Any], files: Mapping[str, Iterable[Any]], name: str) -> List: ...
    @property
    def needs_multipart_form(self) -> bool: ...

class SplitArrayField(forms.Field):
    base_field: forms.Field = ...
    size: int = ...
    remove_trailing_nulls: bool = ...
    def __init__(
        self, base_field: forms.Field, size: int, *, remove_trailing_nulls: bool = ..., **kwargs: Any
    ) -> None: ...
    def to_python(self, value: Optional[Iterable]) -> List: ...
    def clean(self, value: Any) -> List: ...
