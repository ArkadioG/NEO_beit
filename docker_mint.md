# Instalacja Docker na Linux Mint 18.3

Oficjalna dokumentacja na stronie docker zawiera błędy, poniższe kroki pozwolą zainstalować Dockera oraz ustawią uprawnienia tak, że Twój użytkownik nie będzie musiał wołać `sudo` aby uruchomić polecenia Dockera.

1. wykonaj poniższe polecenia
    ```bash
    # zaimportuj klucz PGP
     
    sudo apt-key adv --keyserver hkp://p80.pool.sks-keyservers.net:80 \
    --recv-keys 58118E89F3A912897C070ADBF76221572C52609D
     
    # dodajemy oficjalne repozytorium docker do menadżera pakietów 
     
    sudo apt-add-repository 'deb https://apt.dockerproject.org/repo ubuntu-xenial main'
     
    # update bazy pakietów
     
    sudo apt update
    
    # instalacja wymaganych dependencji
     
    sudo apt install linux-image-generic linux-image-extra-virtual
     
    # Reboot
     
    sudo reboot
    
    # Instalacja Dockera
     
    sudo apt install docker-engine
    
    ```

1. Zmieniamy ustawienia aby używać dockera bez `sudo`  
    <https://docs.docker.com/install/linux/linux-postinstall/#manage-docker-as-a-non-root-user>
    ```bash
    sudo groupadd docker
    sudo usermod -aG docker $USER
    ```
    
    Teraz powinieneś móc używać docker bez sudo - sprawdź poleceniem `docker run hello-world`