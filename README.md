# Web-Scraping-Projesi

## Python dili request ve selenium modulleri ile hazırlamış olduğum web scraping çalışmam

Bu dosya içerisinde bulunan çalişma [Linkedin](https://tr.linkedin.com/) sitesinden bulunan mevcut iş ilanlarını almak için hazırlanmıştır. Kaynak kodları URL adresi olarak, Linkedin'da bulunan son 24 saat içerisinde işleme alınmış İstanbul adresli ilanları göstermektedir. [Python](https://www.python.org/) ile hazırladığım script, dinamik bir site üzerinde çalışcağından request ve [selenium](https://selenium-python.readthedocs.io/) modüllerini içermektedir. Ayrıca alınan verilerin işlenebilmesi için [BeautifulSoup](https://beautiful-soup-4.readthedocs.io/en/latest/) modülü kullanılmıştır. Selenium modülünün kullanılabilmesi için scriptin çalışacağı pc üzerinde, bir browser kurulu olup o browser ve işletim sisteminiz için bir browser drivere ihtiyaç duyulmaktadır. [chromedriver.exe](https://chromedriver.storage.googleapis.com/index.html?path=104.0.5112.29/) veya kullandığınız başka bir tarayıcı için driver dosyasının adresini indirme yaptıktan sonra:
```python
driver_path = "C:\\Users\\chromedriver.exe"
```
şeklinde ekleyiniz.