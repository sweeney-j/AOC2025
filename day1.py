# Part 1
instructions = open("day1.txt")
current_position = 50
ans = 0
for rotation in instructions: 
    direction = rotation[0]
    number = int(rotation[1:].strip())
    if direction == 'R': 
        current_position = (current_position + number) % 100
    else: 
        current_position = (current_position - number) % 100
    if current_position == 0: 
        ans += 1
print(ans)

# Part 2
instructions = open("day1.txt")
current_position = 50
ans2 = 0
for rotation in instructions: 
    direction = rotation[0]
    number = int(rotation[1:].strip())
    if direction == 'R': 
        while number != 0:
            current_position = (current_position + 1) % 100
            if current_position == 0: 
                ans2 += 1
            number -= 1
    else: 
        while number != 0:
            current_position = (current_position - 1) % 100
            if current_position == 0: 
                ans2 += 1
            number -= 1
print(ans2)

