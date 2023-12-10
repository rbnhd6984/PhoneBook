import csv
import easygui

# Пишем функции не выходя
def delete_entry():
    name_to_delete = easygui.enterbox("Введите имя для удаления:")
    if name_to_delete:
        # Ищем контакты с указанным именем
        matching_entries = [entry for entry in phonebook if entry["name"] == name_to_delete]

        if matching_entries:
            # Если найдены соответствующие контакты, удаляем первый из них
            phonebook.remove(matching_entries[0])
            easygui.msgbox(f"Контакт {name_to_delete} удален.")
        else:
            easygui.msgbox("Контакты с таким именем не найдены.")

def edit_entry():
    name_to_edit = easygui.enterbox("Введите имя для редактирования:")
    if name_to_edit:
        # Ищем контакты с указанным именем
        matching_entries = [entry for entry in phonebook if entry["name"] == name_to_edit]

        if matching_entries:
            # Если найдены соответствующие контакты, редактируем первый из них
            edited_name = easygui.enterbox("Введите новое имя:", default=matching_entries[0]["name"]) # насчет default очень не уверена, может что-то другое тут проставить
            edited_phone = easygui.enterbox("Введите новый номер телефона:", default=matching_entries[0]["phone"]) # насчет default очень не уверена, может что-то другое тут проставить

            if edited_name and edited_phone:
                matching_entries[0]["name"] = edited_name
                matching_entries[0]["phone"] = edited_phone
                easygui.msgbox("Контакт успешно отредактирован.")
            else:
                easygui.msgbox("Введены некорректные данные. Редактирование отменено.")
        else:
            easygui.msgbox("Контакты с таким именем не найдены.")
# За пределы этих комментов
phonebook = []  # Хранение контактов

def add_entry():
    name = easygui.enterbox("Введите имя:")
    if name:
        phone = easygui.enterbox("Введите номер телефона:")
        if phone:
            entry = {"name": name, "phone": phone}
            phonebook.append(entry)
            easygui.msgbox("Контакт успешно добавлен!")

def search_entry():
    name_to_search = easygui.enterbox("Введите имя для поиска:")
    if name_to_search:
        found_entries = [entry for entry in phonebook if entry["name"] == name_to_search]
        if found_entries:
            result = "\n".join([f"{entry['name']}: {entry['phone']}" for entry in found_entries])
            easygui.msgbox(f"Найденные контакты:\n{result}")
        else:
            easygui.msgbox("Контакты с таким именем не найдены.")
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