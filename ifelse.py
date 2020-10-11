print('Hi!')
print('What is your name?')
name = input()
print('What is your age?')
age = int(input())
if age < 15:
    print('Hey '+name+',you are a child')
elif age < 30:
    print('Hey '+name+',you are an adult')
elif age < 50:
    print('Hey '+name+',you are a uncle')
else:
    print('Hey '+name+',you are an oldman')