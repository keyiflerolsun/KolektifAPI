# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import json
import os

from flask import jsonify, make_response, send_from_directory

from Kolektif import app

istekler = json.load(open("Kolektif/istekler.json", "r+", encoding='utf8'))

@app.route('/favicon.ico', methods=['GET'])
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), filename='img/favicon.ico', mimetype='image/x-icon')

@app.errorhandler(404)
def dortYuzDort(error):
    return make_response(jsonify(KolektifAPI='İstediğin Şeyi Bulamadım..', istekler=istekler), 404)

@app.errorhandler(500)
def besYuz(error):
    return make_response(jsonify(KolektifAPI='Düzgün Argüman Verilmedi..', istekler=istekler), 500)