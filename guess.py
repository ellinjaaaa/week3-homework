import random

a=random.randint(1, 100)

print("Tev ir 10 mēģinājumi, lai uzminētu skaitli!")

number_of_guesses=0

player_win=False #sākumā nosaku, ka spēlētājs vēl nav vinnējis - =False

while number_of_guesses<10:
    izvele=int(input("Izvēlies skaitli no 1 līdz 100:"))
    number_of_guesses+=1 #palielina mēģinājumu skaitu par 1
    print(f"Šis bija Tavs {number_of_guesses}. mēģinājums.")
    if izvele>a:
        print("Tevis izvēlētais skaitlis ir par lielu!")
    elif izvele<a:
        print("Tevis izvēlētais skaitlis ir par mazu!")
    else:
        player_win=True #ja spēlētājs uzmin, tad tagad spēlētājs ir vinnējis, tādēļ =True
        print("Apsveicu! Tu uzminēji skaitli!")
        break

if player_win==False: #ja 10 mēģinājumi ir beigušies, bet spēlētājs nav joprojām uzminējis, tad izvada pareizo skaitli
    print(f"Pareizas skaitlis: {a}")
    exit()