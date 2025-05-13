import random

def game5():
    pass


def game3():
    user_choice = input("Виберіть K, N, B - ")
    user_choice = str.upper(user_choice)
    comp_choice = random.choice("KNB")
    print(f"Гравець - {user_choice}, Комп'ютер - {comp_choice}")
    if user_choice == comp_choice:
        return "D"
    elif (user_choice == "N" and comp_choice == "B" or
          user_choice == "K" and comp_choice == "N" or
          user_choice == "B" and comp_choice == "k"):
        return "U"
    else:
        return "C"



def print_result(result, winner):
    if winner == "D":
        print("В цьому раунді нічья")
    elif winner == "U":
        print("В цьому раунді переміг гравець")
        result["user"] += 1
    elif winner == "C":
        print("В цьому раунді переміг комп'ютер")
        result["comp"] += 1
    print(f"Гравець - {result['user']}, Комп'ютер - {result['comp']}")


result = {"user":0, "comp":0}

f = int(input("На скільки комбінацій буде гра 3 або 5? - "))
if f == 3:
    game = game3
else:
    game = game5

for i in range(1, 4):
    print(f" ======== РАУНД №{i} ========")
    print_result(result, game())
    print()