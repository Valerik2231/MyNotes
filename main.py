import json

def load_notes():
    try:
        with open('notes.json', 'r', encoding='utf8') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_notes(notes):
    with open('notes.json', 'w', encoding='utf8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)

def show_notes():
    notes = load_notes()
    if not notes:
        print("Нет сохраненных заметок.")
    else:
        print("\nВаши заметки:")
        for idx, note in enumerate(notes, start=1):
            print(f"{idx}. Заголовок: {note['title']}, Текст: {note['body']}")

def add_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    notes = load_notes()
    notes.append({'title': title, 'body': body})
    save_notes(notes)
    print("Заметка добавлена.")

def delete_note():
    notes = load_notes()
    show_notes()
    try:
        note_number = int(input("Введите номер заметки для удаления: "))
        if 0 < note_number <= len(notes):
            del notes[note_number - 1]
            save_notes(notes)
            print("Заметка удалена.")
        else:
            print("Неверный номер заметки.")
    except ValueError:
        print("Пожалуйста, введите число.")

def main():
    while True:
        print("\nПриложение Заметки")
        print("1. Показать все заметки")
        print("2. Добавить заметку")
        print("3. Удалить заметку")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            show_notes()
        elif choice == '2':
            add_note()
        elif choice == '3':
            delete_note()
        elif choice == '4':
            print("Выход из приложения...")
            break
        else:
            print("Неверный выбор. Пожалуйста, выберите один из предложенных вариантов.")

if __name__ == "__main__":
    main()
