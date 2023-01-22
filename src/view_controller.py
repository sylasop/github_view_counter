import json
import os
import requests
from datetime import datetime
from urllib.parse import urlencode

from flask import Flask, make_response


class ViewsCounter:
    def __init__(self, filename):
        """
        Class responsible for handling the logic for incrementing the view count, reading and writing data to a file,
        and creating the SVG image URL.

        :param filename: the filename in which the view count data is saved.
        """
        self.filename = filename
        self._create_file_if_not_exist()
        self.data = self._get_data_from_file()

    def _create_file_if_not_exist(self):
        """
        If the data file does not exist, create it.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"hit": 0, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, f)

    def _get_data_from_file(self):
        """
        Retrieve the data from the file.

        :return: the view count data
        :raises FileNotFoundError: if the data file does not exist
        """
        try:
            with open(self.filename, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            raise FileNotFoundError(f"Data file not found: {self.filename}")

    def increment(self):
        """
        Increment the view count and update the date.
        """
        self.data["hit"] += 1
        self.data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "w") as f:
            json.dump(self.data, f)

    @staticmethod
    def short_number(n):
        """
        Reduce a significant number by utilizing the SI prefixes (k, M, B, T).

        :param n: the number to shorten
        :return: the shortened number
        """
        if n < 1000:
            return str(n)
        prefixes = {3: 'k', 6: 'M', 9: 'B', 12: 'T'}
        for i in prefixes:
            if n < 10 ** (i + 3):
                return f"{n / 10 ** i:.1f}{prefixes[i]}"
        return str(n)

    def get_svg_url(self):
        """
        Generate the URL for the SVG image of the view counter.

        :return: the SVG image URL
        """
        params = {
            "label": "Views",
            "logo": "github",
            "message": ViewsCounter.short_number(self.data["hit"]),
            "color": "purple",
            "style": "for-the-badge"
        }
        return "https://img.shields.io/static/v1?" + urlencode(params)
