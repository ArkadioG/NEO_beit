# Instalacja docker-compose na Linux

Wykonaj poniższe polecenia:

1. pobierz najnowszą wersję (jednolinijkowe polecenie)
`sudo curl -L https://github.com/docker/compose/releases/download/1.21.0/docker-compose-$(uname -s)-$(uname -m) -o /usr/local/bin/docker-compose`
1. zmień pozwolenia dla binarki:  
    `sudo chmod +x /usr/local/bin/docker-compose`
1. sprawdź poprawność instalacji:  
    `docker-compose --version`
