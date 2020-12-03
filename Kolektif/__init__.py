# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from rich.console import Console

konsol = Console(log_path=False)

def hata(yazi):
   konsol.print(yazi, style="bold red")
def bilgi(yazi):
   konsol.print(yazi, style="blue")
def basarili(yazi):
   konsol.print(yazi, style="bold green")
def onemli(yazi):
   konsol.print(yazi, style="bold cyan")
def soru(soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def log_ver(istek):
    konsol.log(f"[green]IP Bilgisi :[/] [bold red]{istek.environ.get('HTTP_X_REAL_IP', istek.remote_addr)}[/]  [blue]--[/]  [green]GET :[/] [bold yellow]{istek.host_url[:-1]}{istek.full_path}[/]", highlight=False)


from flask import Flask
from flask_sitemap import Sitemap

app = Flask(__name__)
ext = Sitemap(app=app)

from Kolektif._endpointler import anaSayfa, _hata, eczane, haber, udemy, deprem, akaryakit, hava, bim, doviz
