floor = 0
negative = False
character_count = 0

input = open('input.txt')
input = input.read()

for character in input:
    if character == '(':
        floor = floor + 1
    elif character == ')':
        floor = floor - 1

    if negative == False:
        character_count = character_count + 1

    if floor < 0:
        negative = True

print('position of first negative floor: ' + str(character_count))
print('floor: ' + str(floor))
