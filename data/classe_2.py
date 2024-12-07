from mutagen.mp3 import MP3


class ProfileChangeLabel:
    def __init__(self):
        pass

    # Функция добавления прослушанной песни к общему счетчику;
    def save_num_of_song_txt(self):
        fl_txt = open("./db/score.txt", mode="r+", encoding="utf-8")
        text = fl_txt.read()
        text_fin = ""
        for i in text:
            if i in "1234567890":
                text_fin += i
            else:
                pass

        fl_txt.seek(0)
        fl_txt.truncate(0)
        fl_txt.write(str(int(text_fin) + 1))
        fl_txt.close()


class Duration:
    def __init__(self):
        self.lenght_file = 0

    def dur_song(self, file):
        self.lenght_file = MP3(file).info.length
        fl_txt = open("./db/duration.txt", mode="r+", encoding="utf-8")
        text = fl_txt.read()
        fin_lenght_file = self.lenght_file + int(text)

        fl_txt.seek(0)
        fl_txt.truncate(0)
        fl_txt.write(str(int(fin_lenght_file) + 1))
        fl_txt.close()
