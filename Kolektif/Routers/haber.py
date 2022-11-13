# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, jsonify
from KekikSpatula import SonDakika

@app.route("/haberGorsel")
@cache.cached(timeout=60 * 60)
def haber_gorsel():
    haber = SonDakika()

    return render_template(
        "haberSayfasi.html",
        veriler    = haber.veri["veri"],
        anahtarlar = ["Haber"],
        baslik     = f"«{haber.veri['kaynak']}» Son Dakika Verileri"
    )

@app.route("/haber")
@cache.cached(timeout=60 * 60)
def haber_json():
    haber = SonDakika()

    return jsonify(
        kaynak    = haber.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = haber.veri["veri"]
    )