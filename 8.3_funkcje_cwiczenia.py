# zadanie 8.3

def make_shirt(shirt_size='L', shirt_text='Uwielbiam Pythona'):
    # wyswietla rozmiar i tekst na koszulce
    print(f"Rozmiar koszulki to: {shirt_size}")
    print(f"Napis na koszulce to: {shirt_text}.")


make_shirt('L', 'Bum szaka laka')
make_shirt(shirt_size='S', shirt_text='Desperados')
make_shirt()
make_shirt('M')

print('==================')

#zadanie 8.6

def city_country(city, country):
    pair = f"{city}, {country}"
    print(pair.title())


city_country('paris', 'france')
city_country('barcelona', 'spain')
city_country('lisbon', 'portugal')

print('========================')

#zadanie 8.7

def make_album(artist_name, album_title, tracks_number=None):
    # zwraca słownik
    album = {'artist': artist_name.title(), 'title': album_title.title()}
    if tracks_number:
        album['number of tracks'] = tracks_number
    return album

# wprowadzenie danych za pomocą input:
while True:
    print("Podaj dane dotyczące albumu. Jeśli chcesz zakończyć, wciśnij 'q'")
    a_name = input("Podaj nazwę artysty: ")
    if a_name == 'q':
        break
    a_title = input("Podaj nazwę albumu: ")
    if a_title == 'q':
        break
    t_number = input("Podaj liczbę utworów na płycie: ")
    if t_number == 'q':
        break

    new_album = make_album(a_name, a_title, t_number)
    print(new_album)


# standardowe wywołanie funkcji:
# new_album_1 = make_album('Sanah', 'Irenka')
# new_album_2 = make_album('Sanah', 'Królowa dram', '13')
# new_album_3 = make_album('Kortez', 'Mój dom')
# print(new_album_1)
# print(new_album_2)
# print(new_album_3)