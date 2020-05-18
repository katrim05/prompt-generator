import random

print("Kirjoittamisehdotusten generaattori / Writing prompt generator")
print()
print("Tämä sovellus antaa sinulle haluamasi määrän tai satunnaisen määrän  \n\
sanoja tai ilmaisuja, joita voit käyttää kirjoittamisen inspiraationa.")
print()

def kysy_maara():   
    maara = -1
    while maara not in range(0,13):
        maara = int(input("Montako ehdotusta haluat? Syötä kokonaisluku välillä 1-12.\n\
Jos syötät luvun 0, kone arpoo sinulle satunnaisen määrän. "))
        if maara not in range(0,13):
            print("Syötit virheellisen luvun.")
    if maara == 0:
        maara = random.randint(1, 13)
    return maara

def lueLista(tiedosto):
    avaaja = open(tiedosto, "r")
    lista = avaaja.readlines()
    return lista

def arvo_ehdotukset(lista, maara):
    satunnaisluvut = random.sample(range(0, len(lista)), maara)
    ehdotukset = []
    for i in satunnaisluvut:
       ehdotukset.append(lista[i])
    return ehdotukset

def tulosta_lista(ehdotukset):
    #tulostetaan alkuun tyhjä rivi selkeyden vuoksi
    print()
    for item in ehdotukset:
        print(item)

def main():
    maara = kysy_maara()
    lista = lueLista("ehdotukset.txt")
    ehdotukset = arvo_ehdotukset(lista, maara)
    tulosta_lista(ehdotukset)

if __name__ == "__main__":
    main()
