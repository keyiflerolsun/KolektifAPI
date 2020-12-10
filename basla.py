# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Kolektif import onemli
from konsolTaban import KekikTaban

KekikTaban(
    baslik   = "@KekikAkademi Kolektif API",
    aciklama = "Kolektif API Başlatıldı..",
    banner   = "kolektif API",
    girinti  = 2
)

import os

from Kolektif import app

port = int(os.environ.get("PORT", 5000))
host = "0.0.0.0"

app.config['JSON_SORT_KEYS']                       = False
app.config['JSONIFY_PRETTYPRINT_REGULAR']          = True
app.config['JSON_AS_ASCII']                        = False
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True

if __name__ == '__main__':
    #app.run(debug = True, host = '0.0.0.0', port = port)

    onemli(f'\n\tKolektifAPI [bold red]{host}[yellow]:[/]{port}[/]\'de başlatılmıştır...\n')

    from waitress import serve
    serve(app, host = host, port = port)
