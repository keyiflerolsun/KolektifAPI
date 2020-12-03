# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, jsonify, request

from KekikSpatula import BimAktuel

bim     = BimAktuel()
kaynak  = bim.veri['kaynak']

@app.route('/bimGorsel')
def bim_gorsel():
    log_ver(request)

    return render_template(
        'veriSayfasi.html',
        veriler     = bim.veri['veri'],
        anahtarlar  = bim.anahtarlar,
        baslik      = f"Bim Aktüel Verileri\n({bim.veri['tarih']})"
    )

@app.route('/bim')
def bim_json():
    log_ver(request)

    return jsonify(bim.veri)