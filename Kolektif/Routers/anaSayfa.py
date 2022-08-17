# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import app, istekler
from flask    import render_template

@app.route("/")
def ana_sayfa():
    return render_template(
        "anaSayfa.html",
        veriler = istekler,
        baslik  = "Python / Flask ile yazılmış REST API"
    )