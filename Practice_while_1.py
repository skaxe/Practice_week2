
def Hello_user():
    while True:
        user_say = input('Как дела? ').lower()
        
        if user_say == 'хорошо':
            print('Отличного дня!')
            break
        else:
            print('Скажи "Хорошо", тогда я прекращу')
Hello_user()
    