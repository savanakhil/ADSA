'''Type Checking: To check the value of particular type()'''
# a = 10
# b = 10.5
# c = "Hello"
# d = [1,2,3]
# e = (1,2,3)
# f = {1,2,3}
# g = {"name":"Akhil","age":20}
# print(type(a))
# print(type(b))
# print(type(c))
# print(type(d))
# print(type(e))
# print(type(f))
# print(type(g))

'''
isinstance():to check the value() object is belongs to particular class or datatype
Syntax:
isinstance(object, type)
'''
# a = 10
# b = 10.5
# c = "Hello"
# d = [1,2,3]
# e = (1,2,3)
# f = {1,2,3}
# g = {"name":"Akhil","age":20}
# print(isinstance(a,int))
# print(isinstance(b,float))
# print(isinstance(c,str))
# print(isinstance(d,list))
# print(isinstance(e,set))
# print(isinstance(f,tuple))
# print(isinstance(g,dict))

'''Duck Typing: same method acts as as same behaviour, we can use it''' 
class Dog:
    def sound(self):
        print("Bow - Bow")
class Cat:
    def sound(self):
        print("Meow - Meow")


def make_sound(animal):
    animal.sound()
d = Dog()
c = Cat()
make_sound(d)
make_sound(c)

def process(data):
    if isinstance(data, int):
        return data * 2
    elif isinstance(data, str):
        return data.upper()
    elif isinstance(data, list):
        return data * 10.5 
print(process(10))
print(process("Kalyani"))


class A:
    pass 
class B(A):
    pass
obj = B()
print(type(obj) == B)
print(type(obj) == A)

print(isinstance(obj, B))
print(isinstance(obj, A))