def rgb_to_hex(rgb):
    """Receives (r, g, b)  tuple, checks if each rgb int is within RGB
    boundaries (0, 255) and returns its converted hex, for example:
    Silver: input tuple = (192,192,192) -> output hex str = #C0C0C0"""
    if not isinstance(rgb, tuple) or len(rgb) != 3:
        raise ValueError("The input must be a tuple of 3 integers")

    for ele in rgb:
        if isinstance(ele, int) and (ele >= 0 and ele <= 255):
            return f"#{rgb[0]:02x}{rgb[1]:02x}{rgb[2]:02x}".upper()
        else:
            raise ValueError(
                "The input must be a tuple of 3 integers in a valid range (0,255)"
            )
