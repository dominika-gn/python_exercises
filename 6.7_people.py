mads_mikkelsen = {'first_name':'mads', 'last_name':'mikkelsen', 'age':'55', 'city':'Osterbro'}
keanu_reeves = {'first_name':'keanu', 'last_name':'reeves', 'age':'57', 'city':'Bejrut'}
charlize_theron = {'first_name':'charlize', 'last_name':'theron', 'age':'46', 'city':'Benoni'}

people = [mads_mikkelsen, keanu_reeves, charlize_theron]

for person in people:
    print(person)

# 6.9

favorite_places = {
    'daniel': ['majorka', 'tajlandia', 'izrael'],
    'dominika': ['nowy jork', 'portugalia', 'włochy'],
    'karina': ['szwajcaria', 'dania', 'hiszpania']
}

for name, places in favorite_places.items():
    print(f"Ulubione miejsca użytkownika {name.title()} to:")
    for place in places:
        print(f"\t{place.title()}")