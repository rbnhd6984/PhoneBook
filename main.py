import csv
import easygui


# Пишем функции не выходя

# Функция для редактирования записи в телефонном справочнике
def edit_entry():
    name = easygui.enterbox("Введите имя:").lower()
    with open('phonebook.csv', 'r') as f:
        reader = csv.reader(f)
        rows = list(reader)
    found = False
    for row in rows:
        if row[0] == name:
            phone = easygui.enterbox(f"Введите новый номер телефона для {name}:")
            row[1] = phone
            found = True
            break
    if found:
        with open('phonebook.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(rows)
        easygui.msgbox(f"Запись {name}: {phone} изменена в телефонном справочнике.")
    else:
        easygui.msgbox(f"Запись {name} не найдена в телефонном справочнике.")


# За пределы этих комментов

# Основной цикл программы
while True:
    # Отображаем пользователю меню с возможными действиями
    choice = easygui.buttonbox("Выберите действие:",
                               choices=["Добавить запись",
                                        "Удалить запись",
                                        "Редактировать запись",
                                        "Найти запись",
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
