animal = "cat"

ex1 = "My " + animal + " sleeping"
ex2 = "My {} sleeping".format(animal)
ex3 = f"My {animal} sleeping."


country = {"name": "Finland", "population": 5531000}


finland_ex = "In {name} live {population} people.".format(**country)
print(finland_ex)


print(5531000 == 5_531_000) 


print(f"{10**2 + 10}")


food = ["apple", "cola", "butter", "bread"]
print(f"I have to buy {', '.join(product for product in food)}.")


hello = "Hello There"
print(hello.upper())

print(f"{' '.join(product.upper() for product in food)}")

print(f"{' '.join(product.capitalize() for product in food)}")

print()

print("Hello World", end="!")
print(" What's up?")


for element in food:
    print(element.replace("a", ""), end=", ")