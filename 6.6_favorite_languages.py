# zadanie 6.6

favorite_languages = {
    'janek': 'python',
    'sara': 'c',
    'edward': 'ruby',
    'paweł': 'python',
}

for name, language in favorite_languages.items():
    print(f"Ulubiony język oprogramowania użytkownika {name.title()} to {language.title()}")

friends = ['paweł', 'sara']
for name in favorite_languages.keys():
    print(f"Witaj, {name.title()}")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\tWitaj, {name.title()}! Widzę, że Twoim ulubionym językiem oprogramowania jest {language}.")

if 'elżbieta' not in favorite_languages.keys():
    print("Elżbieta, proszę, weź udział w naszej ankiecie!")

for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, dziękujemy za udział w ankiecie.")

respondents = ['dagmara', 'sara', 'daniel', 'maria', 'janek']

for respondent in respondents:
    if respondent in favorite_languages.keys():
        print(f"Thank you, {name.title()}, for taking part in a survey")
    else:
        print(f"{respondent.title()}, you have to take part in a survey first.")

