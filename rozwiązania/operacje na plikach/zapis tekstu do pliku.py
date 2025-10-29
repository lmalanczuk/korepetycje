# otwieramy plik w trybie zapisu (utworzy nowy lub nadpisze istniejący)
with open("wynik.txt", "w", encoding="utf-8") as f:
    print("Wpisz kilka zdań (pusta linia kończy wprowadzanie):")

    while True:
        zdanie = input("> ")
        if zdanie == "":   # jeśli użytkownik nic nie wpisze -> zakończ
            break
        f.write(zdanie + "\n")  # zapisujemy zdanie i dodajemy nową linię

print("Zdania zostały zapisane w pliku wynik.txt.")