
class1 = {'school_class': '7g', 'scores': [4,2,3,5]}    
def class_scores(class1):
    
    school_class = class1['school_class']
    scores = class1['scores']
    average_rating = sum(scores)/len(scores)
    return school_class, average_rating

#result = class_scores(class1)
#print(result)
school = [{'school_class': '4А', 'scores': [4,2,3,5]},
          {'school_class': '4Б', 'scores': [4,2,3,5]},
          {'school_class': '4В', 'scores': [4,2,3,5]},
          {'school_class': '4Г', 'scores': [4,2,3,5]}
    ]
school_average_rating = 0
class_number = 0
for school_class in school:    
    result = class_scores(school[class_number])
    print(f'Средняя оценка у {result[0]} класса: {result[1]}')
    school_average_rating += result[1]
    class_number += 1
    
print(f'Средняя оценка по школе: {school_average_rating}')   