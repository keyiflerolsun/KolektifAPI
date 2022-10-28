# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import request, jsonify, abort
from KekikSpatula import TrendyolUrun

@app.route("/trendyol_urun")
@cache.cached(timeout=6 * 60 * 60)
def trendyol_urun_json_args():
    link = request.args.get("link")
    if not link:
        return abort(500)

    trendyol_urun = TrendyolUrun(link)

    return jsonify(
        kaynak    = trendyol_urun.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = trendyol_urun.veri["veri"]
    ) if trendyol_urun.veri else abort(404)