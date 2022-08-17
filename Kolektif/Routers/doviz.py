# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app
from flask        import render_template, jsonify
from KekikSpatula import Doviz

@app.route("/dovizGorsel")
def doviz_gorsel():
    doviz = Doviz()

    return render_template(
        "veriSayfasi.html",
        veriler    = doviz.veri["veri"],
        anahtarlar = doviz.anahtarlar,
        baslik     = f"«{doviz.veri['kaynak']}» Güncel Döviz Verileri"
    )

@app.route("/doviz")
def doviz_json():
    doviz = Doviz()

    return jsonify(
        kaynak    = doviz.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = doviz.veri["veri"]
    )