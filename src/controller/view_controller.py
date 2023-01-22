import json
import os
from datetime import datetime


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

    def _create_file_if_not_exist(self) -> None:
        """
        If the data file does not exist, create it.
        """
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({"hit": 0, "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}, f)

    def _get_data_from_file(self) -> dict:
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

    def increment(self) -> None:
        """
        Increment the view count and update the date.
        """
        self.data["hit"] += 1
        self.data["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(self.filename, "w") as f:
            json.dump(self.data, f)