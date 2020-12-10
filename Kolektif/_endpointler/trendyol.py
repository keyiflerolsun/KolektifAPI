# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, request
from KekikSpatula import TrendyolYorum

from Kolektif import app, log_ver
from Kolektif._endpointler._hata import besYuz, dortYuzDort


@app.route('/trendyol')
def trendyol_json_args():
    log_ver(request)

    link = request.args.get('link')

    if not link:
        return besYuz('hata')

    trendyol  = TrendyolYorum(link)
    if not trendyol.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = trendyol.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = trendyol.veri['veri']
    )