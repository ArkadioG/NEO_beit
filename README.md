# NEO beIT

Materiały z prezentacji na konferencji beIT

## Przygotowanie do warsztatu

Aktualizacja: ***13-04-2018 11:30***

```text
Sprawdź na kilka dni przed warsztatem czy kroki dotyczące instalacji nie zostały zaktualizowane. W razie problemów z instalacją/przygotowaniem privnetu możesz zgłosić buga używając opcji w github.
```

* Wymagany system: Win/**Linux**/OSx
* Wymagana wersja Python: **3.6**  
  <https://www.python.org/downloads/>
* Zainstaluj i uruchom docker:  
  * Windows: <https://docs.docker.com/docker-for-windows/install/>  
  **UWAGA** musisz mieć zainstalowany HyperV, aby zainstalować Docker'a
  * Ubuntu/Mint: <https://docs.docker.com/install/linux/docker-ce/ubuntu/>  
  (wersje Debian/Fedora/CentOS - kliknij na powyższy odnośnik i przejdź do odpowiedniej opcji)
  * Mac: <https://docs.docker.com/docker-for-mac/install/>

* sprawdź czy docker jest uruchomiony <https://docs.docker.com/get-started/#test-docker-installation>
  * wpisz w terminalu/wierszu poleceń komendę: `docker --version`
  * możesz dodatkowo zainstalować testowy kontener:  
    wpisz komendę `docker run hello-world` - docker pobierze, zainstaluje i uruchomi testowy obraz
  * możesz wylistować obrazy: `docker image ls`
  * możesz wylistować kontenery: `docker container ls -a`  

* pobierz i zainstaluj obraz prywatnego blockchain NEO, ktorej użyjemy do testowego wdrażania naszych kontraktów.
  * pobierz obraz prywatnej sieci (privnet)  
  `docker pull metachris/neo-privnet-with-gas`

  * uruchom kontener z blockchainem NEO (polecenie jednolinijkowe!):  
  `docker run -d --name neo-privnet-with-gas -p 20333-20336:20333-20336/tcp -p 30333-30336:30333-30336/tcp metachris/neo-privnet-with-gas`

  * przetestuj czy Twój prywatny blockchain działa poprawnie:  
    * połącz się z kontenerem i uruchom w nim terminal:  
    `docker exec -it neo-privnet-with-gas /bin/bash`
    * będąc w kontenerze przejdź do folderu *opt/neo-python* i uruchom NEO Python CLI (Python'owy wiersz poleceń NEO):  
    `cd opt/neo-python`  
    `python3 prompt.py -p`
    * sprawdź czy kontener i blockchain działają poprawnie:  
    `block 0`
    * możesz wyjść z NEO Python CLI, wpisz:  
    `exit`
