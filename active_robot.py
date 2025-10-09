if __name__ =='__main__':
    rows, cols, *commands = input().split()
    #(*)commands means that the rest of the input will be collected as a list
    #first 2 is row and col and rest is assigned in the commands list
    rows, cols = int(rows), int(cols)

    #up, right, down, left
    rd = [-1, 0, 1, 0]
    cd = [0, 1, 0, -1]
    r, c = 0, 0

    while commands:
        dir, steps, *commands = commands
        dir = ['up', 'right', 'down', 'left'].index(dir)
        steps = int(steps)

        r = (r + rd[dir] * steps) % rows    # the % will get rid of unnecessary steps
        c = (c + cd[dir] * steps) % cols    # and will loop back

        print(r, c)