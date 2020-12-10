# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from flask import jsonify, request
from KekikSpatula import KekikTube

from Kolektif import app, log_ver
from Kolektif._endpointler._hata import besYuz, dortYuzDort


@app.route('/youtube')
def youtube_json_args():
    log_ver(request)

    link = request.args.get('link')

    if not link:
        return besYuz('hata')

    youtube  = KekikTube(link)
    if not youtube.veri:
        return dortYuzDort('Hata')

    return jsonify(
        kaynak      = youtube.veri['kaynak'],
        saglayici   = '@keyiflerolsun',
        veri        = youtube.veri['veri']
    )