Bot = {'Как дела': 'Хорошо', 'Что делаешь': 'Програмирую',
        'И как': 'Ну так' }  
def ask_user():#Ввести вопрос и ответь соответствующе
    #answer = 'Спроси: "Как дела?" '
    while True:
        answer = input('Можно спросить: Как дела, Что делаешь, И как.\n ').lower().replace("?", "")
        if Bot.get(answer.capitalize()) == None:
            print('Введите другой вопрос')
        else:
            print(Bot.get(answer.capitalize()))
          
           
ask_user()