import sys



f = open('lab1.txt')
mat_lab = []
for ligne in f:
    line = []
    for c in ligne:
        if c == '#' or  c == ' ':
            line.append(c)
    mat_lab.append(line)

print(mat_lab)

def print_lab(mat_lab):
    res = ''
    for i in mat_lab:
        res_ligne = ''
        for j in i:
            res_ligne += j
        res += res_ligne + '\n'
    print(res)



print_lab(mat_lab)
