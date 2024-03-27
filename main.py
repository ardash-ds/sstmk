import requests
import socket
import re
from bs4 import BeautifulSoup


url = "sstmk.ru"
# url = "sstmk.ru"
response = requests.get(f"https://{url}")
if response.status_code == 200:
    print("The site is working")
else:
    print(f"Error, status code: {response.status_code}")


ip_address = socket.gethostbyname(url)
print(f"IP addres: {ip_address}")

soup = BeautifulSoup(response.content, 'html.parser')

phone_number_div = soup.find('div', class_='phone-number')
if phone_number_div:
    phone_number_a = phone_number_div.find('a', href=True)
    if phone_number_a:
        phone_number = phone_number_a.text.strip()
        print("Номер телефона:", phone_number)
    else:
        print("Номер телефона не найден")
else:
    print("Div с классом 'phone-number' не найден")

# text = "Телефон: 8 (495) 946-80-48, Мобильный: 8(916)123-45-67"

phone_pattern = re.compile(r'\b[+]?\d{0,3}\s?\((\d{3})\)\s?(\d{3})-(\d{2})-(\d{2})\d\b')
phone_number = phone_pattern.search(phone_number)
print(phone_number)

if phone_number:
    print("Соответствует")
else:
    print("Не соответствует")


# soup = BeautifulSoup(response.content, 'html.parser')
# phone_elements = soup.find_all(phone_pattern)
# phone_elements = soup.find_all(string=phone_pattern)
# print(phone_numbers)

