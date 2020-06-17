f = open('archivo.txt', 'w')
lines = []
op = ''
while op != 'T':
    if op == 'A':
        line = input('Ingrese el texto: ')
        lines.append(line + '\n')
    op = input('¿Deseas añadir una línea al archivo (A) o terminar (T)?')
f.writelines(lines)
f.close()
f = open('archivo.txt', 'r')

for line in f:
    print(line)