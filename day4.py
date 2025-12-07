def read_input(): 
    f = open("input.txt")
    input = []
    for line in f: 
        line = line.strip()
        row = []
        for i in range(len(line)): 
            row.append(line[i])
        input.append(row)
    return input

directions = [[-1, -1], [0, -1], [-1, 1], [-1, 0], [1, 0], [1, -1], [0, 1], [1, 1]]

def calculate_part_one(paper_matrix): 
    remove_paper_coords = []
    accessible_paper = 0
    for row in range(len(paper_matrix)): 
        for col in range(len(paper_matrix[0])): 
            if paper_matrix[row][col] == '@': 
                count = 0
                for direction in directions: 
                    temp_col = col + direction[0]
                    temp_row = row + direction[1]
                    new_posn = [temp_row, temp_col]
                    if is_valid_position(new_posn, paper_matrix): 
                        if paper_matrix[temp_row][temp_col] == '@': 
                            count += 1
                if count <= 3: 
                    accessible_paper += 1
                    remove_paper_coords.append([row, col]) 
    return accessible_paper, remove_paper_coords

def update_matrix(paper_matrix, update_coords): 
    for coords in update_coords: 
        x, y = coords
        paper_matrix[x][y] = "."
    return paper_matrix

def calculate_part_two(paper_matrix): 
    accessible_paper, remove_coords = calculate_part_one(paper_matrix) 
    new_matrix = update_matrix(paper_matrix, remove_coords)
    if accessible_paper > 0: 
        return accessible_paper + calculate_part_two(new_matrix)
    else: 
        return 0

def is_valid_position(position, paper_matrix): 
    x, y = position
    if x < 0 or x >= len(paper_matrix): 
        return False
    if y < 0 or y >= len(paper_matrix[0]): 
        return False
    return True


print(calculate_part_one(read_input()))
print(calculate_part_two(read_input()))
