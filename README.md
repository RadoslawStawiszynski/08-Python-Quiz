# Quiz o programowaniu

Autor: Stawiszynski Radoslaw
Rok: 2022/2023
Wydział: Informatyka

## Opis programu

Program stanowi quiz o programowaniu. Użytkownik może uczestniczyć w quizie, odpowiadając na pytania dotyczące programowania. Wyniki gracza są zapisywane, a także przechowywane dane użytkowników, takie jak imię, wiek, oraz identyfikator.

## Instrukcja uruchomienia

Aby uruchomić program, wykonaj plik `main.py`. Program wczytuje pytania z pliku `pytania_i_odpowiedzi.json` i przeprowadza quiz, zapisując wyniki gracza w pliku `wyniki.txt`. Dodatkowo, dane użytkowników są przechowywane w pliku `dane_uzytkownika.txt`.

## Struktura projektu

- `main.py`: Główny plik programu, zawierający funkcję `main`.
- `definicje.py`: Moduł z funkcjami definiującymi operacje wejścia-wyjścia i logikę gry.
- `pytania_i_odpowiedzi.json`: Plik zawierający pytania i odpowiedzi do quizu.
- `wyniki.txt`: Plik zapisujący wyniki graczy.
- `dane_uzytkownika.txt`: Plik przechowujący dane użytkowników.

## Wymagania

- Python 3.x

## Uruchomienie programu

```bash
python main.py
