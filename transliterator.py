#! /usr/bin/env python
#coding=utf8

import os
import re

# словарь соответствий символов для замены
legend = {
    ' ':'_',
    ',':'',
    'а':'a',
    'б':'b',
    'в':'v',
    'г':'g',
    'д':'d',
    'е':'e',
    'ё':'yo',
    'ж':'zh',
    'з':'z',
    'и':'i',
    'й':'y',
    'к':'k',
    'л':'l',
    'м':'m',
    'н':'n',
    'о':'o',
    'п':'p',
    'р':'r',
    'с':'s',
    'т':'t',
    'у':'u',
    'ф':'f',
    'х':'h',
    'ц':'c',
    'ч':'ch',
    'ш':'sh',
    'щ':'shch',
    'ъ':'y',
    'ы':'y',
    'ь':"'",
    'э':'e',
    'ю':'yu',
    'я':'ya',
    'А':'A',
    'Б':'B',
    'В':'V',
    'Г':'G',
    'Д':'D',
    'Е':'E',
    'Ё':'Yo',
    'Ж':'Zh',
    'З':'Z',
    'И':'I',
    'Й':'Y',
    'К':'K',
    'Л':'L',
    'М':'M',
    'Н':'N',
    'О':'O',
    'П':'P',
    'Р':'R',
    'С':'S',
    'Т':'T',
    'У':'U',
    'Ф':'F',
    'Х':'H',
    'Ц':'Ts',
    'Ч':'Ch',
    'Ш':'Sh',
    'Щ':'Shch',
    'Ъ':'Y',
    'Ы':'Y',
    'Ь':"'",
    'Э':'E',
    'Ю':'Yu',
    'Я':'Ya'
    }

# словарь с исключениями, содержит паттерн и список ["исходынй_символ", "чем_заменить"]
exception_patterns = {
    '\dх\d': ['х', 'x'],         # заменяем русскую х на латинскую "икс" в обозначениях размеров, например 200х200 (чтобы не получилось 200h200)
    'ф\d': ['ф', 'd'],           # заменяем русскую ф на латинскую d в обозначениях диаметров, например ф30 (чтобы не получилось f300)
    'Н\d': ['Н', 'h']            # заменяем русскую Н на латинскую h в обозначениях высоты, например h30 (чтобы не получилось N300)
}


def letter_replacer(word, dic):
    '''
    Функция заменяет символы в строке (word) согласно словарю (dic)
    '''
    for key, value in dic.items():
        word = word.replace(key, value)
    return word


def file_renamer(extension='dxf', dic=legend, exception_patterns = None):
    '''
    Функция переименовывает файлы в текущей деректории.
    extension - расширение файла, по умолчанию 'dxf'
    dic - словарь соответствия символов для замены, по умолчанию legend
    exception_patterns - словарь исключений, по умолчанию None
    '''
    for filename in os.listdir('.'):
        if filename[-4:].lower() == '.' + extension.lower():                                       # проверяем расширение 
            old_filename = filename
            if exception_patterns != None:                                                         # если указан словарь исключений, сначала отрабатываем его
                for key, value in exception_patterns.items():
                    search_key = re.search(key, old_filename)
                    if search_key:                                                                 # если нашлись паттерны, меняем символы в паттернах
                        replacement_part = search_key.group().replace(value[0], value[1])
                        old_filename = old_filename.replace(search_key.group(), replacement_part)  # меняем найденный паттерн в имени файла
            new_filename = letter_replacer(old_filename, dic)                                      # новое имя для файла через словарь соответствия 
            if filename == new_filename:
                print(f'{filename} не требует переименования')
            else:
                os.rename(filename, new_filename)                                                  # переименовываем файл


# вызываем функцию переименования с нужными параметрами
file_renamer(exception_patterns=exception_patterns)