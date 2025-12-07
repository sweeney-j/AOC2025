from typing import DefaultDict

def read_input(): 
    f = open("input.txt")
    return f

def pt1(file): 
    sum = 0
    for line in file: 
        line_best = 0
        for idx, num in enumerate(line): 
            for j in range(idx + 1, len(line)): 
                line_best = max(int(str(num) + str(line[j])), line_best)
        sum += line_best
    return sum

def pt2(file):
    total = 0
    for sequence in file:
        sequence = sequence.strip()
        ans = ""
        l = 0

        while len(ans) < 12:
            need = 12 - len(ans)
            r = len(sequence) - need
            idx = find_largest_in_range(l, r, sequence)
            ans += sequence[idx]
            l = idx + 1

        total += int(ans)

    return total
        
# Returns the index of the largest number in the provided range. 
def find_largest_in_range(l, r, sequence): 
    best = 0
    best_idx = 0
    for i in range(l, r + 1): 
        if best < int(sequence[i]): 
            best_idx = i
            best = int(sequence[i])
    return best_idx

print(pt1(read_input()))
print(pt2(read_input()))
