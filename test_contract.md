# Testowy kontrakt - sprawdzenie poprawności instalacji

W tym kroku uruchomimy istniejący kontrakt, tym samym upewnimy się, że cała instalacja jest poprawna oraz poznasz jaką ścieżkę będziesz wskazywać do plików kontraktów.

## Testowy deploy kontraktu

Wraz z neo-local jest dostępny jeden kontrakt, który możemy uruchomić aby sprawdzić działanie naszej prywatnej sieci oraz kompiatora (neo-boa - zainstalowany wraz z neo-python).

1.  będąc w konsoli `neo>` wpisz polecenie:  
    `build /smart-contracts/wake_up_neo.py test 07 05 True False main`

**GRATULACJE** Właśnie wdrożyłeś pierwszy kontrakt do swojego prywatnego blockchainu NEO.
    
## Lokalizacja kontraktu i ścieżki w neo-python

Kontrakt testowy uruchomiony powyżej znajduje się w folderze `<ścieżka do repo>/neo-local/smart-contracts`


## Przydatne linki

* Argumenty kontraktu i zwracane wartości  
    <https://neo-python.readthedocs.io/en/latest/data-types.html#contractparametertypes>
* neo-python dokumentacja:  
    <https://neo-python.readthedocs.io/en/latest/>
* neo-boa  
    
* neo-local
    <https://github.com/neoauth/neo-local>