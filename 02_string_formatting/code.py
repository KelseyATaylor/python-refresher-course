# name = "Bob"
# greeting = f"Hello, {name}"

# print(greeting)

# name = "Rolf"

# print(greeting)


name = "Bob"

print(f"Hello, {name}")

name = "Rolf"

print(f"Hello, {name}")

# ############


name = "Lyla"
greeting = "Hello, {}"
with_name = greeting.format(name)

print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("Rolf", "Monday")
print(formatted)


