# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app
from flask        import render_template, jsonify
from KekikSpatula import UcuzUcak

@app.route("/ucakGorsel")
def ucak_gorsel():
    ucak = UcuzUcak()

    return render_template(
        "veriSayfasi.html",
        veriler    = ucak.veri["veri"],
        anahtarlar = ucak.anahtarlar,
        baslik     = f"«{ucak.veri['kaynak']}» Ucuz Uçak Biletleri"
    )

@app.route("/ucak")
def ucak_json():
    ucak = UcuzUcak()

    return jsonify(
        kaynak    = ucak.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = ucak.veri["veri"]
    )