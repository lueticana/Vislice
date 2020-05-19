<!DOCTYPE html>

<html>

<body>

    <div>
        <img src='/img/{{igra.stevilo_napak()}}.jpg' />
    </div>
    <div>
        Pravilni del gesla:{{igra.pravilni_del_gesla()}}
    </div>
    <div>
        Nepravilne crke: {{igra.nepravilni_ugibi()}}
    </div>

    % if stanje == zmaga:
        <b>Zmagali ste!</b>
        <form action="/igra/" method="post">
            <button type="submit">Nova igra</button>
        </form>
    % elif stanje == poraz:
        <b>Izgubili ste! Pravilno geslo je bilo {{igra.geslo}}</b>
        <form action="/igra/" method="post">
            <button type="submit">Nova igra</button>
        </form>
    % else:
        <form method='post' action='/igra/{{id_igre}}/'>
            <input name='crka'> <input type='submit' value='Ugibaj!'>
        </form>
    % end






</body>

</html>