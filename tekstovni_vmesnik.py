import model

def izpis_igre(igra):
    tekst = (
        'Stevilo preostalih poskusov: {stevilo_preostalih_poskusov} \n\n'
        '{pravilni_del_gesla} \n\n'
        'Neuspeli poskusi: {neuspeli_poskusi} \n\n'
    
    ).format(
        stevilo_preostalih_poskusov = model.STEVILO_DOVOLJENIH_NAPAK - igra.stevilo_napak() + 1,
        pravilni_del_gesla = igra.pravilni_del_gesla(),
        neuspeli_poskusi = igra.nepravilni_ugibi()
    )

    return tekst

def izpis_zmage(igra):
    tekst = (
        'Jupiiiiii, zmaga! Geslo je bilo: {geslo}'
    ).format(
        geslo = igra.pravilni_del_gesla()
    )
    return tekst


def izpis_poraza(igra):
    tekst = (
        'Buuu, poraz! Geslo je bilo: {geslo}'
    ).format(
        geslo = igra.geslo
    )
    return tekst

def zahtevaj_vnos():
    return input('Crka: ')

def pozeni_vmesnik():

    igra = model.nova_igra()

    while True:
        print(izpis_igre(igra))
        poskus = zahtevaj_vnos()
        igra.ugibaj(poskus)
        if igra.zmaga():
            print(izpis_zmage(igra))
            break
        elif igra.poraz():
            print(izpis_poraza(igra))
            break
    return

pozeni_vmesnik()