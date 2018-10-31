import random

def main():
    gen_number = Gen_a_number()
    un = user_number()
    response = compare_numbers(gen_number, un)
    play_again(response)

def Gen_a_number():
    gen_number = (random.randint(1, 1000)) 
    # print(gen_number)
    return gen_number

def user_number():
    un = int(input("Guess your number between 1 and 1000 : "))
    return un

def compare_numbers(gen_number, un):
    count = 1
    while un!=gen_number and count < 10:
        if un < gen_number:
            un = int(input("Guess high, you have {} tries left: ".format(10-count)))
        elif un > gen_number:
            un = int(input("Guess low, you have {} tries left: ".format(10-count)))
        count = count + 1
    else:
        if un == gen_number:
            print("Awesome, You got it in {}: ".format(count))  
        else:
            print("You Lose Buddy!!! my number was {}: ".format(gen_number))
        response = input("Do you want to play again(Y/N)? " )
        return response 


def play_again(response):
    if response.lower() == "yes" or response.upper() == "Y":
        main()
    else:
        print("Thanks for playig the Number Game")

      
            

if __name__ == "__main__":
    main()
