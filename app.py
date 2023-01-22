from flask import Flask
from src.view_counter import view_url

app = Flask(__name__)


@app.route("/")
def views():
    """
    View function for root route management. Increase the number of views, generate the URL for the SVG picture,
    and return the SVG image in the response.

    :return: the SVG image of the view counter
    """
    return view_url()


if __name__ == "__main__":
    app.run()
