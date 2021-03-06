# Portfel

W tym kroku odtworzymy portfel zawierający :moneybag: :
* **1.000.000 NEO**
* **7 624 GAS**

>Są to coiny istniejące wyłacznie w privnecie - nie użyjesz ich w main necie :unamused:

## Dane portfela

* **WIF key:** `KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr`
* **Adres:** `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`
* **Script hash:** `b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'`

Wyjaśnienie:
* WIF - jest to klucz prywatny portfela
* Adres - adres publiczny portfela
* Script hash - zhashowany adres portfela - używany wewnątrz kontraktów w funkcji `CheckWitness`

## Odtworzenie portfela

Możemy zrobić to na 2 sposoby:

1. Pobranie pliku portfela  
    Musisz być w bashu wewnątrz kontenera, w folderze `/`  
    * pobierz plik portfela: `curl https://s3.amazonaws.com/neo-experiments/neo-privnet-old.wallet -o main.wallet`
    * uruchom neo cli: `python3 /opt/neo-python/prompt.py -p`
    * otwórz portfel: `open wallet main.wallet`  
      hasło: `coz`
    * przebuduj portfel: `wallet rebuild`
        
        

1. odtworzenie za pomocą klucza WIF  
    Poniższe kroki wykonywane są z poziomu neo-python. Aby uruchomić neo-python:
    * uruchom cli neo: `python3 opt/neo-pythonprompt.py -p`
    * utwórz nowy portfel: `create wallet main.wallet`
    * importuj klucz: `import wif KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr`
    * przebuduj portfel: `wallet rebuild`
    
Po przebudowaniu portfela możesz sprawdzić stan środków poleceniem `wallet`. W odpowiedzi zobaczysz informacje o portfelu, jego adresach oraz stanie środków

>"synced_balances": [  
        "[NEO]: 100000000.0 ",  
        "[NEOGas]: 7624.0 "  
    ],
    
W folderze `/` znajdują się 3 portfele: `wallet1.db3`, `wallet2.db3`, `wallet3.db3`. Hasło do każdego z nich to `coz` możesz je używać w swoich testach kontraktu.
    
[Przejdź do kolejnego kroku - ]()
   


