import random


# readme
# lisää ehdotuksia tiedostoon

print("Kirjoittamisehdotusten generaattori / Writing prompt generator")
print()
print("Tämä sovellus antaa sinulle haluamasi määrän tai satunnaisen määrän  \n\
sanoja tai ilmaisuja, joita voit käyttää kirjoittamisen inspiraationa.")
print()


maara = -1;
while maara not in range(0,13):
    maara = int(input("Montako ehdotusta haluat? Syötä kokonaisluku välillä 1-12.\n\
Jos syötät luvun 0, kone arpoo sinulle satunnaisen määrän. "))
    if maara not in range(0,13):
        print("Syötit virheellisen luvun.")

if maara == 0:
    maara = random.randint(1, 13)


# listan luominen
tiedosto = open("ehdotukset.txt", "r")
lista = tiedosto.readlines()


# uniikkien satunnaislukujen luominen ehdotusten hakemista varten
satunnaisluvut = random.sample(range(0, len(lista)), maara)

print()
# ehdotusten hakeminen ja tulostaminen listasta satunnaislukujen avulla
for i in satunnaisluvut:
    print(lista[i])
