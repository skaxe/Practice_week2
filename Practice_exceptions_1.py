def Hello_user():
    while True:
        try:
            user_say = input('Как дела?').lower()

            if user_say == 'хорошо':
                print('Отличного дня!')
            else:
                print('Скажи "Хорошо", тогда я прекращу')
        except KeyboardInterrupt:
            print('Пока!')
            break
Hello_user()
