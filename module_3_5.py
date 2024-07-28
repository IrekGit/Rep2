# Основной задачей будет отделение первой цифры в числе: создайте переменную first
# и запишите в неё первый символ из str_number в числовом представлении(int).
# Возвращайте значение first * get_multiplied_digits(int(str_number[1:])).
# Таким образом вы умножите первую цифру числа на результат работы этой же функции с числом, но уже без первой цифры.
# 4 пункт можно выполнить только тогда, когда длина str_number больше 1,
# т.к. в противном случае не получиться взять срез str_number[1:].
# Если же длина str_number не больше 1, тогда вернуть оставшуюся цифру first
def get_multiplied_digits(number):
    str_number = str(number)
    first = int(str_number[0])
    str_number = str_number[1:]
    if len(str_number) != 0:
        return first * get_multiplied_digits(int(str_number))
    else:
        return first


input_number = int(input('Введите число, произведение цифр которого хотите получить: '))
multiplication_number = get_multiplied_digits(input_number)
print(f'Получите результат (нули в расчете не учитываются): {multiplication_number}')