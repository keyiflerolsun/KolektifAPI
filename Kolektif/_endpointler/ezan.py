# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz, dortYuzDort

from KekikSpatula import Ezan

@app.route('/ezanGorsel')
def ezan_gorsel():
    log_ver(request)

    il = request.args.get('il')
    if not il:
        return besYuz('Hata')

    vakit  = Ezan(il)
    if not vakit.veri:
        return dortYuzDort('Hata')

    return render_template(
        'veriSayfasi.html',
        veriler     = vakit.veri['veri'],
        anahtarlar  = vakit.anahtarlar,
        baslik      = f"«{vakit.veri['kaynak']}» {il} vakit Kursları"
    )

@app.route('/ezan')
def ezan_json_args():
    log_ver(request)

    il = request.args.get('il')

    if not il:
        return besYuz('hata')

    vakit  = Ezan(il)
    if not vakit.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = vakit.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = vakit.veri['veri']
    )

@app.route('/ezan/<il>')
def ezan_json_dizin(il):
    log_ver(request)

    if not il:
        return besYuz('hata')

    vakit  = Ezan(il)
    if not vakit.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = vakit.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = vakit.veri['veri']
    )