class String_cal:
    def __init__(self):
        pass

    def calculate_sum(self,first,second):
        try:
            return int(first) + int(second)
        except ValueError:
            return 0

add = String_cal()
add.calculate_sum("","")
first_number = ""
second_number = ""
sum = add.calculate_sum(first_number,second_number)

if sum == "":
    # print(calculate_sum(first_number,second_number))
    print("Conversion failed")
else:
    print(sum)

print(add.calculate_sum("",""))