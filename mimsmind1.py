import random

def str_to_tuple(s):
    '''s: str '''
    lst = []
    for n in range(len(s)):
        lst += [(s[n], len(s) - 1 - n)]
    return lst

# print(str_to_tuple('975'))
# print(str_to_tuple('95'))

def check_bull_cow(l1, l2): # this function has error: see example below
    '''d1, d2: dict'''
    count_bull = 0 
    count_cow = 0
    for num1, indx1 in l1:
        for num2, indx2 in l2:
            if num1 == num2:
                if indx1 == indx2:
                    count_bull += 1
                else:
                    count_cow += 1
    return count_bull, count_cow



def num_format(num, len_digit=3):
    result = "0" * (len_digit - len(str(num))) + str(num)
    return result

l1 = str_to_tuple(num_format(338))
l2 = str_to_tuple(num_format(3))

print(check_bull_cow(l1, l2))

# print(num_format('78'))
# print(type(num_format('78')))

def mimsmind1(len_digit=3):
    count = 0
    maxrounds = 2 ** len_digit + len_digit
    guess = None
    num = random.randint(0, 10 ** len_digit - 1)
    print(num)
    lst_random = str_to_tuple(num_format(num))
    print(lst_random)
    print("Let's play the mimsmind1 game. You have {} guesses.".format(maxrounds))
    prompt = "Guess a {}-digit number: ".format(len_digit)
    prompt_other = "Try again: "
    invalid = "Invalid input. "
    while count < maxrounds:
        try:
            guess = input(prompt)  #prompt should return "Invalid" for ValueError. NEED TO FIX!
            test = int(guess.strip())
            prompt = prompt_other
        except ValueError:
            print(invalid, end="")  
            continue
        if len(guess) != len_digit:
            print(invalid, end="")
            continue
        else:
            lst_guess = str_to_tuple(guess)
            if test == num:
                print("Congratulations. You guessed the correct number in {} tries.".format(count))
                break
            if count != (maxrounds - 1):
                check = check_bull_cow(lst_random, lst_guess)
                (count_bull, count_cow) = check
                print("{} bull(s), {} cow(s). ".format(count_bull, count_cow), end="")
            count += 1
    else:
        print("Sorry. You did not guess the number in {} tries. The correct number is {}.".format(maxrounds, num))
        

def main():
    mimsmind1(3)

if __name__ == "__main__":
    main()