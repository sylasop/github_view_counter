import requests
from flask import make_response, Response

from src.controller.view_controller import ViewsCounter
from src.helpers.get_svg_url import get_svg_url
from src.models.args_model import args_model_from_dict


def view_url(arguments: dict = None):
    """
    View function for root route management. Increase the number of views, generate the URL for the SVG picture,
    and return the SVG image in the response.

    :return: the SVG image of the view counter
    """
    arguments = args_model_from_dict(arguments)
    """
    {
  "label": "",
  "message": "",
  "labelColor":"",
  "backgroundColor": "",
  "logoSpacing": null,
  "logo": "",
  "style": ""}
    """
    views_counter = ViewsCounter("views.json")
    try:
        views_counter.increment()
    except FileNotFoundError as e:
        # handle the error if the data file is not found
        return str(e), 500
    response = make_response("")
    response.headers["Expires"] = "Thu, 01 Dec 1994 16:00:00 GMT"
    response.headers["Last-Modified"] = "Thu, 01 Dec 1994 16:00:00 GMT"
    response.headers["Pragma"] = "no-cache"
    response.headers["Cache-Control"] = "no-cache, must-revalidate"
    response.headers["Content-type"] = "image/svg+xml"
    try:
        response.data = requests.get(get_svg_url(views_counter=views_counter, label_color=arguments.label_color,
                                                 color=arguments.background_color, logo_width=arguments.logo_spacing,
                                                 style=arguments.style, logo=arguments.logo,
                                                 label=arguments.label)).text
    except requests.exceptions.RequestException as e:
        # handle the error if the request to the SVG image URL fails
        return str(e), 500
    return response
