from urllib.parse import urlencode

from src.constants.constants import custom_icon
from src.controller.view_controller import ViewsCounter
from src.helpers.short_number_converter import short_number


def get_svg_url(
        views_counter: ViewsCounter,
        label, color, logo_width, style, label_color,
        logo) -> str:
    """
    Generate the URL for the SVG image of the view counter.

    :return: the SVG image URL
    """
    params = {
        "label": "Visitors" if label is None else label,
        "message": short_number(views_counter.data["hit"]),
        "labelColor": "BB33FF" if label_color is None else label_color,
        "color": "DF33FF" if color is None else color,
        "logoWidth": 28 if logo_width is None else logo_width,
        "logo": custom_icon if logo is None else logo,
        "style": "for-the-badge" if style is None else style
    }
    return "https://img.shields.io/static/v1?" + urlencode(params)
