#9.1 Unit converter:
print ("Hello user, lets convert kilometers into miles:")
miles = 0.621371
while True:
    km = int(input("Please enter kilometers: "))
    print(km * miles)
    Yes = input("Do you want to do another conversion? Enter y for YES, n for NO: ")
    if Yes != "y":
        break
print("Thank You and Goodbye!")
#9.2 FIZZ BUZZ -- TOO MANY QUESTIONS :D

#9.3 String lowercase:
sentence = input("Please enter a sentence: ")
print(sentence.lower())

