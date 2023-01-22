from dataclasses import dataclass
from typing import Any, TypeVar, Type, cast

T = TypeVar("T")


def to_class(c: Type[T], x: Any) -> dict:
    assert isinstance(x, c)
    return cast(Any, x).to_dict()


@dataclass
class ArgsModel:
    label: any
    message: any
    label_color: any
    background_color: any
    logo_spacing: any
    logo: any
    style: any
    has_label: any

    @staticmethod
    def from_dict(obj: Any) -> 'ArgsModel':
        assert isinstance(obj, dict)
        label = obj.get("label")
        message = obj.get("message")
        label_color = obj.get("labelColor")
        background_color = obj.get("backgroundColor")
        logo_spacing = obj.get("logoSpacing")
        logo = obj.get("logo")
        style = obj.get("style")
        has_label = obj.get("hasLabel")
        return ArgsModel(label, message, label_color, background_color, logo_spacing, logo, style, has_label)

    def to_dict(self) -> dict:
        result: dict = {"label": self.label, "message": self.message,
                        "labelColor": self.label_color, "backgroundColor": self.background_color,
                        "logoSpacing": self.logo_spacing, "logo": self.logo,
                        "style": self.style, "hasLabel": self.has_label}
        return result


def args_model_from_dict(s: Any) -> ArgsModel:
    return ArgsModel.from_dict(s)


def args_model_to_dict(x: ArgsModel) -> Any:
    return to_class(ArgsModel, x)
