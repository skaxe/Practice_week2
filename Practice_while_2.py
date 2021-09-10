Bot = {'Как дела': 'Хорошо', 'Что делаешь': 'Програмирую',
        'И как': 'Ну так' }  
def ask_user():#Ввести вопрос и ответь соответствующе
    answer = 'Спроси: "Как дела?" '
    while True:
       user_say = input(answer).lower().replace("?", "")
       if user_say == 'как дела':
           print(Bot['Как дела'])
           del Bot['Как дела']
           answer = 'Спроси: "Что делаешь?" '
       elif user_say == 'что делаешь':
           print(Bot['Что делаешь'])
           del Bot['Что делаешь']
           answer = 'Спроси: "И как?" '
       elif user_say == 'и как':
           print(Bot['И как'])
           del Bot['И как']
           break
       
           
           
ask_user()