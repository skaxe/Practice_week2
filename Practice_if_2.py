a ='aaaa'
if type(a) == int:
    print('dastroka')
else:
    print('net')
def string_qualifier(string1, string2):
    if type(string1) != str  or type(string2) != str:#условие на строку:
        return 0      
    elif string1 == string2:
        return 1
    elif  string1 != string2 and len(string1) > len(string2):
        return 2
    
    elif string2 =='learn' and string1 != string2:
        return 3
string1 = 'learn'
string2 = 'learn'

result = string_qualifier(string1, string2)
print(result)

        
    
    
