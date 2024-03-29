# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, request, jsonify, abort
from KekikSpatula import DiscUdemy

@app.route("/udemyGorsel")
@cache.cached(query_string=True)
def udemy_gorsel():
    kategori = request.args.get("kategori")
    if not kategori:
        return abort(500)

    udemy = DiscUdemy(kategori)

    return render_template(
        "veriSayfasi.html",
        veriler    = udemy.veri["veri"],
        anahtarlar = udemy.anahtarlar,
        baslik     = f"«{udemy.veri['kaynak']}» {kategori} Udemy Kursları"
    ) if udemy.veri else abort(404)

@app.route("/udemy")
@cache.cached(query_string=True)
def udemy_json_args():
    kategori = request.args.get("kategori")
    if not kategori:
        return abort(500)

    udemy = DiscUdemy(kategori)

    return jsonify(
        kaynak    = udemy.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = udemy.veri["veri"]
    ) if udemy.veri else abort(404)

@app.route("/udemy/<kategori>")
@cache.cached(query_string=True)
def udemy_json_dizin(kategori):
    if not kategori:
        return abort(500)

    udemy = DiscUdemy(kategori)

    return jsonify(
        kaynak    = udemy.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = udemy.veri["veri"]
    ) if udemy.veri else abort(404)