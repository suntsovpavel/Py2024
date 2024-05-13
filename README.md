##Задание
Напишите код, который запускается из командной строки и получает на вход путь до директории на ПК.

Соберите информацию о содержимом в виде объектов namedtuple.

Каждый объект хранит:
○ имя файла без расширения или название каталога,
○ расширение, если это файл,
○ флаг каталога,
○ название родительского каталога.

В процессе сбора сохраните данные в текстовый файл используя логирование

##Пример вызова из командной строки
C:\Users\01\Documents\task_py> python main.py 'C:/Users/01/Documents/test_dir'
