# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import HavaDurumu

from Kolektif import app, log_ver
from Kolektif._endpointler._hata import besYuz, dortYuzDort


@app.route('/havaGorsel')
def hava_gorsel():
    log_ver(request)

    il      = request.args.get('il')
    ilce    = request.args.get('ilce')

    if not il or not ilce:
        return besYuz('Hata')

    hava = HavaDurumu(il, ilce)
    if not hava.veri:
        return dortYuzDort('Hata')

    return render_template(
        'veriSayfasi.html',
        veriler     = hava.veri['veri'],
        anahtarlar  = hava.anahtarlar,
        baslik      = f"«{hava.veri['kaynak']}» hava Verileri"
    )

@app.route('/hava')
def hava_json_args():
    log_ver(request)

    il      = request.args.get('il')
    ilce    = request.args.get('ilce')

    if not il or not ilce:
        return besYuz('Hata')

    hava = HavaDurumu(il, ilce)
    if not hava.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = hava.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = hava.veri['veri']
    )

@app.route('/hava/<il>/<ilce>')
def hava_json_dizin(il, ilce):
    log_ver(request)

    if not il or not ilce:
        return besYuz('Hata')

    hava = HavaDurumu(il, ilce)
    if not hava.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = hava.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = hava.veri['veri']
    )