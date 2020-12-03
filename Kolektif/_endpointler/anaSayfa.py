# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, log_ver
from flask import render_template, request
import json

istekler = json.load(open("Kolektif/istekler.json", "r+", encoding='utf8'))

@app.route('/')
def ana_sayfa():
    log_ver(request)

    return render_template(
        'anaSayfa.html',
        veriler = istekler,
        baslik  = "Python / Flask ile yazılmış REST API"
    )