import os
import json
from utils.colours import colour_text

from scenes.intro    import scene as intro_scene
from scenes.forest   import scene as forest_scene
from scenes.castle   import scene as castle_scene
from scenes.snow     import scene as snow_scene
from scenes.timehill import scene as timehill_scene

SCENE_HANDLERS = {
    "intro":          intro_scene,
    "forest_start":   forest_scene,
    "castle_start":   castle_scene,
    "snow_start":     snow_scene,
    "timehill_start": timehill_scene,
}

SAVE_PATH = "data/save.json"

def load_game():
    if os.path.exists(SAVE_PATH):
        with open(SAVE_PATH, "r") as f:
            try:
                return json.load(f).get("scene", "intro")
            except json.JSONDecodeError:
                pass
    return "intro"

def save_game(scene_id):
    with open(SAVE_PATH, "w") as f:
        json.dump({"scene": scene_id}, f)

def play_game():
    current = load_game()
    while True:
        handler = SCENE_HANDLERS.get(current)
        if not handler:
            print(colour_text(f"Scene not found: {current}", "red"))
            break

        next_scene = handler()
        if not next_scene:
            print(colour_text("Thanks for playing — more coming soon!", "blue"))
            break

        save_game(next_scene)
        current = next_scene

if __name__ == "__main__":
    play_game()
