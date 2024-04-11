'''
Реализовать консольное приложение заметки, с сохранением, чтением,
добавлением, редактированием и удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через
точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы
(команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.
'''

from random import *
import os
from datetime import datetime
import json
notes_book = []
def save():
    with open("notes_book.json", "w", encoding="utf-8") as fh:
        fh.write(json.dumps(notes_book, ensure_ascii=False))
    print("заметка сохранена")

def load():
    global notes_book
    if os.path.exists('notes_book.json'):
        with open("notes_book.json", "r", encoding="utf-8") as fh:
            notes_book= json.load(fh)
        print("заметки загружены")

        return notes_book

def delete():
    try:
        note_id = int(input("Введите идентификатор заметки, которую хотите удалить: "))
        for note in notes_book:
            if note["id"] == note_id:
                notes_book.remove(note)
                save()
                print("Заметка удалена")
    except:
        print("Такой заметки не существует")
        
def change():
    try:
        note_id = int(input("Введите идентификатор заметки, которую хотите редактировать: "))
        for note in notes_book:
            if note["id"] == note_id:
                title = input("Введите новое значение заголовка заметки: ")
                description = input("Введите новое  значение тела заметки: ")
                note["title"] = title
                note["body"] = description
                note["date"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                save()
                print("Заметка успешно отредактирована")

    except:
        print("Такой заметки не существует")
        
def show_note():
    note_id = int(input("Введите идентификатор заметки, которую хотите вывести: "))
    for note in notes_book:
        if note["id"] == note_id:
            print(note)


while True:
    print("/start - начало работы бота \n/load - загрузка данных из файла(внешнее хранилище)\n/all - показать все заметки\n/stop - прекращение работы бота\n/add - добавление новой заметки\n/delete - удаление заметки\n/save - сохранение контакта\n/change - изменение заметки\n/show - показать заметку")
    command = input("Введите команду: ")

    if command == "/add":
        title = input("Введите заголовок заметки: ")
        description = input("Введите текст заметки: ")
        note_id = len(notes_book) +1
        date =  datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        notes_book.append({"id":note_id, "title": title, "body": description, "date": date})
        '''notes_book = {"id":note_id, "title": title, "body": description, "date": date}'''
        save()
        print("добавлена заметка")

    elif command =="/start":
        print("Heey,это приложение заметок, здесь можно управлять своими заметками")
    elif command == "/all":
        print("Список всех заметок: ")
        print(notes_book)

    elif command == "/save":
        save()
        
    elif command == "/load":
        phone_book = load()
    elif command == "/stop":
        print("работа бота остановлена")
        break
    elif command == "/delete":
        delete()
    elif command == "/show":
        show_note()
    elif command == "/change":
        change()
