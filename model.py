import random
import json
STEVILO_DOVOLJENIH_NAPAK = 9
PRAVILNA_CRKA = '+'
PONOVLJENA_CRKA = 'o'
NAPACNA_CRKA = '-'
ZMAGA = 'W'
PORAZ = 'X'

ZACETEK = 'S'

class Igra:

    def __init__(self, geslo, crke=None):
        self.geslo = geslo
        if crke is None:
            self.crke = []
        else:
            self.crke = crke

    def napacne_crke(self):
        return [crka for crka in self.crke if crka not in self.geslo]

    def pravilne_crke(self):
        return [crka for crka in self.crke if crka in self.geslo]

    def stevilo_napak(self):
        return len(self.napacne_crke())

    def zmaga(self):
        for crka in self.geslo:
            if not crka in self.crke:
                return False
        return True

    def poraz(self):
        return self.stevilo_napak() > STEVILO_DOVOLJENIH_NAPAK

    def pravilni_del_gesla(self):
        delni = ''
        for crka in self.geslo:
            if crka in self.crke:
                delni += crka + ' '
            else:
                delni += '_ '
        return delni[:-1]

    def nepravilni_ugibi(self):
        return ' '.join(self.napacne_crke())

    def ugibaj(self, ugib):
        crka = ugib.upper()
        if crka in self.crke:
            return PONOVLJENA_CRKA
        else:
            self.crke.append(crka)
        if crka in self.geslo:
            if self.zmaga():
                return ZMAGA
            else:
                return PRAVILNA_CRKA
        else:
            if self.poraz():
                return PORAZ
            else:
                return NAPACNA_CRKA


def nova_igra():
    return Igra(random.choice(bazen_besed))


class Vislice:

    def __init__(self, datoteka_s_stanjem, datoteka_z_besedami='besede.txt'):
        self.igre = {}
        self.datoteka_s_stanjem = 'stanje.json'
        with open('besede.txt', 'r', encoding='utf-8') as f:
            bazen_besed = f.read().split('/n')

    def nalozi_igre_iz_datoteke(self):
        with open(self.datoteka_s_stanjem) as f:
            podatki = json.load(f)
        self.igre = {}
        for id_igre, igra in podatki.items():
            self.igre[int(id_igre)] = (
                Igra(igra['geslo'], igra['crke']),
                igra['stanje']
            ) 

    def zapisi_igre_v_datoteko(self):
        podatki = {}
        for id_igre, (igra, stanje) in self.igre.items():
            podatki[id_igre] = {'geslo': igra.geslo, 'crka' : igra.crka, 'stanje' : stanje}
        with open(self.datoteka_s_stanjem, 'w') as f:
            json.dump(podatki, f)


    def prost_id_igre(self):
        if self.igre.keys():
            return max(self.igre.keys()) + 1
        else:
            return 0

    def nova_igra(self):
        id_igre = self.prost_id_igre()
        igra = nova_igra()

        self.igre[id_igre] = (igra, ZACETEK)
        return id_igre

    def ugibaj(self, id_igre, crka):
        igra = self.igre[id_igre][0]
        novo_stanje = igra.ugibaj(crka)
        self.igre[id_igre] = (igra, novo_stanje)


