# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, render_template, request
from KekikSpatula import DiscUdemy

from Kolektif import app, log_ver
from Kolektif._endpointler._hata import besYuz, dortYuzDort


@app.route('/udemyGorsel')
def udemy_gorsel():
    log_ver(request)

    kategori = request.args.get('kategori')
    if not kategori:
        return besYuz('Hata')

    udemy  = DiscUdemy(kategori)
    if not udemy.veri:
        return dortYuzDort('Hata')

    return render_template(
        'veriSayfasi.html',
        veriler     = udemy.veri['veri'],
        anahtarlar  = udemy.anahtarlar,
        baslik      = f"«{udemy.veri['kaynak']}» {kategori} Udemy Kursları"
    )

@app.route('/udemy')
def udemy_json_args():
    log_ver(request)

    kategori = request.args.get('kategori')

    if not kategori:
        return besYuz('hata')

    udemy  = DiscUdemy(kategori)
    if not udemy.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = udemy.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = udemy.veri['veri']
    )

@app.route('/udemy/<kategori>')
def udemy_json_dizin(kategori):
    log_ver(request)

    if not kategori:
        return besYuz('hata')

    udemy  = DiscUdemy(kategori)
    if not udemy.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = udemy.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = udemy.veri['veri']
    )