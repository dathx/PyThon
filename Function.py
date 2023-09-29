def my_function():
    print("In my_function()")

param = "Daaa"
def function_2(param = 'Default'):
    print(f'Hello {param}')

def add_two_num(num1, num2):
    return num1+num2;

def get_even_num_in_list(list):
    new_list = []
    for num in list:
        if(num%2==0):
            new_list.append(num)
    return new_list

def check_1(work_hour):
    for name,hour in work_hour:
        print(name)

my_function()
function_2()  # default
function_2(param) #with param

total = add_two_num(2,3)
print(total)

list = [1,2,4,5,7,8]
print(get_even_num_in_list(list))

work_hour = [("Dat",10),("B",11), ("C",2)]
check_1(work_hour)
