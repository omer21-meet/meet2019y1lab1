name = input("Whats your name?")
print("Hello " + name)
age = (input("Whats your age " + name))
live = input("Where do u live?")
print(live + " is a nice place!")
team = input("Whats your favorite soccer team?")
print("I dont like them that much...")

num = input("Choose a number between 0 to 1000 and i will try to guess it!")
num2 = 985
if num == num2:
    print("is your number 985?")
else:
    print("Hmm let me think...")
    num3 = input("Can u write your number again?") 
    answer = input("Is your number " + num3 + "?")
    if answer != "no" or "nope" or "nah" or "nop":
        print("Yay!, thanks for playing!")

