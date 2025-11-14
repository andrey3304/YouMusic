from audioplayer import AudioPlayer
from random import choice
from data.functions import translate_ru
from data.models import get_session, UserStats, MusicFile
from datetime import datetime


class Music:
    def __init__(self):
        self.last_sound = ""
        self.random_music_list = ["bella_ciao", "gata_only", "si_ai"]
        self.music_dict = {
            "bella_ciao": "sounds/bella_ciao.mp3",
            "gata_only": "sounds/gata_only.mp3",
            "si_ai": "sounds/si_ai.mp3"
        }

    # Главная функция запуска и остановки играющей песни;
    def play_stop_sound(self, stp=False, music=False):
        try:
            if stp:
                self.music_player.close()
                self.label_name_music_volna.setText(f"Название песни")
                print("Exit from sound")
            else:
                self.music_player = AudioPlayer(music)
                self.music_player.play(loop=True, block=False)
                self.label_name_music_volna.setText(f"Название: {translate_ru(text=music)[7:-4].capitalize()}")
                self.label_path_file.setText(music)

                # Обновляем статистику в БД при воспроизведении
                self._update_play_stats(music)

        except Exception as e:
            print(f"Ошибка воспроизведения: {e}")

    def _update_play_stats(self, music_path):
        """Обновляет статистику прослушивания в базе данных"""
        try:
            session = get_session()

            # Находим или создаем запись о файле
            music_file = session.query(MusicFile).filter_by(file_path=music_path).first()
            if music_file:
                music_file.play_count += 1
                music_file.last_played = datetime.now()
            else:
                # Если файл не в базе, добавляем его
                import os
                file_name = os.path.basename(music_path)
                file_extension = os.path.splitext(music_path)[1].lower()

                music_file = MusicFile(
                    file_path=music_path,
                    file_name=file_name,
                    file_extension=file_extension,
                    play_count=1,
                    last_played=datetime.now()
                )
                session.add(music_file)

            # Обновляем общую статистику пользователя
            user_stats = session.query(UserStats).first()
            if user_stats:
                user_stats.total_songs_played += 1
                user_stats.updated_at = datetime.now()

            session.commit()
            session.close()

        except Exception as e:
            print(f"Ошибка обновления статистики: {e}")

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
