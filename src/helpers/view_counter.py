import datetime

import requests
from flask import make_response

from src.controller.view_controller import ViewsCounter
from src.utils.get_svg_url import get_svg_url
from src.helpers.validators.validate_username import validate_username
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
  "username": "test",
  "labelColor":"",
  "backgroundColor": "",
  "logoSpacing": null,
  "logo": "",
  "style": "",
  "hasLabel": null
  }
    """
    print(arguments)
    views_counter = ViewsCounter("views.json", arguments.username)
    try:
        if validate_username(arguments.username):
            views_counter.increment()
        else:
            return "Invalid username", 400
    except FileNotFoundError as e:
        # handle the error if the data file is not found
        return str(e), 500
    response = make_response("")
    response.headers["Expires"] = "0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Content-type"] = "image/svg+xml"
    try:
        cache_buster = datetime.datetime.timestamp(datetime.datetime.now())
        response.data = requests.get(get_svg_url(views_counter=views_counter, label_color=arguments.label_color,
                                                 color=arguments.background_color, logo_width=arguments.logo_spacing,
                                                 style=arguments.style, logo=arguments.logo,
                                                 label=arguments.label if not None else "", message=arguments.message,
                                                 has_label=arguments.has_label if arguments.has_label is not None else "true",
                                                 logo_color=arguments.logo_color, cache_buster=cache_buster)).text
    except requests.exceptions.RequestException as e:
        # handle the error if the request to the SVG image URL fails
        return str(e), 500
    return response
