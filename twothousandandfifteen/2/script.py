input = open('input.txt')
input = input.read()
input = input.split('\n')

flaeche = 0
ribbon = 0

for i in input:
    biggest_value = 0

    if i != '':
        i = i.split('x')
        i = [int(e) for e in i]

        biggest_value = i.index(max(i))

        laenge = int(i[0])
        breite = int(i[1])
        hoehe = int(i[2])

        a = laenge * breite
        b = breite * hoehe
        c = hoehe * laenge

        sides = [a, b, c]

        smallest_side = min(sides)

        flaeche = flaeche + 2 * laenge * breite + 2 * breite * hoehe + 2 * hoehe * laenge + smallest_side

        del i[biggest_value]

        ribbon = ribbon + int(i[0]) + int(i[0]) + int(i[1]) + int(i[1]) + laenge * breite * hoehe

print('fläche für das geschenkpapier: ' + str(flaeche))
print('länge der schleife: ' + str(ribbon))
