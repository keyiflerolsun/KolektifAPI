# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, jsonify
from KekikSpatula import Piiz

@app.route("/piizGorsel")
@cache.cached(timeout=6 * 60 * 60)
def piiz_gorsel():
    piiz = Piiz()

    return render_template(
        "veriSayfasi.html",
        veriler    = piiz.veri["veri"],
        anahtarlar = piiz.anahtarlar,
        baslik     = f"«{piiz.veri['kaynak']}» Güncel Alkol Fiyatları"
    )

@app.route("/piiz")
@cache.cached(timeout=6 * 60 * 60)
def piiz_json():
    piiz = Piiz()

    return jsonify(
        kaynak    = piiz.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = piiz.veri["veri"]
    )