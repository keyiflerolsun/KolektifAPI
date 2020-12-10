# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import SonDepremler

from Kolektif import app, log_ver

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