import requests

WP_URL = "http://wordpress/wp-json/wp/v2/posts/1"
WP_USER = "admin"
WP_PASS = "rcCVBAVJXd5dDXTe8JxQnLmc"

data = {
    "title": "Merhaba ben Mehmet Öğüt!",
    "content": "BTS Group tarafından verilmiş olan MentalArts Case Study tasklarını bir python betiği ile düzenlemeye dayanan bir test yazısıdır burda yazan yazıyı değiştirmek için app.py dosyası içerisinde bulundan content kısmında değişiklik yaptıktan sonra startup.sh dosyasını çalıştırmanız yeterli olucaktır !",
    "status": "publish"
}

response = requests.post(WP_URL, json=data, auth=(WP_USER, WP_PASS))

if response.status_code == 200:
    print("[✔] WordPress yazısı başarıyla güncellendi.")
else:
    print("[✘] Hata oluştu:", response.json())
