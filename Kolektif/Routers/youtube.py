# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif     import app, cache
from flask        import request, jsonify, abort
from KekikSpatula import KekikTube

@app.route("/youtube")
@cache.cached(timeout=6 * 60 * 60, query_string=True)
def youtube_json_args():
    link = request.args.get("link")
    if not link:
        return abort(500)

    youtube = KekikTube(link)

    return jsonify(
        kaynak    = youtube.veri["kaynak"],
        saglayici = "@keyiflerolsun",
        veri      = youtube.veri["veri"]
    ) if youtube.veri else abort(500)