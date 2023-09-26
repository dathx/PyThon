print(1/2)
print(type("1.9"))
print("Hello {}".format("Đạt"))
print('{1},{0}'.format("A",'B'))
print("{a},{b}".format(a="a",b="b"))
print("Rs: {:1.2f}".format(102.123))
name = "Đạt"
print(f"Hello {name}")

strc='rules!'
print("Python {}".format(strc))


my_dic = {'key1': "value1", "key2":[2,2,4]}
print(my_dic["key1"])
print(my_dic['key2'])

my_dic['key3']="value3"
print(my_dic)
print(my_dic.keys())
print(my_dic.values())

my_dic1={"key1":"value1", 'key2':[1,2,3]}
print(my_dic1)

my_list = [3,2,3,3,4,1,3]
print(set(my_list))