import re

regex = re.compile(r'\d+')

def has_negatives(string):
    empty_string = ''
    
    for x in range(len(string)):
        if string[x] == '-' and string[x+1].isdecimal():
            empty_string += '-' + string[x+1] + ','
    
    return empty_string

def add(string):
    sum = 0
    numbers = regex.findall(string)
    negatives = has_negatives(string)
    
    try:
        string[:-1]
    except:
        raise "This is not ok!"
    if negatives:
        raise Exception("Negatives are not allowed: " + negatives)    
    
    if string == '':
        return 0
    else:
        for x in numbers:            
            if int(x) > 20:
                pass
            else:
                num = int(x)
                sum += num        
        return sum
print(add("1,2,3,4"))