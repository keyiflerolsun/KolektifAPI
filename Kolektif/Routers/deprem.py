# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, jsonify
from KekikSpatula import SonDepremler

@app.route("/depremGorsel")
@cache.cached(timeout=60)
def deprem_gorsel():
    deprem = SonDepremler()

    return render_template(
        "veriSayfasi.html",
        veriler    = deprem.veri["veri"],
        anahtarlar = deprem.anahtarlar,
        baslik     = f"«{deprem.veri['kaynak']}» Son Depremler Verisi"
    )

@app.route("/deprem")
@cache.cached(timeout=60)
def deprem_json():
    deprem = SonDepremler()

    return jsonify(
        kaynak    = deprem.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = deprem.veri["veri"]
    )