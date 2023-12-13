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