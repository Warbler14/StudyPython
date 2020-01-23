fruit = {"orange": "a sweet, citrus fruit"
         , "apple": "good for making cider"
         , "lemon": "a sour, yellow citrus fruit"
         , "grape": "a small, sweet fruit growing in bunches"
         , "lime": "a sour, green citrus fruit"}

print(fruit)
print("========================================================================================")

print(fruit.keys())
print("========================================================================================")

ordered_keys = list(fruit.keys())
print(ordered_keys)
print("========================================================================================")

ordered_keys.sort()
print(ordered_keys)
print("========================================================================================")

ordered_keys = sorted(list(fruit.keys()))
print(ordered_keys)
print("========================================================================================")

for f in ordered_keys:
    print(f + " - " + fruit[f])
print("========================================================================================")

for f in sorted(fruit.keys()):
    print(f + " - " + fruit[f])
print("========================================================================================")

for f in sorted(fruit):
    print(f + " - " + fruit[f])
print("========================================================================================")

fruit["tomato"] = "tomato"

for f in sorted(fruit):
    print(f + " - " + fruit[f])
print("========================================================================================")

t_fruit = tuple(fruit.items())
for snack in sorted(t_fruit):
    item, description = snack
    print(item + " = " + description)
print("========================================================================================")

