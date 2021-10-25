mads_mikkelsen = {'first_name':'mads', 'last_name':'mikkelsen', 'age':'55', 'city':'Osterbro'}

print(mads_mikkelsen)

for key, value in mads_mikkelsen.items():
    print(f"Klucz: {key}")
    print(f"Wartość: {value}")

print("=======================")

glossary = {'Aplikacja': 'Program przeznaczony do wykonywania określonych funkcji',
            'Bug': 'Błąd występujący w kodzie strony internetowej czy też aplikacji, który uniemożliwia jej poprawne działanie.',
            'GUI': 'Skrót od Graphical User Interface, czyli graficzny interfejs użytkownika',
            'Front-end': 'Ta część strony internetowej lub aplikacji, którą widzi jej końcowy użytkownik.',
            'Back-end': 'Wszystkie “zakulisowe” działania programistów, które są niezbędne do utrzymania ciągłości działania frontu strony internetowej czy też aplikacji.'}

for key, value in glossary.items():
    print(f"{key} : {value}")

glossary['Interpreter'] = 'Program, który analizuje kod źródłowy, a następnie go wykonuje. '
glossary['Zmienna'] = 'Nazwa określająca jakąś zapamiętywaną i wykorzystywaną w programie wartość lub strukturę danych.'
glossary['Lista'] = 'Indeksowana sekwencja takich samych lub różnych elementów, które można zmieniać. '
glossary['Tupla'] = 'Zawiera indeksowaną sekwencję takich samych lub różnych elementów, ale nie można ich zmieniać.'
glossary['Słownik'] = 'Typ mapowania, zestaw par elementów w postaci “klucz: wartość”. '

for key, value in glossary.items():
    print(f"{key} : {value}")

print("=======================")

#zadanie 6.5

rivers = {'nil': 'egipt', 'wisła': 'polska', 'tamiza': 'wielka brytania'}

for key, value in rivers.items():
    print(f"{key.title()} przepływa przez {value.title()} ")

for key in rivers.keys():
    print(key.title())

for value in rivers.values():
    print(value.title())

print("========================")


