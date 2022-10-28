# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import request, jsonify, abort
from KekikSpatula import TrendyolKategori

@app.route("/trendyol_kategori")
@cache.cached(timeout=6 * 60 * 60)
def trendyol_kategori_json_args():
    kategori_adi = request.args.get("kategori_adi")
    sayfa_sayisi = request.args.get("sayfa_sayisi")

    if not kategori_adi or not sayfa_sayisi or not sayfa_sayisi.isdigit():
        return abort(500)

    trendyol_kategori = TrendyolKategori(kategori_adi, int(sayfa_sayisi))

    return jsonify(
        kaynak    = trendyol_kategori.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = trendyol_kategori.veri["veri"]
    ) if trendyol_kategori.veri else abort(404)