# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, request, jsonify, abort
from KekikSpatula import Google

@app.route("/googleGorsel")
@cache.cached(timeout=6 * 60 * 60)
def google_gorsel():
    ara = request.args.get("ara")
    dil = request.args.get("dil")

    if not ara or not dil:
        return abort(500)

    google = Google(ara, dil)

    return render_template(
        "veriSayfasi.html",
        veriler    = google.veri["veri"],
        anahtarlar = google.anahtarlar,
        baslik     = f"«{google.veri['kaynak']}» google Verileri"
    ) if google.veri else abort(404)

@app.route("/google")
@cache.cached(timeout=6 * 60 * 60)
def google_json_args():
    ara = request.args.get("ara")
    dil = request.args.get("dil")

    if not ara or not dil:
        return abort(500)

    google = Google(ara, dil)

    return jsonify(
        kaynak    = google.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = google.veri["veri"]
    ) if google.veri else abort(404)

@app.route("/google/<ara>/<dil>")
@cache.cached(timeout=6 * 60 * 60)
def google_json_dizin(ara, dil):
    if not ara or not dil:
        return abort(500)

    google = Google(ara, dil)

    return jsonify(
        kaynak    = google.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = google.veri["veri"]
    ) if google.veri else abort(404)