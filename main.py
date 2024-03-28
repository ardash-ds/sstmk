import requests
import socket

import re
from bs4 import BeautifulSoup


def site_check(url: str) -> requests.Response:
    response = requests.get(f"https://{url}")
    if response.status_code == 200:
        print("Сайт работатет")
    else:
        print(f"Ошибка: {response.status_code}")
    return response

def get_ip(url: str):
    ip_address = socket.gethostbyname(url)
    print(f"IP addres: {ip_address}")


def number_search(response: requests.Response) -> int:
    soup = BeautifulSoup(response.content, 'html.parser')

    phone_number_div = soup.find('div', class_='phone-number')
    if phone_number_div:
        phone_number_a = phone_number_div.find('a', href=True)
        if phone_number_a:
            phone_number = phone_number_a.text.strip()
            print("Номер телефона:", phone_number)
            return phone_number
        else:
            print("Номер телефона не найден")
    else:
        print("Div с классом 'phone-number' не найден")
        

def number_check(pattern: str, number: str) -> None:
    phone_pattern = re.compile(pattern)
    check_number = phone_pattern.search(number)
    if check_number:
        print("Номер соответствует шаблону")
    else:
        print("Номер не соответствует шаблону")


def main():
    url = "sstmk.ru"
    pattern = '[+]?:{0,1}\d{0,1}\s{0,1}(\(\d{3}\)\s{0,1}\d{3}|\(\d{5}\)\d{1})-\d\d-\d\d'
    response = site_check(url)
    get_ip(url)
    number = number_search(response)
    if number:
        number_check(pattern, number)
    
    
if __name__ == '__main__':
    main()
    