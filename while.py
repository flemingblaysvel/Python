while True:
    print('Who are you?')
    name = input()
    if name != 'Arun':
       continue
    print('Hello, Arun. What is the password?')
    password = input()
    if password == 'kumar':
       break
print('Access granted.')