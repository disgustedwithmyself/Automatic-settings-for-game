import os
import subprocess

games_dir = "C:\\Program Files (x86)\\Steam"

def get_games_list():
    games_list = []
    for dirpath, dirnames, filenames in os.walk(games_dir):
        for filename in filenames:
            if filename.endswith(".exe"):
                game_path = os.path.join(dirpath, filename)
                games_list.append(game_path)
    return games_list

def choose_game():
    games_list = get_games_list()
    for i, game_path in enumerate(games_list):
        print(f"{i+1}. {game_path}")
    while True:
        game_index = input("Выберите игру (введите номер): ")
        try:
            game_index = int(game_index)
            if game_index < 1 or game_index > len(games_list):
                print("Ошибка: введите корректный номер игры.")
            else:
                return games_list[game_index-1]
        except ValueError:
            print("Ошибка: введите корректный номер игры.")

def set_game_settings(game_exe_path, game_settings):
    for key, value in game_settings.items():

        cmd = f'"{game_exe_path}" --set-{key}={value}'

        subprocess.run(cmd, shell=True)

if __name__ == "__main__":
    game_exe_path = choose_game()

    game_settings = {
        "resolution": (1920, 1080),
        "graphics_quality": "high",
        "anti_aliasing": "off",
        "shadows": "off",
        "texture_quality": "high",
        "ambient_occlusion": "off",
        "motion_blur": "off",
        "depth_of_field": "off",
        "v_sync": "off",
    }

    set_game_settings(game_exe_path, game_settings)

    print("Настройки игры были успешно изменены!")
