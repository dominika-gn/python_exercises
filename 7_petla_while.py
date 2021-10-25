# 7.4

prompt = "\nJakie dodatki wybierasz do swojej pizzy?"
prompt += "\nNapisz 'koniec', aby zakończyć działanie programu"
message = ''
while message != 'koniec':
    message = input(prompt)
    if message != 'koniec':
        print(f"{message.title()} został dodany do pizzy.")
    else:
        print(message)

print("===================")
# 7.5

age = int(input("Proszę, podaj swój wiek: "))

while age > 0:
    if age < 3:
        print("Przysługuje Ci bilet bezpłatny")
    elif 3 <= age < 12:
        print("Bilet kosztuje 10 zł.")
    else:
        print("Bilet kosztuje 15 zł.")
    break