from boa.interop.Neo.Runtime import Log, Notify

# testowy deploy kontraktu:
# build /smart-contracts/notify2.py test 05 05 False False main

def Main():

    # lista zawierająca różne typy
    msg = ["a", 1, 2, b"3"]

    # Log() nie jest w stanie wypisać obiektu, poradzi sobie tylko z tablicą bajtów
    # odkomentuj poniższe instrukcje - po wywołaniu kontraktu zobaczysz błędy
    # spowodowane przez Log()

    # print(msg)
    # Log(msg)

    # Notify wypisze zawartość obiektu bez problemu
    Notify(msg)

    