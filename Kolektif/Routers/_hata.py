# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, istekler, cache
from flask    import make_response, jsonify, send_from_directory
from os       import path

@app.route("/favicon.ico", methods=["GET"])
@cache.cached(timeout=60 * 60)
def favicon():
    try:
        return send_from_directory(directory=path.join(app.root_path, "static"), filename="favicon.ico", mimetype="image/x-icon")
    except TypeError:
        return send_from_directory(directory=path.join(app.root_path, "static"), path="favicon.ico", mimetype="image/x-icon")

@app.errorhandler(404)
@cache.cached(timeout=60 * 60)
def dort_yuz_dort(error):
    return make_response(jsonify(KolektifAPI="Sayfa Bulunamadı..", istekler=istekler), 404)

@app.errorhandler(403)
@cache.cached(timeout=60 * 60)
def dort_yuz_uc(error):
    return make_response(jsonify(KolektifAPI="Bu Sayfaya Erişim İzniniz Yoktur..!", istekler=istekler), 403)

@app.errorhandler(410)
@cache.cached(timeout=60 * 60)
def dort_yuz_on(error):
    return make_response(jsonify(KolektifAPI="Sayfa Taşınmış Olabilir..", istekler=istekler), 410)

@app.errorhandler(500)
@cache.cached(timeout=60 * 60)
def bes_yuz(error):
    return make_response(jsonify(KolektifAPI="Düzgün Argüman Verilmedi.. » (Sunucu Hatası Oluştu!)", istekler=istekler), 500)