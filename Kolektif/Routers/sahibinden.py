# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app
from flask        import request, jsonify, abort
from KekikSpatula import Sahibinden

@app.route("/sahibinden")
def sahibinden_json_args():
    link = request.args.get("link")
    if not link:
        return abort(500)

    sahibinden = Sahibinden(link)

    return jsonify(
        kaynak    = sahibinden.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = sahibinden.veri["veri"]
    ) if sahibinden.veri else abort(404)