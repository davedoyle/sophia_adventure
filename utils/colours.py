def colour_text(text, colour):
    colours = {
        "red": "\033[91m",
        "green": "\033[92m",
        "yellow": "\033[93m",
        "blue": "\033[94m",
        "reset": "\033[0m"
    }
    return f"{colours.get(colour, '')}{text}{colours['reset']}"
