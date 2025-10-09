def read_matrix():
    rows = int(input('enter number of rows: '))
    assert rows > 0
    lst_of_lsts = [0] *rows
    
    for row in range(rows):
        lst_of_lsts[row] = list(map(int, input('enter: ').split()))
    return rows, len(lst_of_lsts[0]), lst_of_lsts

if __name__ == '__main__':
    rows, cols, matrix = read_matrix()
    target_value = int(input('enter value to search for: '))

    for idx, col in enumerate(zip(*matrix)):
        if target_value in col:
            print(f'found at {idx}')
            break
    else:
        print('Not Found')