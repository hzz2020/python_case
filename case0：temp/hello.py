from sys import argv, path

for i in argv:
    print('\n===', i)
print('path:', path)

print("hello\n3233")
print(r"hello\n3233")

a, b, c, d = 4, 5.5, True, 4 + 3j

print(type(a), type(b), type(c), type(d))

print(isinstance(a, int))
print(isinstance(b, int))

