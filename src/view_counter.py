import requests
from flask import make_response

from src.view_controller import ViewsCounter


def view_url():
    """
    View function for root route management. Increase the number of views, generate the URL for the SVG picture,
    and return the SVG image in the response.

    :return: the SVG image of the view counter
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
        response.data = requests.get(views_counter.get_svg_url()).text
    except requests.exceptions.RequestException as e:
        # handle the error if the request to the SVG image URL fails
        return str(e), 500
    return response
