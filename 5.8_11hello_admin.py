# zadania 5.8 - 5.9

users = []


if users:
    for user in users:
        if user == 'admin':
            print('Witaj, admin! Czy chcesz przejrzeć dzisiejszy raport?')
        else:
            print(f"Witaj {user}! Dziękujemy, że ponownie się zalogowałeś")
else:
    print("Musimy znależć jakichś użytkowników!")

# zadanie 5.10
# jak sprawić, by wielkość liter nie miała znaczenia? - kopie listy lower ???

print("====================")

current_users = ['Adam', 'Zosia', 'Przemek', 'Inga', 'Klaudia']
new_users = ['Mateusz', 'Michał', 'Klaudia', 'Natalia', 'Łukasz']


for new_user in new_users:
    if new_user in current_users:
        print("Ta nazwa użytkownika jest już zajęta. Proszę, wybierz inną nazwę.")
    else:
        print("Ta nazwa jest wolna - możesz jej użyć.")

#zadanie 5.11

print("---------------------")

liczby = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for liczba in liczby:
    if liczba == 1:
        print(f"{liczba}st")
    elif liczba == 2:
        print(f"{liczba}nd")
    elif liczba == 3:
        print(f"{liczba}rd")
    else:
        print(f"{liczba}th")
