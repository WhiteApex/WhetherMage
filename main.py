import json
import locale
import requests
from ipywidgets import widgets


#Версия без автополучения города через gps
# city_list= ['Москва', "Екатеринбург", "Санкт-Петербург", "Казань", "Иркутск"]
#
# def get_city() -> str:
#     print('Выберите ваш город:')
#     print(", ".join(city_list))
#     chouse = input()
#     return chouse


def get_api_info(city: str):
    key = '56ae6e21fc976169815b7ed53c3583a7'
    api = 'https://api.openweathermap.org/data/2.5/forecast?q=' + city + '&units=metric&lang=ru&appid=' + key

    try:
        res = requests.get(api)
        data = res.json()


        #print(data['forecast'][0]['description'])

        # print(data['main']['temp'])
        # print(data['main']['feels_like'])
        # print(data['main']['temp_min'])
        # print(data['main']['temp_max'])
        #
        # print(data['wind']['speed'])
        #
        # print(data['name'])

        # print(data['weather'][0]['description'])

        file_name = "data.json"

        # Запись словаря в файл
        with open(file_name, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

        for day in data['list']:
            print(f'Дата: {day['dt_txt']}')
            print(f'Температура: {day['main']['temp']}')
            print(f'Погода: {day['weather'][0]['description']}')

        print(data)

    except Exception as e:
        print('Exception:', e)


def get_location() -> str:
    try:
        ip_addr = requests.get('https://api.ipify.org').text
        url = f'http://ip-api.com/json/{ip_addr}'
        response = requests.get(url).json()
        return response['city']
    except Exception as e:
        print(e)
        return 'Ошибка'





if __name__ == '__main__':
    city = get_location()
    get_api_info(city)

# import requests
# s_city = "Petersburg,RU"
# city_id = 0
# appid = "56ae6e21fc976169815b7ed53c3583a7"
# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/find",
#                  params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
#     data = res.json()
#     cities = ["{} ({})".format(d['name'], d['sys']['country'])
#               for d in data['list']]
#     print("city:", cities)
#     city_id = data['list'][0]['id']
#     print('city_id=', city_id)
# except Exception as e:
#     print("Exception (find):", e)
#     pass