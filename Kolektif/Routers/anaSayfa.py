# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, istekler, cache
from flask    import render_template

@app.route("/")
@cache.cached(timeout=60 * 60)
def ana_sayfa():
    return render_template(
        "anaSayfa.html",
        veriler = istekler,
        baslik  = "Python / Flask ile yazılmış REST API"
    )