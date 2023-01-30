# e-diary-db-change

Это библиотека скриптов для изменения школьных оценок на положительные в БД школы.

## Установка и подготовка

1. В качестве тренировочного манекена спользуется [веб-страницы школьного сайта](https://github.com/devmanorg/e-diary), которую нужно скачать и установить необходимые зависимости.
2. Скачать этот репозиторий и поместить файл `scripts.py` в корневую папку скачанной веб-страницы.

Опционально можно скачать [пример БД](https://dvmn.org/filer/canonical/1562234129/166/) и поместить с заменой в корневую папку скачанной веб-страницы.

## Использование

1. Запустить веб-страницу командой `python3 manage.py server`. Открыть её в браузе по ссылке http://127.0.0.1:8000/.
2. В отдельной командной строке запустить Django shell командой `python3 manage.py shell`.
3. В ней выполнить команду `from scripts import fix_marks, remove_chastisements, create_commendation`
4. Дальше выполнять в произвольном порядке скрипты: `fix_marks`, `remove_chastisements`, `create_commendation`

## Пример использования

Запуск веб-страницы:
```comandline
python3 manage.py server
```
Вывод:
```comandline
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 30, 2023 - 20:59:42
Django version 2.2.24, using settings 'project.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```

Запуск Django shell:
```comandline
python3 manage.py shell
```
Вывод:
```comandline
Python 3.10.6 (main, Nov 14 2022, 16:10:14) [GCC 11.3.0]
Type 'copyright', 'credits' or 'license' for more information
IPython 8.7.0 -- An enhanced Interactive Python. Type '?' for help.

In [1]: 
```

Выполнение ряда команд в Django shell:
```comandline
In [1]: from scripts import fix_marks, remove_chastisements, create_commendation

In [2]: fix_marks("Фролов Иван")

In [3]: remove_chastisements("Фролов Иван")

In [4]: create_commendation("Фролов Иван", "Математика")
```

### fix_marks

Скрипт меняет ученику все оценки ниже 4 на 5.  
На вход принимет 1 аргумент - имя ученика в формате `Фамилия Имя Отчество`. Имя может быть обрезано слева или справа.  
В случае успеха ничего не выводит.

### remove_chastisements

Скрипт удаляет все замечания ученика.  
На вход принимет 1 аргумент - имя ученика в формате `Фамилия Имя Отчество`. Имя может быть обрезано слева или справа.  
В случае успеха ничего не выводит.

### create_commendation

Скрипт создаёт запись с похвалой ученику по определённому предмету на случайное занятие.  
На вход принимет 2 аргумента: 
1. имя ученика (обязательный аргмент) - в формате `Фамилия Имя Отчество`, имя может быть обрезано слева или справа.
2. название предмета (необязательный аргумент) - если не указан, то выбирается случайный предмет.

В случае успеха ничего не выводит.

## Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).