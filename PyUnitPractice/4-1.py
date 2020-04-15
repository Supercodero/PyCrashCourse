pizzas = ["piz","oh!jones","kfc","mcdonload"]
for pizza in pizzas:
    print("I like "+pizza.title()+" pizza!\n")

print("I really love pizza")

print(pizzas)
print(sorted(pizzas))
pizzas.reverse()
print(pizzas)
pizzas.sort()
print(pizzas)

print("The first three items in the list are")
print(pizzas[:3])
print("Three items from the middle of the list are")
print(pizzas[1:3])
print("The last three items in the list are")
print(pizzas[-3:])

friend_pizzas = pizzas[:]
pizzas.append("my_favorite")
friend_pizzas.append("friend_favorite")

print("my favorite pizzas are:")
for pizza in pizzas:
    print(pizza)

print("\n my friend's favorite pizzas are: ")
for pizza in friend_pizzas:
    print(pizza)