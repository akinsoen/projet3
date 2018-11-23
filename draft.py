import sys
lab = sys.argv[1]
g_or_d = 0
if sys.argv[2] == 'd':
    g_or_d = 1
elif sys.argv[2] == 'g':
    g_or_d = -1


f = open('lab1.txt')
mat_lab = []
for ligne in f:
    line = []
    for c in ligne:
        if c == '#' or c == ' ':
            line.append(c)
    mat_lab.append(line)

f.close()
print(mat_lab)


def print_lab():
    res = ''
    for i in mat_lab:
        res_ligne = ''
        for j in i:
            res_ligne += j
        res += res_ligne + '\n'
    print(res)

direction = 'v'
def redirection(direction):
    if g_or_d == 1:                  # droite
        if mat_lab[col - g_or_d][line] == ' ':
            direction = '<'
        elif mat_lab[col][line + 1] == '#':    # remplacer par else ?
            if mat_lab[col + 1][line] == ' ':
                direction = '>'
            else:
                direction = '^'
        



    if g_or_d == -1:                 # gauche


print_lab()



col = 1
line = 0
position = mat_lab[col][line]
path = []


if direction == 'v':
    if mat_lab[col - g_or_d][line] == '#':
        if mat_lab[col][line + 1] == ' ':
            mat_lab[col][line + 1] = 'v'
            path.append((col, line + 1))
            mat_lab[col][line] = ' '
            line += 1
            print_lab()
        else:
            redirection(direction)
    else:
        redirection(direction)

if direction == '>':
    if mat_lab[col][line + g_or_d] == '#':
        if mat_lab[col + 1][line] == ' ':
            mat_lab[col + 1][line] = '>'
            path.append((col + 1, line))
            mat_lab[col][line] = ' '
            col += 1
            print_lab()
        else:
            redirection(direction)
    else:
        redirection(direction)

if direction == '^':
    if mat_lab[col + g_or_d][line] == '#':
        if mat_lab[col][line - 1] == ' ':
            mat_lab[col][line - 1] = '^'
            path.append((col, line - 1))
            mat_lab[col][line] = ' '
            line -= 1
            print_lab()
        else:
            redirection(direction)
    else:
        redirection(direction)

if direction == '<':
    if mat_lab[col][line - g_or_d] == '#':
        if mat_lab[col - 1][line] == ' ':
            mat_lab[col - 1][line] = '<'
            path.append((col - 1, line))
            mat_lab[col][line] = ' '
            col -= 1
            print_lab()
        else:
            redirection(direction)
    else:
        redirection(direction)