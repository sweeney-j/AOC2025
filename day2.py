def read_input(): 
    f = open("input.txt")

    total_numbers = []
    number_pairs = []
    current_number = ""
    for char in f.readline(): 
        if char == "-": 
            number_pairs.append(current_number)
            current_number = ""
        elif char == ",": 
            number_pairs.append(current_number)
            total_numbers.append(number_pairs)
            current_number = ""
            number_pairs = []
        else: 
            current_number += char

    # To get the last pair
    number_pairs.append(current_number[:-1])
    total_numbers.append(number_pairs)
    return total_numbers 

def pt1(): 
    all_pairs = read_input()
    bad_numbers = [] 
    sum = 0
    for pairs in all_pairs: 
        for num in range(int(pairs[0]), int(pairs[1]) + 1): 
            if len(str(num)) % 2 == 0: 
                length = len(str(num)) // 2
                first_half = str(num)[0:length]
                second_half = str(num)[length:]
                if first_half == second_half: 
                    bad_numbers.append(num)
                    sum += num
    return sum 

def pt2(): 
    all_pairs = read_input()
    sum = 0 
    for pairs in all_pairs: 
        for num in range(int(pairs[0]), int(pairs[1]) + 1): 
            str_num = str(num)
            if len(str_num) < 2: 
                continue 
            for i in range(0, len(str_num) // 2): 
                current_substring = str_num[:i + 1]
                built_string = current_substring * (len(str_num) // (i+1))
                if built_string == str_num: 
                    sum += num
                    break 
    return sum

print(pt1())
print(pt2())







