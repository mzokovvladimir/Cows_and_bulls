"""
Гра «Бики та корови»
Це логічна гра, в ході якої гравець за кілька спроб повинен зрозуміти, що загадав суперник (це можуть бути числа,
символи, слова тощо). Після кожної спроби гравець виставляє «оцінку»: скільки букв/цифр/символів
вгадано без збігу з позиціями (тобто показує кількість «корів») і скільки вгадано точно, разом з
розташуванням (тобто показує кількість "биків").

Ідея
Згенерувати два різних числа.
Знайти кількість «корів» та «биків» у кожному числі.
За допомогою циклу for пройтися за кількістю:
3.1 Якщо цифра є у списку індексів «биків», то не чіпати цієї цифри.
3.2 Якщо цифра є у списку індексів корів, то поміняти рандомно цю цифру з іншої корів, якщо такі є
3.3 Якщо цифра не "корова" і не "бик", то рандомно згенерувати нову цифру.
Отримати два однакові числа."""
import random


def is_valid(number):
    """ Перевірка числа на унікальність. Усі 4 цифри числа мають бути різні """
    try:
        # Перекладаємо наше число до списку символів. Порівнюємо з безліччю (у безлічі немає символів, що повторюються)
        number_list = list(str(number))
        if len(set(number_list)) == 4:
            return True
        return False
    except:
        return False


def check(number_guess, number_computer):
    """ Знаходимо кількість корів і биків у числі """

    # індекси корів та биків
    n_c, n_b = [], []

    try:
        # переводимо наші числа до списку із символів
        number_guess_list = list(str(number_guess))
        number_computer_list = list(str(number_computer))

        # проходимося по числу
        for index in range(len(number_guess_list)):
            # якщо в різних числах в однакових індексах цифри рівні, то це бик
            if number_computer_list[index] == number_guess_list[index]:
                n_b.append(index)
            # якщо в числах є однакові цифри, але на різних місцях, то це корова
            elif number_guess_list[index] in number_computer_list:
                n_c.append(index)

        # повертаємо списки індексів корів та биків
        return n_c, n_b
    except:
        return n_c, n_b


def game(number_guess, n_c, n_b):
    """ Ф-я перескладання числа з наявних даних """

    # переводимо наше число до списку із символів
    number_guess_list = list(str(number_guess))

    # проходимося за списком number_guess_list
    for index in range(len(number_guess_list)):
        # якщо індексу цифри немає у списку індексів бугаїв, але є у списку корів
        if index not in n_b and index in n_c:
            # рандомним способом переставляємо
            index_random = n_c[random.randint(0, len(n_c)-1)]
            number_guess_list[index], number_guess_list[index_random] = number_guess_list[index_random], \
                                                                        number_guess_list[index]
        # якщо індексу цифри немає в жодному зі списків
        if index not in n_b and index not in n_c:
            number_guess_list[index] = str(random.randint(1, 9))
            while not is_valid(int(''.join(number_guess_list))):
                number_guess_list[index] = str(random.randint(1, 9))

    return int(''.join(number_guess_list))


# змінні
number_guess = 0  # загадане число
number_computer = 0  # число, яке потрібно відгадати
n = 0  # кіл-ть спроб
# списки
n_c = []
n_b = []
# генерируємо число, яке необхідно відгадати
while not is_valid(number_guess):
    number_guess = random.randint(1000, 9999)
# генеруємо число від якого наша програма відштовхуватиметься
while not is_valid(number_computer):
    number_computer = random.randint(1000, 9999)


# головний цикл, працює, поки не буде 4 бики, тобто два числа не будуть рівні між собою

# отримуємо списки індексів корів та биків
n_c, n_b = check(number_guess, number_computer)

while len(n_b) != 4:
    # перезберемо число з наявних даних
    number_guess = game(number_guess, n_c, n_b)

    # отримуємо списки індексів корів та биків
    n_c, n_b = check(number_guess, number_computer)
    n += 1
    print(f"Спроба: {n}; Число: {number_guess}; Число, яке необхідно відгадати: {number_computer}")

print(number_guess)
