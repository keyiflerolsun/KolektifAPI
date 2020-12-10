# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import Doviz

from Kolektif import app, log_ver

doviz   = Doviz()
kaynak  = doviz.veri['kaynak']

@app.route('/dovizGorsel')
def doviz_gorsel():
    log_ver(request)

    return render_template(
        'veriSayfasi.html',
        veriler     = doviz.veri['veri'],
        anahtarlar  = doviz.anahtarlar,
        baslik      = f"«{kaynak}» Güncel Döviz Verileri"
    )

@app.route('/doviz')
def doviz_json():
    log_ver(request)

    return jsonify(
        kaynak      = kaynak,
        saglayici   = '@keyiflerolsun',
        veri        = doviz.veri['veri']
    )