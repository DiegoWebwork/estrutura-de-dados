elementos = [['a', 'b', 'c', 'd'], ['q', 'i', 'n', 'm'], ['f', 'e', 'h', 'j'], ['p', 'o', 'l','g'],];

elementos2 = sorted([elementos for j in elementos for elementos in j])

print(elementos2)
