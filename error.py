try:
    a=5
    b="python"
    c=a+b
except TypeError:
    print('TypeError Exception Raised')
else:
    print('success')

try:
    print(float('python'))
except ValueError:
    print('ValueError: could not convert string into float :\'Python\'')
else:
    print('success')

class Attributes(object):
    a=2
    print(a)
try:
    object = Attributes()
    print(object.attribute)
except AttributeError:
    print("Attribute Exception Raised.")
