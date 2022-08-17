# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, istekler
from flask    import make_response, jsonify, send_from_directory
import os

@app.get("/favicon.ico")
def favicon():
    return send_from_directory(directory=os.path.join(app.root_path, "static"), path="img/favicon.ico", mimetype="image/x-icon")

@app.errorhandler(404)
def dort_yuz_dort(error):
    return make_response(jsonify(KolektifAPI="Sayfa Bulunamadı..", istekler=istekler), 404)

@app.errorhandler(403)
def dort_yuz_uc(error):
    return make_response(jsonify(KolektifAPI="Bu Sayfaya Erişim İzniniz Yoktur..!", istekler=istekler), 403)

@app.errorhandler(410)
def dort_yuz_on(error):
    return make_response(jsonify(KolektifAPI="Sayfa Taşınmış Olabilir..", istekler=istekler), 410)

@app.errorhandler(500)
def bes_yuz(error):
    return make_response(jsonify(KolektifAPI="Düzgün Argüman Verilmedi.. » (Sunucu Hatası Oluştu!)", istekler=istekler), 500)