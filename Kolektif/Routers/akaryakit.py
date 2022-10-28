# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, jsonify
from KekikSpatula import Akaryakit

@app.route("/akaryakitGorsel")
@cache.cached(timeout=6 * 60 * 60)
def akaryakit_gorsel():
    akaryakit = Akaryakit()

    return render_template(
        "veriSayfasi.html",
        veriler    = akaryakit.veri["veri"],
        anahtarlar = akaryakit.anahtarlar,
        baslik     = f"«{akaryakit.veri['kaynak']}» Güncel Akaryakıt Verileri"
    )

@app.route("/akaryakit")
@cache.cached(timeout=6 * 60 * 60)
def akaryakit_json():
    akaryakit = Akaryakit()

    return jsonify(
        kaynak    = akaryakit.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = akaryakit.veri["veri"]
    )