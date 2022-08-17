# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app
from flask        import render_template, request, jsonify, abort
from KekikSpatula import NobetciEczane

@app.route("/eczaneGorsel")
def eczane_gorsel():
    il   = request.args.get("il")
    ilce = request.args.get("ilce")

    if not il or not ilce:
        return abort(500)

    eczane = NobetciEczane(il, ilce)

    return render_template(
        "veriSayfasi.html",
        veriler    = eczane.veri["veri"],
        anahtarlar = eczane.anahtarlar,
        baslik     = f"«{eczane.veri['kaynak']}» Eczane Verileri"
    ) if eczane.veri else abort(404)

@app.route("/eczane")
def eczane_json_args():
    il   = request.args.get("il")
    ilce = request.args.get("ilce")

    if not il or not ilce:
        return abort(500)

    eczane = NobetciEczane(il, ilce)

    return jsonify(
        kaynak    = eczane.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = eczane.veri["veri"]
    ) if eczane.veri else abort(404)

@app.route("/eczane/<il>/<ilce>")
def eczane_json_dizin(il, ilce):
    if not il or not ilce:
        return abort(500)

    eczane = NobetciEczane(il, ilce)

    return jsonify(
        kaynak    = eczane.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = eczane.veri["veri"]
    ) if eczane.veri else abort(404)