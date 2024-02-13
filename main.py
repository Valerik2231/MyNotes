def show_notes():
    try:
        with open('notes.txt', 'r') as file:
            notes = file.readlines()
            print("\nВаши заметки:")
            for number, note in enumerate(notes, start=1):
                print(f"{number}. {note.strip()}")
    except FileNotFoundError:
        print("Файл заметок не найден. Будет создан новый файл.")

def add_note():
    note = input("Введите заметку: ")
    with open('notes.txt', 'a') as file:
        file.write(note + '\n')
    print("Заметка добавлена.")

def delete_note():
    show_notes()
    try:
        note_number = int(input("Введите номер заметки для удаления: "))
        with open('notes.txt', 'r') as file:
            notes = file.readlines()

        if note_number <= len(notes) and note_number > 0:
            del notes[note_number - 1]
            with open('notes.txt', 'w') as file:
                file.writelines(notes)
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