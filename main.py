# STAWISZYNSKI RADOSLAW , NR INDEKSU 159088, 
# ROK 2022/2023, WYDZIAL INFORMATYKA, GRUPA D1, SEM 2

# Program obsługujący system wejścia-wyjścia

from definicje import wczytaj_wyniki_z_pliku, rozpocznij_gre, wczytaj_pytania, zapisz_wynik_do_pliku, wyswietl_pytanie, sprawdz_odpowiedz, zapisz_dane_do_pliku

def main():
    imie, wiek, dane_uzytkownika = rozpocznij_gre()

    zapisz_dane_do_pliku(imie, wiek, dane_uzytkownika)

    wyniki = wczytaj_wyniki_z_pliku()

    for pytanie in wczytaj_pytania("pytania_i_odpowiedzi.json"):
        wyswietl_pytanie(pytanie)
        odpowiedz = input("Twoja odpowiedź: ")
        if sprawdz_odpowiedz(pytanie, odpowiedz):
            print("Poprawna odpowiedź!\n")
            wyniki[imie] = wyniki.get(imie, 0) + 1
        else:
            print("Błędna odpowiedź.\n")

    zapisz_wynik_do_pliku(imie, wyniki[imie])
    print(f"Twój wynik: {wyniki[imie]}")
    print("Dziękuję za udział w grze!\n\n")

if __name__ == "__main__":
    main()
