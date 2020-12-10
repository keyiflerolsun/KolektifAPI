# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import Akaryakit

from Kolektif import app, log_ver

akaryakit   = Akaryakit()
kaynak      = akaryakit.veri['kaynak']

@app.route('/akaryakitGorsel')
def akaryakit_gorsel():
    log_ver(request)

    return render_template(
        'veriSayfasi.html',
        veriler     = akaryakit.veri['veri'],
        anahtarlar  = akaryakit.anahtarlar,
        baslik      = f"«{kaynak}» Güncel Akaryakıt Verileri"
    )

@app.route('/akaryakit')
def akaryakit_json():
    log_ver(request)

    return jsonify(
        kaynak      = kaynak,
        saglayici   = '@keyiflerolsun',
        veri        = akaryakit.veri['veri']
    )