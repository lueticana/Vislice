import bottle, model
DATOTEKA_S_STANJEM = 'tanje.json'

vislice = model.Vislice(DATOTEKA_S_STANJEM)

bottle.TEMPLATE_PATH.insert(0, 'views')

@bottle.get('/')
def index():
    return bottle.template('index')

@bottle.get('/img/<picture>')
def static_files(picture):
    return bottle.static_file(picture, 'img')

@bottle.post('/nova_igra/')
def nova_igra():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = vislice.nova_igra()
    vislice.zapisi_igre_v_datoteko()
    bottle.response.set_cookie('id_igre', id_igre, path='/', secret='VISLICE')
    bottle.redirect('/igra/')


@bottle.get('/igra/')
def pokazi_igro():
    vislice.nalozi_igre_iz_datoteke()
    id_igre = bottle.request.get_cookie('id_igre', secret='VISLICE')
    igra, stanje = vislice.igre[id_igre]
    return bottle.template('igra', igra=igra, stanje=stanje, id_igre=id_igre, zmaga=model.ZMAGA, poraz=model.PORAZ)

@bottle.post('/igra/<id_igre:int>/')
def ugibaj(id_igre):nalozi_igre_iz_datoteke()
    vislica.
    id_igre = bottle.request.get_cookie('id_igre', secret='VISLICE')

    crka = bottle.request.forms.crka

    vislice.ugibaj(id_igre, crka)
    vislice.zapisi_igre_v_datoteko()
    bottle.redirect(f'/igra/')





bottle.run(reloader=True, debug=True)