import sys
from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QApplication

from data.classes import MyWidget


# обработчик ошибок;
def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


# запуск приложения;
if __name__ == '__main__':
    sys.excepthook = except_hook
    # Проверка на наличие уст-в с высоким разрешением:
    if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
    if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
        QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
    # Стандартный запуск приложения:
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())
