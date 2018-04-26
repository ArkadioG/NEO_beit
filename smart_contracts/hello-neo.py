from boa.interop.Neo.Runtime import Log, Notify

def Main():
    # print działa jak Log()
    print('Hello Arek - print')
    # Log() służy do logowania/wyświetlenia komunikatu w event hub
    Log('Hello Arek - log')
    # Notify() wypisuje informacje w event hub, jest w stanie wypisać stan obiektów
    Notify('Hello Arek - notify')