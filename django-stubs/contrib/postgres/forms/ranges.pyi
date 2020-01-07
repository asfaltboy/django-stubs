from django import forms
from django.forms.widgets import MultiWidget
from typing import Any, Callable, Optional

_OptAttrs = Dict[str, Any]

class BaseRangeField(forms.MultiValueField):
    def __init__(self, **kwargs: Any) -> None: ...
    def compress(self, values: Any) -> Tuple[Optional[Callable], Optional[Callable]]: ...

class IntegerRangeField(BaseRangeField): ...
class FloatRangeField(BaseRangeField): ...
class DateTimeRangeField(BaseRangeField): ...
class DateRangeField(BaseRangeField): ...

class RangeWidget(MultiWidget):
    def __init__(self, base_widget: forms.Widget, attrs: Optional[_OptAttrs] = ...) -> None: ...
    def decompress(self, value: Any) -> List: ...
