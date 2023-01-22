from random import random


def random_color_gen() -> str:
    """
    Generate a random color.

    :return: a random color
    """
    random_solid_color = lambda: int(random() * 256)
    return f"#{random_solid_color():02x}{random_solid_color():02x}{random_solid_color():02x}"


def random_color_gen_v2():
    """
    Generate a random color.

    :return: a random color
    """
    random_solid_color = ["f44336", "e91e63", "9c27b0", "673ab7", "3f51b5", "2196f3", "03a9f4", "00bcd4", "009688",
                          "4caf50", "8bc34a", "cddc39", "ffeb3b", "ffc107", "ff9800", "ff5722", "795548", "9e9e9e",
                          "607d8b", "000000", "ffffff", "f48fb1", "f06292", "e91e63", "d81b60", "c2185b", "ad1457",
                          "880e4f", "ff80ab", "ff4081", "f50057", "c51162", "e1bee7", "ce93d8", "ba68c8", "ab47bc",
                          "9c27b0", "8e24aa", "7b1fa2", "6a1b9a", "4a148c", "5e35b1", "3949ab", "303f9f", "283593",
                          "1a237e"]
    return random_solid_color[random.randint(0, len(random_solid_color) - 1)]
