# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, jsonify, request

from KekikSpatula import UcuzUcak

ucak    = UcuzUcak()
kaynak  = ucak.veri['kaynak']

@app.route('/ucakGorsel')
def ucak_gorsel():
    log_ver(request)

    return render_template(
        'veriSayfasi.html',
        veriler     = ucak.veri['veri'],
        anahtarlar  = ucak.anahtarlar,
        baslik      = f"«{kaynak}» Ucuz Uçak Biletleri"
    )

@app.route('/ucak')
def ucak_json():
    log_ver(request)

    return jsonify(
        kaynak      = kaynak,
        saglayici   ='@keyiflerolsun',
        veri        = ucak.veri['veri']
    )