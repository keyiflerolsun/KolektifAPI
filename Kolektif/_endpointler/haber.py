# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import SonDakika

from Kolektif import app, log_ver

haber   = SonDakika()
kaynak  = haber.veri['kaynak']

@app.route('/haberGorsel')
def haber_gorsel():
    log_ver(request)

    return render_template(
        'haberSayfasi.html',
        veriler     = haber.veri['veri'],
        anahtarlar  = ['Haber'],
        baslik      = f"«{kaynak}» Son Dakika Verileri"
    )

@app.route('/haber')
def haber_json():
    log_ver(request)

    return jsonify(
        kaynak      = kaynak,
        saglayici   = '@keyiflerolsun',
        veri        = haber.veri['veri']
    )