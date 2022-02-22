#! /usr/bin/env python
#coding=utf8

import os
import re


def letter_replacer(word, dic):
    for key, value in dic.items():
        word = word.replace(key, value)
    return word

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



#def file_renamer(extension='dxf', dic=legend):
    #for filename in os.listdir('.'):
        #if filename[-4:].lower() == '.' + extension:
            #new_filename = letter_replacer(filename, dic)
            #if filename == new_filename:
                #print(f'{filename} не требует переименования')
            #else:
                #os.rename(filename, new_filename)
                #print(f'{filename} переименован в {new_filename}')



exception_patterns = {
    '\dх\d': ['х', 'x'],         # заменяем русскую х на латинскую "икс" в обозначениях размеров, например 200х200 (чтобы не получилось 200h200)
    'ф\d': ['ф', 'd']            # заменяем русскую ф на латинскую d в обозначениях диаметров, например ф30 (чтобы не получилось f300)
}

def file_renamer(extension='dxf', dic=legend, exception_patterns = None):
    for filename in os.listdir('.'):
        if filename[-4:].lower() == '.' + extension:
            old_filename = filename
            if exception_patterns != None:
                for key, value in exception_patterns.items():
                    search_key = re.search(key, old_filename)
                    if search_key:
                        replacement_part = search_key.group().replace(value[0], value[1])
                        old_filename = old_filename.replace(search_key.group(), replacement_part)
            new_filename = letter_replacer(old_filename, dic)
            if filename == new_filename:
                print(f'{filename} не требует переименования')
            else:
                os.rename(filename, new_filename)

file_renamer(exception_patterns=exception_patterns)