# Функция для перевода названия из английских символов в русские;
def translate_ru(text) -> str:
    trans_end = {'a': 'а', 'b': 'б', 'v': 'в', 'g': 'г', 'd': 'д', "-": " ",
                 'e': 'е', 'yo': 'ё', 'zh': 'ж', 'z': 'з', 'i': 'и',
                 'y': 'ы', 'k': 'к', 'l': 'л', 'm': 'м', 'n': 'н',
                 'o': 'о', 'p': 'п', 'r': 'р', 's': 'с', 't': 'т',
                 'u': 'у', 'f': 'ф', 'kh': 'х', 'ts': 'ц', 'ch': 'ч',
                 'sh': 'ш', 'sch': 'щ', 'yu': 'ю', 'ya': 'я', "c": "к"}

    text = text.lower()
    for eng, rus in trans_end.items():
        text = text.replace(eng, rus)
    if "ыа" in text:
        ind = text.find("ыа")
        text = text[:ind] + "я" + text[ind + 2:]
    if "сч" in text:
        ind = text.find("сч")
        text = text[:ind] + "ш" + text[ind + 2:]
    return text
