from django import forms
from typing import Any

class InvalidJSONInput(str): ...
class JSONString(str): ...

class JSONField(forms.CharField):
    default_error_messages: Any = ...
    widget: Any = ...
    def to_python(self, value: Any): ...
    def bound_data(self, data: Any, initial: Any): ...
    def prepare_value(self, value: Any): ...
