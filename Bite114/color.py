import os
import sys
import urllib.request

# PREWORK (don't modify): import colors, save to temp file and import
tmp = os.getenv("TMP", "/tmp")
color_values_module = os.path.join(tmp, "color_values.py")
urllib.request.urlretrieve(
    "https://bites-data.s3.us-east-2.amazonaws.com/color_values.py", color_values_module
)
sys.path.append(tmp)

# should be importable now
from color_values import COLOR_NAMES  # noqa E402


class Color:
    """Color class.

    Takes the string of a color name and returns its RGB value.
    """

    def __init__(self, color):
        self.color = color
        if color.upper() in COLOR_NAMES:
            self.rgb = COLOR_NAMES.get(color.upper())
        else:
            self.rgb = None

    @staticmethod
    def hex2rgb(hex):
        """Class method that converts a hex value into an rgb one"""
        hex = hex.lstrip("#")
        if len(hex) != 6:
            raise ValueError
        return tuple(int(hex[i : i + 2], 16) for i in (0, 2, 4))

    @staticmethod
    def rgb2hex(rgb):
        """Class method that converts an rgb value into a hex one"""
        if type(rgb) != tuple:
            raise ValueError
        for ele in rgb:
            if ele not in range(0, 256):
                raise ValueError
        return "#%02x%02x%02x" % rgb

    def __repr__(self):
        """Returns the repl of the object"""
        return f"Color('{self.color}')"

    def __str__(self):
        """Returns the string value of the color object"""
        if self.rgb:
            return str(self.rgb)
        else:
            return "Unknown"
