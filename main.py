from selenium import webdriver
from bs4 import BeautifulSoup

browserProfile = webdriver.ChromeOptions()
browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'})
browser = webdriver.Chrome('chromedriver', chrome_options=browserProfile)

il = input("İl: ").lower().capitalize()
ilce = input("İlçe: ").lower().capitalize()
url = browser.get(f"https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il={il}&ilce={ilce}")

kaynak = browser.page_source
soup = BeautifulSoup(kaynak, "html.parser")

anlikDurumTarih = soup.find("span",{"class":"ad_time ng-binding"})
anlikDerece = soup.find("div", {"class":"anlik-sicaklik-deger ng-binding"})
anlikHava = soup.find("div", {"class":"anlik-sicaklik-havadurumu-ikonismi ng-binding"})
anlikNem = soup.find("div", {"class":"anlik-nem-deger-kac ng-binding"})

print(f"""
İl: {il}/{ilce}
Tarih: {anlikDurumTarih.text}
Sıcaklık: {anlikDerece.text}°C
Hava: {anlikHava.text}
Nem: %{anlikNem.text}
""")