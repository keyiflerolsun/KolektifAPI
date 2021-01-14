# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, jsonify, request

from KekikSpatula import CocukMasallari

masal   = CocukMasallari()
kaynak  = masal.veri['kaynak']

@app.route('/masalGorsel')
def masal_gorsel():
    log_ver(request)

    return render_template(
        'veriSayfasi.html',
        veriler     = masal.veri['veri'],
        anahtarlar  = masal.anahtarlar,
        baslik      = f"«{kaynak}» Çocuk Masalları Verisi"
    )

@app.route('/masal')
def masal_json():
    log_ver(request)

    return jsonify(
        kaynak      = kaynak,
        saglayici   ='@keyiflerolsun',
        veri        = masal.veri['veri']
    )