notas = []
while True:
    x = round(float(input()), 1)
    if 0 <= x <= 10:
        notas.append(x)
    else:
        print("nota invalida")
    if len(notas) == 2:
        break

media = sum(notas)/2
print(f"media = {media:.2f}")
