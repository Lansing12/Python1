#HOMEWORK 7.1#
mood = input('What is your mood today?')
if mood == 'happy':
    print("It's great to see you happy!")
elif mood == "nervous":
    print('Take a deep breath 3 times')
elif mood == 'sad':
    print("What's wrong?")
elif mood == 'excited':
    print('Wow!! Nice!!')
elif mood == 'relaxed':
    print('Great!!!')
else:
    print("I don't recognize this mood")

#HOMEWORK 7.2#
secret = 55
guess = int(input('Guess a secret number'))
if guess == secret:
    print('Amazing, You are right!!!!!')
else:
     print('Sorry!!! Try next time!')

#HOMEWORK 7.3#
x= int(input('Please enter first number: '))
y = int(input('Please enter second number: '))
operation = input('Please, choose arithmetic operation: "+" "-" "*" or "/"')
if operation == '+':
    print(x + y)
elif operation == '-':
    print(x - y)
elif operation == '*':
    print(x * y)
elif operation == '/':
    print (x / y)
else:
    print('Chosen wrong arithmetic operation')
