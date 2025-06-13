# scenes/castle.py

from utils.colours import colour_text

def scene():
    # Transitional narrative
    print(colour_text(
        "\nSophia and Bunny step out of the daisied field and see a looming town wall.\n"
        "Grey clouds dim the sky, and townspeople peer anxiously from behind shutters.\n"
        "Undeterred, Sophia tucks her pyjama trousers and marches forward.\n",
        "yellow"
    ))

    # Castle Land description
    print(colour_text(
        "\nThe massive Stone Wall Golem stands guard over the gate.\n"
        "Its eyes glow as it booms: \"Solve the four sums on my lock, and pass you may.\"\n",
        "yellow"
    ))

    # Placeholder for the arithmetic-lock puzzle
    print(colour_text(
        "[Number-lock puzzle coming soon…]\n"
        "There are 4 sums to solve (e.g., 37 - 28 = ?).\n"
        "Get each one right to open the gate!",
        "blue"
    ))

    return None
