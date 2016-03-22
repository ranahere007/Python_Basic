print("Do you want store your word:" )
user = input("Enter 'S' to start: ")
store = list()

while user == 'S':
    one = input("Enter your word:")
    store.append(one)
    user = input("S to continue and type any for exit:")

print("Your stored words are:")
for words in store:
     print(words)
