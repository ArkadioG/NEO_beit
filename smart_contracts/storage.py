from boa.interop.Neo.Runtime import Log, Notify
from boa.interop.Neo.Storage import Get, Put, GetContext

# build /smart-contracts/storage.py test ff 07 True False

"""
Ten kontrakt pokazuje użycie trwałej pamięci (storage).
Storage działa na zasadzie słownika: klucz-wartość
"""

def Main():

    # pobieramy kontekst storage'u dla danego kontraktu
    # każdy kontrakt ma własny obszar storage
    context = GetContext()

    # klucz
    item_key = 'moj-klucz'

    # pobieramy wartość za pomocą klucza
    item_value = Get(context, item_key)

    msg = ['Wartosc odczytana ze storage:', item_value]
    Notify(msg)

    # w przypadku gdy para klucz-wartość nie są zapisane
    # próba pobrania wartości za pomocą nie istniejącego w storage klucza
    # zwróci wartość pustego ciągu bajtów b''
    if len(item_value) == 0:
        Notify('Klucz nie istnieje w storage, ustawiam wartosc na 1')
        item_value = 1

    else:
        Notify("Klucz juz jest w storage, zwiększam wartosc o 1.")
        item_value += 1

    # zapisanie wartości pod kluczem
    Put(context, item_key, item_value)

    msg = ["Nowa wartosc zapisana do storage:", item_value]
    Notify(msg)

    return item_value
