from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QFileDialog

from data.classe_1 import Music
from data.classe_2 import ProfileChangeLabel, Duration


class MyWidget(QMainWindow, Music, ProfileChangeLabel, Duration):
    def __init__(self):
        super().__init__()
        self.thr_first = ""
        self.path_to_mp3file = ""  # ;
        print("Check successful:")
        self.button_main_run()  # запуск функция главного окна;

    # функция запуска главного окна;
    def button_main_run(self):
        uic.loadUi('./forms/MainWindow.ui', self)  # Загружаем главное окно;
        self.button_play_main.clicked.connect(self.button_play_main_run) # Сигнал для функции Случайная музыка;
        self.button_profile.clicked.connect(self.button_profile_run)  # Сигнал для включения профильного окна;
        self.button_pause_main.clicked.connect(self.button_pause_main_run)  # ;
        self.button_open_file.clicked.connect(self.button_open_file_run)  # ;
        print("-> Main - ok")

    # Функция запуска профильного окна;
    def button_profile_run(self):
        uic.loadUi('./forms/ProfileWindow.ui', self)  # ;
        self.button_profile_back.clicked.connect(self.button_main_run)  # ;


        # Открывает файл, чтобы добавить к счетчику количества прослушанных песен;
        fl_txt = open("./db/score.txt", mode="r+", encoding="utf-8")
        text = fl_txt.read()
        fl_txt.close()
        self.label_num_of_song.setText(text)

        # Открываем файл, чтобы добавить к счетчику время песни
        fl_txt = open("./db/duration.txt", mode="r+", encoding="utf-8")
        text = fl_txt.read()
        text_hour = 0
        text_minut = 0
        if int(text) // 3600 != 0:
            text_hour = int(text) // 3600
            text_minut = int(text) % 3600
        else:
            text_minut = int(text) // 60
        fl_txt.close()

        if text_hour != 0:
            if text_hour == 1 and text_minut == 1:
                self.label_duration_file.setText(f"{text_hour} час {text_minut} минута")
            elif text_hour == 1 and text_minut in [2, 3, 4]:
                self.label_duration_file.setText(f"{text_hour} час {text_minut} минуты")
            elif text_hour == 1 and 4 < text_minut < 60:
                self.label_duration_file.setText(f"{text_hour} час {text_minut} минут")
            else:
                pass
        elif 1 < text_hour < 5:
            if text_minut == 1:
                self.label_duration_file.setText(f"{text_hour} часа {text_minut} минута")
            elif text_minut in [2, 3, 4]:
                self.label_duration_file.setText(f"{text_hour} часа {text_minut} минуты")
            elif 4 < text_minut < 60:
                self.label_duration_file.setText(f"{text_hour} часа {text_minut} минут")
            else:
                pass
        elif 4 < text_hour:
            if text_minut == 1:
                self.label_duration_file.setText(f"{text_hour} часов {text_minut} минута")
            elif text_minut in [2, 3, 4]:
                self.label_duration_file.setText(f"{text_hour} часов {text_minut} минуты")
            elif 4 < text_minut < 60:
                self.label_duration_file.setText(f"{text_hour} часов {text_minut} минут")
            else:
                pass
        else:
            if text_minut == 1:
                self.label_duration_file.setText(f"{text_minut} минута")
            elif text_minut in [2, 3, 4]:
                self.label_duration_file.setText(f"{text_minut} минуты")
            elif 4 < text_minut < 60:
                self.label_duration_file.setText(f"{text_minut} минут")
            else:
                pass


        print("-> Profile - ok")

    # Функция запуска рандомной песни;
    def button_play_main_run(self):
        self.random_sounds()  # ;

    # Функция остановки мелодии;
    def button_pause_main_run(self):
        self.play_stop_sound(stp=True)

    # Функция запуска открытия файла;
    def button_open_file_run(self):
        self.save_num_of_song_txt()
        fname, ftype = QFileDialog.getOpenFileName(self,
                                                   "Выбери музыкальный файл mp3/wav",
                                                   "",
                                                   "Файл (*.mp3);;Файл (*.wav)")
        try:
            self.dur_song(fname)
            self.play_stop_sound(music=fname)
        except Exception:
            print("Плак-плак")
