# Instalacja Python 3.6 na Linux Ubuntu/Mint

Najprawdopodobniej główną wersją Python3 na Twoim systemie będzie Python 3.5.2. Wykonaj poniższe kroki:

1. sprawdź czy Python 3.6 jest zainstalowany na Twoim systemie
    * uruchom polecenie `python3 -V`
        - jeśli odpowiedź nie jest `Python 3.6.x` rób kolejny krok
        - jeśli odpowiedź jest `Python 3.6.x` to w dalszej części używaj polecenia `python3`
    * uruchom polecenie `python3.6` 
        - jeśli polecenie będzie nie rozpoznane musisz zainstalować Pythona 3.6
        - jeśli uruchomi się interpreter - w dalszej części warsztatu używaj polecenia `python3.6` 
    
1. instalacja Python 3.6
    * dodaj repozytorium z Pythonem 3.6 do systemu: `sudo add-apt-repository ppa:jonathonf/python-3.6`
    * zaktualizuj apt: `sudo apt-get update`
    * zainstaluj Python 3.6: `sudo apt-get install python3.6`
    * sprawdź poprawność instalacji: `python3.6 -V` w odpowiedzi powinieneś zpbaczyć `Python 3.6.3`
    * w dalszej części warsztatu używaj polecenia `python3.6`
    
     
      