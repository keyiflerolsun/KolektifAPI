# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import NobetciEczane

from Kolektif import app, log_ver
from Kolektif._endpointler._hata import besYuz, dortYuzDort


@app.route('/eczaneGorsel')
def eczane_gorsel():
    log_ver(request)

    il      = request.args.get('il')
    ilce    = request.args.get('ilce')

    if not il or not ilce:
        return besYuz('Hata')

    eczane = NobetciEczane(il, ilce)
    if not eczane.veri:
        return dortYuzDort('Hata')

    return render_template(
        'veriSayfasi.html',
        veriler     = eczane.veri['veri'],
        anahtarlar  = eczane.anahtarlar,
        baslik      = f"«{eczane.veri['kaynak']}» Eczane Verileri"
    )

@app.route('/eczane')
def eczane_json_args():
    log_ver(request)

    il      = request.args.get('il')
    ilce    = request.args.get('ilce')

    if not il or not ilce:
        return besYuz('Hata')

    eczane = NobetciEczane(il, ilce)
    if not eczane.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = eczane.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = eczane.veri['veri']
    )

@app.route('/eczane/<il>/<ilce>')
def eczane_json_dizin(il, ilce):
    log_ver(request)

    if not il or not ilce:
        return besYuz('Hata')

    eczane = NobetciEczane(il, ilce)
    if not eczane.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = eczane.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = eczane.veri['veri']
    )