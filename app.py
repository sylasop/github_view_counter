from flask import Flask, request, jsonify
from src.helpers.view_counter import view_url

app = Flask(__name__)


@app.route("/")
def views():
    """
    View function for root route management. Increase the number of views, generate the URL for the SVG picture,
    and return the SVG image in the response.

    :return: the SVG image of the view counter
The arguments are: label, message, labelColor, backgroundColor, logoSpacing, logo, style, hasLabel
In JSOn FORMAt:  {"label":"","message":"","labelColor":"","backgroundColor":"", logoSpacing":null,"logo":"","style":"", "hasLabel":null}
    """
    arguments = jsonify(request.args).json
    return view_url(arguments)


if __name__ == "__main__":
    app.run()
