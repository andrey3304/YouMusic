from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog
from data.models import init_db
from data.classe_1 import Music
from data.classe_2 import ProfileChangeLabel, Duration


class MyWidget(QMainWindow, Music, ProfileChangeLabel, Duration):
    def __init__(self):
        super().__init__()
        self.thr_first = ""
        self.path_to_mp3file = ""

        # Инициализация базы данных
        init_db()

        print("Check successful:")
        self.button_main_run()

    # функция запуска главного окна;
    def button_main_run(self):
        uic.loadUi('./forms/MainWindow.ui', self)
        self.button_play_main.clicked.connect(self.button_play_main_run)
        self.button_profile.clicked.connect(self.button_profile_run)
        self.button_pause_main.clicked.connect(self.button_pause_main_run)
        self.button_open_file.clicked.connect(self.button_open_file_run)
        print("-> Main - ok")

    # Функция запуска профильного окна;
    def button_profile_run(self):
        uic.loadUi('./forms/ProfileWindow.ui', self)
        self.button_profile_back.clicked.connect(self.button_main_run)

        # Получаем статистику из базы данных вместо txt файлов
        try:
            from data.models import get_session, UserStats
            session = get_session()
            user_stats = session.query(UserStats).first()
            session.close()

            if user_stats:
                # Устанавливаем количество прослушанных песен
                self.label_num_of_song.setText(str(user_stats.total_songs_played))

                # Форматируем и устанавливаем общее время прослушивания
                total_seconds = user_stats.total_listening_time
                text_hour = total_seconds // 3600
                text_minut = (total_seconds % 3600) // 60

                # Используем вашу существующую логику форматирования
                if text_hour != 0:
                    if text_hour == 1 and text_minut == 1:
                        self.label_duration_file.setText(f"{text_hour} час {text_minut} минута")
                    elif text_hour == 1 and text_minut in [2, 3, 4]:
                        self.label_duration_file.setText(f"{text_hour} час {text_minut} минуты")
                    elif text_hour == 1 and 4 < text_minut < 60:
                        self.label_duration_file.setText(f"{text_hour} час {text_minut} минут")
                elif 1 < text_hour < 5:
                    if text_minut == 1:
                        self.label_duration_file.setText(f"{text_hour} часа {text_minut} минута")
                    elif text_minut in [2, 3, 4]:
                        self.label_duration_file.setText(f"{text_hour} часа {text_minut} минуты")
                    elif 4 < text_minut < 60:
                        self.label_duration_file.setText(f"{text_hour} часа {text_minut} минут")
                elif 4 < text_hour:
                    if text_minut == 1:
                        self.label_duration_file.setText(f"{text_hour} часов {text_minut} минута")
                    elif text_minut in [2, 3, 4]:
                        self.label_duration_file.setText(f"{text_hour} часов {text_minut} минуты")
                    elif 4 < text_minut < 60:
                        self.label_duration_file.setText(f"{text_hour} часов {text_minut} минут")
                else:
                    if text_minut == 1:
                        self.label_duration_file.setText(f"{text_minut} минута")
                    elif text_minut in [2, 3, 4]:
                        self.label_duration_file.setText(f"{text_minut} минуты")
                    elif 4 < text_minut < 60:
                        self.label_duration_file.setText(f"{text_minut} минут")
            else:
                self.label_num_of_song.setText("0")
                self.label_duration_file.setText("0 минут")

        except Exception as e:
            print(f"Ошибка загрузки статистики: {e}")
            self.label_num_of_song.setText("0")
            self.label_duration_file.setText("0 минут")

        print("-> Profile - ok")

    # Функция запуска рандомной песни;
    def button_play_main_run(self):
        self.random_sounds()

    # Функция остановки мелодии;
    def button_pause_main_run(self):
        self.play_stop_sound(stp=True)

    # Функция запуска открытия файла;
    def button_open_file_run(self):
        self.save_num_of_song_txt()
        fname, ftype = QFileDialog.getOpenFileName(
            self,
            "Выбери музыкальный файл mp3/wav",
            "",
            "Файл (*.mp3);;Файл (*.wav)"
        )
        try:
            self.dur_song(fname)
            self.play_stop_sound(music=fname)
        except Exception as e:
            print(f"Ошибка открытия файла: {e}")
