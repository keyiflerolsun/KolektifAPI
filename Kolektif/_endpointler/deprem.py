# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, jsonify, request

from KekikSpatula import SonDepremler

deprem   = SonDepremler()
kaynak   = deprem.veri['kaynak']

@app.route('/depremGorsel')
def deprem_gorsel():
    log_ver(request)

    return render_template(
        'veriSayfasi.html',
        veriler     = deprem.veri['veri'],
        anahtarlar  = deprem.anahtarlar,
        baslik      = f"«{kaynak}» Son Depremler Verisi"
    )

@app.route('/deprem')
def deprem_json():
    log_ver(request)

    return jsonify(
        kaynak      = kaynak,
        saglayici   ='@keyiflerolsun',
        veri        = deprem.veri['veri']
    )