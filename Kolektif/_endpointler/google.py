# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, request, jsonify
from Kolektif._endpointler._hata import besYuz, dortYuzDort

from KekikSpatula import Google

@app.route('/googleGorsel')
def google_gorsel():
    log_ver(request)

    ara = request.args.get('ara')
    if not ara:
        return besYuz('Hata')

    google  = Google(ara)
    if not google.veri:
        return dortYuzDort('Hata')

    return render_template(
        'veriSayfasi.html',
        veriler     = google.veri['veri'],
        anahtarlar  = google.anahtarlar,
        baslik      = f"«{google.veri['kaynak']}» {ara} Google Sonuçları"
    )

@app.route('/google')
def google_json_args():
    log_ver(request)

    ara = request.args.get('ara')

    if not ara:
        return besYuz('hata')

    google  = Google(ara)
    if not google.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = google.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = google.veri['veri']
    )

@app.route('/google/<ara>')
def google_json_dizin(ara):
    log_ver(request)

    if not ara:
        return besYuz('hata')

    google  = Google(ara)
    if not google.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = google.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = google.veri['veri']
    )