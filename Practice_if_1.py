age = int(input('Введите ваш возраст: '))
print(f"Ваш возраст: {age}")


def life_period(age):
    if age < 2:
        return 'Вы еще малы для садика'
    elif  2 <= age < 7:
        return 'Вы должны ходить в детский садик'
    elif  7 <= age < 18:
        return 'Вы должны ходить в школу'
    elif  18 <= age < 23:
        return 'Вы должны ходить в ВУЗ'
    else:
        return 'Вы должны работать до 65 лет'
my_age = life_period(age)
print(my_age)
    

        