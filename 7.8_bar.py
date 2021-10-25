sandwich_orders = ['salami', 'pastrami', 'prosciutto', 'camembert', 'kurczak', 'serek', 'prosciutto', 'pastrami', 'pastrami']
finished_sandwiches = []

print("W barze skończyło się pastrami")

#usuwa dany element dopóki nie zostaną usunięte wszystkie 'pastrami':
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# przenosi elementy z jednej listy na drugą
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()

    print(f"Przygotowano kanapkę {current_sandwich}")
    finished_sandwiches.append(current_sandwich)

print(f"\nZrobiono następujące kanapki:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich.title())