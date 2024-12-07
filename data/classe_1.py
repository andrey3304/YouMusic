from audioplayer import AudioPlayer
from random import choice

from data.functions import translate_ru


class Music:
    def __init__(self):
        self.last_sound = ""
        self.random_music_list = ["u-menya-takie-gory", "lesnic", "aleschka"]

        self.music_dict = {"u-menya-takie-gory": "sounds/u-menya-takie-gory.mp3",
                           "lesnic": "sounds/lesnic.mp3",
                           "aleschka": "sounds/aleschka.mp3"}

    # Главная функция запуска и остановки играющей песни;
    def play_stop_sound(self, stp=False, music=False):
        try:
            if stp:
                self.music_player.close()
                self.label_name_music_volna.setText(f"Название песни")
                print("Exit from sound")
            self.music_player = AudioPlayer(music)
            self.music_player.play(loop=True, block=False)
            self.label_name_music_volna.setText(f"Название: {translate_ru(text=music)[7:-4].capitalize()}")
            self.label_path_file.setText(music)
        except Exception:
            print("Все зашибись, так и должно быть")

    # Функция, которая запускает случайную скаченную мелодию;
    def random_sounds(self):
        name_sound = self.music_dict[choice(self.random_music_list)]
        if self.last_sound == name_sound:
            print("Одинаковая песня")
            self.random_sounds()
        else:
            self.last_sound = name_sound
            self.play_stop_sound(music=name_sound)
            print(name_sound)
