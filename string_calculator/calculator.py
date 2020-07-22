import re

# regex = re.compile(r'\d+')

def has_negatives(string):
    empty_string = ''
    for number in range(len(string)):
        if string[number] == '-' and string[number+1]:
            empty_string += '-' + string[number+1] + ','
    return empty_string

def add(string):
    delimiter = ';'
    string_with_delimiters = '//{}\n1{}2'.format(delimiter,delimiter)

    negative = has_negatives(string)

    if string == '':
        return 0

    elif '-' in string:
        try:
            string[:-1]
        except:
            raise "This is not ok!"
        if negative:
            raise Exception("ERROR: Negatives are not allowed.")

    elif delimiter in string_with_delimiters:
        numbers = re.findall(r'[^//|{}|\n]'.format(delimiter), string_with_delimiters)
        total = sum([int(number) for number in numbers])
        return total

    elif '//' in string:
        delimiter = re.findall(r'\d+', string)
        total = sum([int(number) for number in delimiter])
        return total

    elif '\n' in string:
        new_string = re.split(r',|\n', string)
        total = sum([int(number) for number in new_string])
        return total

    elif ',' in string:
        total = sum([int(number) for number in string.split(',')])
        return total

    else:
        return int(string)

print(add("1,1"))

# def add(string):
#     sum = 0
#     numbers = regex.findall(string)
#     negative = has_negatives(string)
    
#     try:
#         string[:-1]
#     except:
#         raise "This is not ok!"
#     if negative:
#         raise Exception("Negatives are not allowed: " + negative)    
    
#     if string == '':
#         return 0
#     else:
#         for number in numbers:            
#             if int(number) > 20:
#                 pass
#             else:
#                 num = int(number)
#                 sum += num        
#         return sum

#     delimiter = ','
#     if string.startswith('//'):
#         delimiter = string[2]
#         string = string[3:]
#     string = string.replace('\n', ',')

# print(add("//[abc][777][:(]\n1abc27773:(1"))
# print(add("-1,-2"))
