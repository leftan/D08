import random

def mimsmind0(len_digit = 1):
    num = random.randint(0, 10 ** len_digit - 1)
    count = 0
    print("Let's play the mimsmind0 game.")
    guess = int(input("Guess a {}-digit number: ".format(len_digit)))
    while True:
        count += 1
        if guess == num:
            print("Congratulations. You guessed the correct number in {} tries.".format(count))
            break
        elif guess < num:
            guess = int(input("Try again. Guess a higher number: "))
        else:
            guess = int(input("Try again. Guess a lower number: "))


def main():
    mimsmind0()

if __name__ == "__main__":
    main()
