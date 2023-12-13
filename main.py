import csv
import easygui

# Функция поиска
def search_entry():
    name = easygui.enterbox("Введите имя для поиска:").lower()
    with open('pb.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
        found = False
        for row in rows:
            # Сравнение без учета регистра
            if row[0].lower() == name:
                easygui.msgbox(f"Найдена запись: Имя - {row[0]}, Телефон - {row[1]}")
                found = True
                break
        if not found:
            easygui.msgbox(f"Запись с именем {name} не найдена.")

# Пишем функции не выходя

# Функция для редактирования записи в телефонном справочнике
def edit_entry():
    name = easygui.enterbox("Введите имя:").lower()
    with open('pb.csv', 'r') as file:
        reader = csv.reader(file)
        rows = list(reader)
    found = False
    for row in rows:
        if row[0] == name:
            phone = easygui.enterbox(f"Введите новый номер телефона для {name}:")
            row[1] = phone
            found = True
            break
    if found:
        with open('pb.csv', 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(rows)
        easygui.msgbox(f"Запись {name}: {phone} изменена в телефонном справочнике.")
    else:
        easygui.msgbox(f"Запись {name} не найдена в телефонном справочнике.")


def add_entry():
    name = easygui.enterbox("Введите имя:").lower()
    phone = easygui.enterbox("Input phone number:")
    with open("pb.csv", "a", newline='') as file:
        writer = csv.writer(file)
        writer.writerows([name, phone])
    easygui.msgbox(f"Contact {name}: {phone} added")


def delete_entry():
    name = easygui.enterbox("Введите имя:").lower()
    with open("pb.csv", "r") as file:
        reader = csv.reader(file)
        rows = list(reader)
        found = False
        for row in rows:
            if row[0].lower() == name:
                rows.remove(row)
                found = True
                break
        if found:
            with open("pb.csv", "w", newline='') as file:
                writer = csv.writer(file)
                writer.writerows(rows)
                easygui.msgbox(f"Запись {name} удалена из телефонного справочника.")
        else:
            easygui.msgbox(f"Запись {name} не найдена в телефонном справочнике.")



# За пределы этих комментов

# Основной цикл программы
while True:
    # Отображаем пользователю меню с возможными действиями
    choice = easygui.buttonbox("Выберите действие:",
                               choices=["Добавить запись", "Удалить запись", "Редактировать запись", "Найти запись",
                                        "Выход"])

    # Выполняем выбранное действие
    if choice == "Добавить запись":
        add_entry()
    elif choice == "Удалить запись":
        delete_entry()
    elif choice == "Редактировать запись":
        edit_entry()
    elif choice == "Найти запись":
        search_entry()
    elif choice == "Выход":
        break
