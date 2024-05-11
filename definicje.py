# Importujemy bibliotekę do obsługi systemu wejścia-wyjścia
import sys
import random
import string
import json


def wczytaj_dane_uzytkownika():
    dane_uzytkownika = []
    try:
        with open("dane_uzytkownika.txt", "r") as plik:
            lines = plik.readlines()
            i = 0
            while i + 2 < len(lines):
                uzytkownik = {
                    'id': lines[i].split(":")[1].strip(),
                    'imie': lines[i+1].split(":")[1].strip(),
                    'wiek': lines[i+2].split(":")[1].strip()
                }
                dane_uzytkownika.append(uzytkownik)
                i += 4  # Przeskakujemy 4 linie, aby przejść do kolejnego użytkownika
    except FileNotFoundError:
        pass
    return dane_uzytkownika

def pobierz_imie():
    while True:
        imie = input("Podaj swoje imię graczu: ")
        if imie.strip():  # Sprawdź, czy podano niepusty ciąg znaków
            return imie
        else:
            print("Podaj poprawne imię.")

def generuj_id():
    return ''.join(random.choices(string.ascii_letters + string.digits, k=8))

def czy_uzytkownik_istnieje(imie, dane_uzytkownika):
    for uzytkownik in dane_uzytkownika:
        if uzytkownik['imie'] == imie:
            return True
    return False

def pobierz_wiek():
    while True:
        try:
            wiek = int(input("Ile masz lat?: "))
            return wiek
            break
        except ValueError:
            print("Podaj poprawny wiek jako liczbę.")

def zapisz_dane_do_pliku(imie, wiek, dane_uzytkownika):
    uzytkownik = {
        'id': generuj_id(),
        'imie': imie,
        'wiek': wiek,
    }

    dane_uzytkownika.append(uzytkownik)

    with open("dane_uzytkownika.txt", "w") as plik:
        for uzytkownik in dane_uzytkownika:
            plik.write(f"ID: {uzytkownik['id']}\n")
            plik.write(f"Imię: {uzytkownik['imie']}\n")
            plik.write(f"Wiek: {uzytkownik['wiek']}\n\n")

    print("Dane zostały zapisane do pliku.\n\n")

def rozpocznij_gre():
    dane_uzytkownika = wczytaj_dane_uzytkownika()

    # Operacja wejścia: pobranie danych od użytkownika z klawiatury
    imie = pobierz_imie()

    if czy_uzytkownik_istnieje(imie, dane_uzytkownika):
        print("Użytkownik o podanym imieniu już istnieje.")
        sys.exit()

    # Operacja wyjścia: wypisanie powitania na ekranie
    print(f"Witaj, {imie}!\nZapraszam Cię do gry w 'Quiz o programowaniu'.")

    # Operacja wejścia: pobranie wieku od użytkownika, dodanie obsługi błędu
    wiek = pobierz_wiek()

    return imie, wiek, dane_uzytkownika

#------------------#

# Kolejne zadanie 2

def wczytaj_wyniki_z_pliku():
    wyniki = {}
    try:
        with open("wyniki.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                imie, wynik = line.strip().split(":")
                wyniki[imie] = int(wynik)
    except FileNotFoundError:
        pass
    return wyniki

def wczytaj_pytania(plik):
    with open(plik, 'r') as file:
        return json.loads(file.read())

def wyswietl_pytanie(pytanie):
    print(f"{pytanie['indeks']}. {pytanie['pytanie']}")
    for odpowiedz in pytanie['odpowiedzi']:
        print(odpowiedz)

def sprawdz_odpowiedz(pytanie, odpowiedz):
    return odpowiedz.upper() == pytanie['poprawna']

def zapisz_wynik_do_pliku(imie, wynik):
    with open("wyniki.txt", "a") as file:
        file.write(f"{imie}: {wynik}\n")

