import csv
import easygui

# Пишем функции не выходя


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