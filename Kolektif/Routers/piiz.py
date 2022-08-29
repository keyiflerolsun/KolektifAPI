# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app
from flask        import render_template, jsonify
from KekikSpatula import Piiz

@app.route("/piizGorsel")
def piiz_gorsel():
    piiz = Piiz()

    return render_template(
        "veriSayfasi.html",
        veriler    = piiz.veri["veri"],
        anahtarlar = piiz.anahtarlar,
        baslik     = f"«{piiz.veri['kaynak']}» Güncel Alkol Fiyatları"
    )

@app.route("/piiz")
def piiz_json():
    piiz = Piiz()

    return jsonify(
        kaynak    = piiz.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = piiz.veri["veri"]
    )