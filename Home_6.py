# Сделать программу в виде функций в которой нужно будет угадывать число.
import random
def fun(guesses_made):
      
        number = random.randint(1, 10)
        print("Так, я загадав число від 1  до 10")
        while guesses_made < 3:
            guess = int(input("Введіть ваше число: "))
            guesses_made += 1
            if guess < number:
                print("Ваше число менше загаданого.")
            if guess > number:
                print("Ваше число більше загаданого.")
            if guess == number:
                break
        if guess == number:
            print("Ух ти! Ви угадали моє число, використавши до {0} спроб!".format(guesses_made))
        else:
            print("А ось і не вгадав! Я загадав інше число, а саме число {0}".format(number))
fun(0)
