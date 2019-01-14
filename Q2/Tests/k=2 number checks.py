file = open("ephemeral_numbers_4.txt", "r")
mods = set()
for number in file:
    res = int(number)%9
    mods.add(res)
print(mods)