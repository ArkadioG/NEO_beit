# Portfel 

Portfel służy do przechowywania NEO i GASu, wdrażania i uruchamiania kontraktów.

Po instalacji **neo-local** dostępny jest portfel zawierający :moneybag: :
* **1.000.000 NEO**
* **7 624 GAS** 

## Dane portfela

* ścieżka do portfela: `./neo-privnet.wallet`
* hasło do portfela `coz`


* **WIF key:** `KxDgvEKzgSBPPfuVfw67oPQBSjidEiqTHURKSDL1R7yGaGYAeYnr`
* **Adres:** `AK2nJJpJr6o664CWJKi1QRXjqeic2zRp8y`
* **Script hash:** `b'#\xba\'\x03\xc52c\xe8\xd6\xe5"\xdc2 39\xdc\xd8\xee\xe9'`

Wyjaśnienie:
* WIF - jest to klucz prywatny portfela
* Adres - adres publiczny portfela
* Script hash - zhashowany adres portfela - używany wewnątrz kontraktów w funkcji `CheckWitness`

## Otwarcie portfela

Będąc w konsoli `neo>` (po uruchomieniu neo-local):
* wpisz polecenie  
    `open wallet ./neo-privnet.wallet`
* Przebuduj portfel:  
    `wallet rebuild`
* wyświetl informacje o portfelu:  
    `wallet`
    
## Opłaty sieci - informacja

Deploy kontraktów do sieci wymaga wniesienia opłaty - wdrażasz kontrakt za pomocą adresu portfela, więc portfel musi zawierać odpowiednią ilość środków:
* **100 GAS** - za utworzenie kontraktu
* **+400 GAS** - za funkcjonalność dostępu do trwałego magazynu danych (storage)
* **+500 GAS** - za funkcjonalność dynamicznego wywoływania (dynamic call)  

Dodatkowo sieć pobiera opłaty za używnie funkcjonalności systemu w trakcie wykonywania kontraktu. Przy tym trzeba pamiętać, że jeśli suma opłat danej operacji będziemniejsza od **10 GAS**, to operacja ta wykoanana będzie za darmo.

>Pełna lista opłat: <http://docs.neo.org/en-us/sc/systemfees.html>

Prywatna sieć pobiera takie same opłaty, więc musimy posiadac portfel, który ma odpowiednio dużo GASu.

 #### [Kolejny krok - uruchomienie testowego kontraktu](test_contract.md) 
 