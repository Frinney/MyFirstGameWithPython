import time
from random import randint
play = True
menu = -1
while play:
    print("1 - Начать играть\n"
          "2 - Выход из игры\n"
          )
    if menu == -1:
        try:
            menu = int(input())
        except ValueError as e:
            print("gfghvbfh")
            menu = -1

    if menu == 1:
        houseDoor = randint(1, 10)
        print(houseDoor)
        play = False
        print("Ваш отец был убит в этом доме и вы решили отомстить. Ходят слухи что это все сделал призрак. Чтобы убить этого призрака вам нужно пройти все двери. И уничтожить призрака")
        print("Выбирете дверь в которую хотите пойти.Всего 10 дверей")


    if menu == 2:
         print("Закрытие игры")
         time.sleep(1)
         print("5")
         time.sleep(1)
         print("4")
         time.sleep(1)
         print("3")
         time.sleep(1)
         print("2")
         time.sleep(1)
         print("1")
         play = False
         print("Пока")
         exit(0)
#GAME

a = int(input())
if a == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if a != houseDoor:
    print("Вы проходите дальше")

s = int(input())
if s == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if s != houseDoor:
    print("Вы проходите дальше")


b = int(input())
if b == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if b != houseDoor:
    print("Вы проходите дальше")

c = int(input())
if c == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if c != houseDoor:
    print("Вы проходите дальше")

s = int(input())
if s == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if s != houseDoor:
    print("Вы проходите дальше")

n = int(input())
if n == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if n != houseDoor:
    print("Вы проходите дальше")

m = int(input())
if m == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if m != houseDoor:
    print("Вы проходите дальше")

q = int(input())
if q == houseDoor:
    print("GAME OVER")
    time.sleep(5)
    exit(0)
if q != houseDoor:
    print("Вы проходите дальше")

w = int(input())
if w == houseDoor:
    print("GAME OVER")
    play = False
    time.sleep(5)
    exit(0)
if w != houseDoor:
    print("Вы отомстили призраку за убийство отца")
    print("Спасибо за проходжение.Выполняется закрытие игры")
    time.sleep(15)
    exit(0)
if s == a:
    print(hfghg)





















