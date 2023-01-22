from urllib.parse import urlencode

from src.constants.constants import custom_icon
from src.controller.view_controller import ViewsCounter
from src.helpers.has_label_checker import has_label_check
from src.helpers.short_number_converter import short_number


def get_svg_url(
        views_counter: ViewsCounter,
        label, color, logo_width, style, label_color,
        logo, has_label) -> str:
    """
    Generate the URL for the SVG image of the view counter.

    :return: the SVG image URL
    """
    print(has_label_check(has_label, label))
    params = {
        "label": has_label_check(has_label, label),
        "message": short_number(views_counter.data["hit"]),
        "labelColor": "BB33FF" if label_color is None else label_color,
        "color": "DF33FF" if color is None else color,
        "logoWidth": 28 if logo_width is None else logo_width,
        "logo": custom_icon if logo is None else logo,
        "style": "for-the-badge" if style is None else style
    }
    return "https://img.shields.io/static/v1?" + urlencode(params)
