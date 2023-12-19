import random


def get_a_random_word():
    """
    Функция для получения случайного слова из заранее созданного списка в 100 элементов
    """

    # Список из 100 слов на английском языке для расшифровки
    list_of_words_to_decipher = [
        "time", "year", "way", "day", "man", "government", "company", "part", "place", "case", "problem", "fact",
        "friend", "example", "life", "hand", "woman",
        "child", "world", "school", "state", "family", "business", "country", "question", "home", "job", "money",
        "father", "mother", "book", "food", "water",
        "room", "area", "number", "people", "table", "person", "group", "fact", "problem", "idea", "fact", "company",
        "system", "program", "question", "work",
        "government", "part", "place", "case", "question", "example", "life", "hand", "woman", "child", "world",
        "school", "state", "family", "business", "country",
        "question", "home", "job", "money", "father", "mother", "book", "food", "water", "room", "area", "number",
        "people", "table", "person", "group", "fact",
        "problem", "idea", "fact", "company", "system", "program", "question", "work", "government"
    ]
    random_word_ = (random.choice(list_of_words_to_decipher)).lower()
    return random_word_


def encrypt_the_word(random_word_):
    """
    Функция для шифрования полученного слова
    """

    # Словарь с буквами (латиница) и кода в азбуке Морзе (ключ - буква, значение - код Морзе)
    dictionary_code_morse = {
        "a": ".-", "b": "-...", "c": "-.-.", "d": "-..", "e": ".", "f": "..-.", "g": "--.", "h": "....", "i": "..",
        "j": ".---", "k": "-.-",
        "l": ".-..", "m": "--", "n": "-.", "o": "---", "p": ".--.", "q": "--.-", "r": ".-.", "s": "...", "t": "-",
        "u": "..-", "v": "...-",
        "w": ".--", "x": "-..-", "y": "-.--", "z": "--.."
    }

    encrypted_word_ = " ".join([dictionary_code_morse.get(list(random_word_)[i]) for _
                               in range(len(list(random_word_)))])
    return encrypted_word_


def print_statistics(answers_):
    """
    Функция для подведения статистики по вопросам и ответам
    """

    statistics = f"""
        Всего задачек: {len(answers_)}
        Отвечено верно: {sum(answers_)}
        Отвечено неверно: {len(answers_) - sum(answers_)}
        """
    return statistics


"""
Эта программа создана для тестирования знаний пользователя азбуки Морзе, умения расшифровать слова.
Основной блок программы, где реализуется всё.
"""
if __name__ == "__main__":
    # Создаём необходимые нам переменные
    answers = []

    # Начало программы, знакомство с пользователем и объяснение правил
    if input("Сегодня мы потренируемся расшифровывать морзянку. \n Напиши да, если хочешь начать: ").lower() == "да":
        user_name = input("Отличный выбор!\nДавай для начала познакомимся. Как тебя зовут? ")
        print(
            f"\n{user_name.capitalize()}, отлично! Я загадаю тебе 5 слов, и зашифрую их с помощью азбуки Морзе. "
            f"Тебе нужно будет расшифровать и написать загаданное слово.\nДавай начнём!")

        # Начинаем цикл со счётчиком в 5 раз, где будем создавать и шифровать слово, а пользователь будет отгадывать его
        for i in range(5):

            # Выбираем случайное слово и шифруем его
            random_word = get_a_random_word()
            encrypted_word = encrypt_the_word(random_word)
            print(f"\nЯ загадал слово № {i + 1}. Попробуй его расшифровать. Вот оно:\n{encrypted_word}")

            # Ввод пользователем слова        
            answer_user = input("Введи расшифрованное слово: ")

            # Условие для проверки является ли введённое слово зашифрованным и запись результата
            if answer_user.lower() == random_word:
                print("Молодец! Ты угадал!")
                answers.append(True)
            else:
                print(f"Ты не угадал... Загаданное слово {random_word}. Но не сдавайся! В следующий раз повезёт!")
                answers.append(False)

        # Вывод результата
        print(print_statistics(answers))
    else:
        print("Тогда до следующего раза! Удачи!")
