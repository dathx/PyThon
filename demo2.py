numbers = [1,2,3,4,5,6,7]
for num in numbers:
    print(num)

for strc in "Hello":
    print("Hello")

n = 0
while n< 5:
    print(n)
    n+=1;
else:
    print("ok")

for item in enumerate("Hello"):
    print(item)

print('a' in "Haha")

print(min(2,7,8,1))
print(max(2,3,4,7,2))

from random import randint
ran = randint(0,10)
print(ran)

# text = input("Input text here: ")
# print(text)

my_list = [num for num in range(0,10) if num % 2==0]
print(my_list)