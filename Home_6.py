# Сделать программу в виде функций в которой нужно будет угадывать число.
import random
def fun(guesses_made):
      
        number = random.randint(1, 10)
        print("Так, я загадав число від 1  до 10")
        for guesses_made in range(3):
            guess = int(input("Введіть ваше число: "))
            guesses_made += 1
            if guess < number:
                print("Ваше число менше загаданого.")
            elif guess > number:
                print("Ваше число більше загаданого.")
            elif guess == number:
                print("Ух ти! Ви угадали моє число, використавши до {} спроб!".format(guesses_made))
                break
        
        if guess != number:
             print("А ось і не вгадав! Я загадав інше число, а саме число {}".format(number))
        
fun(0)



# Сделать программу в виде функций в которой нужно будет угадывать число.
# import random
# def fun(guesses_made):
      
#         number = random.randint(1, 10)
#         print("Так, я загадав число від 1  до 10")
#         while guesses_made < 3:
#             guess = int(input("Введіть ваше число: "))
#             guesses_made += 1
#             if guess < number:
#                 print("Ваше число менше загаданого.")
#             if guess > number:
#                 print("Ваше число більше загаданого.")
#             if guess == number:
#                 break
#         if guess == number:
#             print("Ух ти! Ви угадали моє число, використавши до {} спроб!".format(guesses_made))
#         else:
#             print("А ось і не вгадав! Я загадав інше число, а саме число {}".format(number))
# fun(0)
