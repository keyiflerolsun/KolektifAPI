# KolektifAPI
Flask Tabanlı KekikSpatula API

```python
{
  "udemy": [
    "/udemyGorsel?kategori=python",
    "/udemy?kategori=python",
    "/udemy/python"
  ],
  "hava":[
    "/havaGorsel?il=canakkale&ilce=merkez",
    "/hava?il=hatay&ilce=samandag",
    "/hava/mardin/nusaybin"
  ],
  "eczane": [
    "/eczaneGorsel?il=canakkale&ilce=merkez",
    "/eczane?il=hatay&ilce=samandag",
    "/eczane/mardin/nusaybin"
  ],
  "ezan": [
    "/ezanGorsel?il=canakkale",
    "/ezan?il=hatay",
    "/ezan/mardin"
  ],
  "google": [
    "/googleGorsel?ara=lorem impsum sit amet",
    "/google?ara=lorem impsum sit amet",
    "/google/lorem impsum sit amet"
  ],
  "youtube": [
    "",
    "/youtube?link=https://www.youtube.com/watch?v=1YlwjEQzMdU",
    ""
  ],
  "trendyol": [
    "",
    "/trendyol?link=https://www.trendyol.com/soly/meltblown-filtre-3-katli-tam-ultrasonik-cerrahi-maske-yesil-100-adet-p-47636885",
    ""
  ],
  "deprem":[
    "/depremGorsel",
    "/deprem",
    ""
  ],
  "akaryakit":[
    "/akaryakitGorsel",
    "/akaryakit",
    ""
  ],
  "haber": [
    "/haberGorsel",
    "/haber",
    ""
  ],
  "bim": [
    "/bimGorsel",
    "/bim",
    ""
  ],
  "doviz": [
    "/dovizGorsel",
    "/doviz",
    ""
  ]
}
```

## Proje Gelişimi

## v0.3
- **[KekikSpatula](https://github.com/keyiflerolsun/KekikSpatula)** __Entegrasyonu..__

### v0.2
- *Spatula*(_Scrape_) dosyaları oluşturulup, `Flask` tek dosya olarak oluşturuldu.
- `gunicorn` ile *Heroku* _Deploy_ edildi.

### v0.1
- Kod okunurluğunu arttırmak ve projenin geliştirilebilmesi için `Flask` ın el verdiği dosya/dizin sistemi oluşturuldu.
- `jinja2` iyileştirmeleri yapıldı ve dosya/dizin sistemi oluşturuldu.
- `gunicorn` ile *Heroku* _Deploy_ edildi.

### v0.0.3
- `flask_sitemap` kütüphanesi kullanılarak otomatik bir sitemap oluşturuldu.
- `jsonify` ile dönen sayfalara _favicon_ eklendi.
- _gunicorn_'un `app.config` konfigürasyonlarını yoksayması sorunları yüzünden `waitress` _serve_ kullanıldı.

### v0.0.1
- `rich` kütüphanesiyle Konsol Log sistemi eklenmiştir..
