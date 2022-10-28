# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import render_template, request, jsonify, abort
from KekikSpatula import Ezan

@app.route("/ezanGorsel")
@cache.cached(timeout=6 * 60 * 60, query_string=True)
def ezan_gorsel():
    il = request.args.get("il")
    if not il:
        return abort(500)

    vakit = Ezan(il)

    return render_template(
        "veriSayfasi.html",
        veriler    = vakit.veri["veri"],
        anahtarlar = vakit.anahtarlar,
        baslik     = f"«{vakit.veri['kaynak']}» {il} Ezan Vakitleri"
    ) if vakit.veri else abort(404)

@app.route("/ezan")
@cache.cached(timeout=6 * 60 * 60, query_string=True)
def ezan_json_args():
    il = request.args.get("il")
    if not il:
        return abort(500)

    vakit = Ezan(il)

    return jsonify(
        kaynak    = vakit.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = vakit.veri["veri"]
    ) if vakit.veri else abort(404)

@app.route("/ezan/<il>")
@cache.cached(timeout=6 * 60 * 60, query_string=True)
def ezan_json_dizin(il):
    if not il:
        return abort(500)

    vakit = Ezan(il)

    return jsonify(
        kaynak    = vakit.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = vakit.veri["veri"]
    ) if vakit.veri else abort(404)