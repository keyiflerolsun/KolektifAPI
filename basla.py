# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from CLI      import konsol, cikis_yap, hata_yakala
from Kolektif import app
from os       import environ

port = int(environ.get("PORT", 1453))
host = "0.0.0.0"

if __name__ == "__main__":
    try:
        # app.run(debug=False, host=host, port=port)

        konsol.print(f"\nKolektifAPI [bold red]{host}[yellow]:[/]{port}[/]\'de başlatılmıştır...\n", style="bold cyan", width=70, justify="center")

        from waitress import serve
        serve(app, host=host, port=port)
        # serve(app, host=host, port=port, url_scheme="https")

        cikis_yap(False)
    except Exception as hata:
        hata_yakala(hata)