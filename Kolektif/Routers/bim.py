# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, jsonify
from KekikSpatula import BimAktuel

@app.route("/bimGorsel")
@cache.cached(timeout=6 * 60 * 60)
def bim_gorsel():
    bim = BimAktuel()

    return render_template(
        "veriSayfasi.html",
        veriler    = bim.veri["veri"],
        anahtarlar = bim.anahtarlar,
        baslik     = f"Bim Aktüel Verileri\n({bim.veri['tarih']})"
    )

@app.route("/bim")
@cache.cached(timeout=6 * 60 * 60)
def bim_json():
    bim = BimAktuel()

    return jsonify(bim.veri)