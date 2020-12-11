# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from KekikTaban import KekikTaban

taban = KekikTaban(
    baslik   = "@KekikAkademi Kolektif API",
    aciklama = "Kolektif API Başlatıldı..",
    banner   = "kolektif API",
    girinti  = 2
)

konsol = taban.konsol

def onemli(yazi):
   konsol.print(yazi, style="bold cyan")
def log_ver(istek):
    # konsol.log(f"[green]IP Bilgisi :[/] [bold red]{istek.environ.get('HTTP_X_REAL_IP', istek.remote_addr)}[/]  [blue]--[/]  [green]GET :[/] [bold yellow]{istek.host_url[:-1]}{istek.full_path}[/]", highlight=False)
    konsol.log(f"[bold red]{istek.environ.get('HTTP_X_REAL_IP', istek.remote_addr)}[/]  [blue]--[/] [bold yellow]{istek.full_path}[/]", highlight=False)

from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)

app.config['JSON_SORT_KEYS']                       = False
app.config['JSONIFY_PRETTYPRINT_REGULAR']          = True
app.config['JSON_AS_ASCII']                        = False
app.config['SITEMAP_INCLUDE_RULES_WITHOUT_PARAMS'] = True

ext = Sitemap(app=app)

from Kolektif._endpointler import anaSayfa, _hata, eczane, haber, udemy, deprem, akaryakit, hava, bim, doviz, ezan, google, trendyol, youtube
