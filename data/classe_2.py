from mutagen.mp3 import MP3
from data.models import get_session, UserStats, MusicFile
from datetime import datetime

import os


class ProfileChangeLabel:
    def __init__(self):
        pass

    # Функция добавления прослушанной песни к общему счетчику;
    def save_num_of_song_txt(self):
        """Теперь сохраняет в базу данных вместо txt файла"""
        try:
            session = get_session()
            user_stats = session.query(UserStats).first()

            if user_stats:
                user_stats.total_songs_played += 1
                user_stats.updated_at = datetime.now()
                session.commit()

            session.close()
        except Exception as e:
            print(f"Ошибка при сохранении статистики: {e}")


class Duration:
    def __init__(self):
        self.lenght_file = 0

    def dur_song(self, file):
        """Сохраняет длительность в базу данных"""
        try:
            self.lenght_file = MP3(file).info.length

            session = get_session()

            # Обновляем общее время прослушивания
            user_stats = session.query(UserStats).first()
            if user_stats:
                user_stats.total_listening_time += int(self.lenght_file)
                user_stats.updated_at = datetime.now()

            # Обновляем или создаем запись о файле
            music_file = session.query(MusicFile).filter_by(file_path=file).first()
            if music_file:
                music_file.duration = int(self.lenght_file)
            else:
                file_name = os.path.basename(file)
                file_extension = os.path.splitext(file)[1].lower()

                music_file = MusicFile(
                    file_path=file,
                    file_name=file_name,
                    file_extension=file_extension,
                    duration=int(self.lenght_file)
                )
                session.add(music_file)

            session.commit()
            session.close()

        except Exception as e:
            print(f"Ошибка при сохранении длительности: {e}")
