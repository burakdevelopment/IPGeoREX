import requests
import argparse

def get_ip_location(ip_address):
    url = f"http://ip-api.com/json/{ip_address}"
    response = requests.get(url)
    data = response.json()

    if data['status'] == 'success':
        print(f"IP: {data['query']}")
        print(f"Location: {data['city']}, {data['regionName']}, {data['country']}")
        print(f"Location Coordinates: Latitude {data['lat']}, Longitude {data['lon']}")
        print(f"Internet Service Provider: {data['isp']}")
    else:
        print("The IP location could not be found.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='wooserr')
    parser.add_argument('ip_address', type=str, help='IP adresi')
    args = parser.parse_args()

    ip_address = args.ip_address

    get_ip_location(ip_address)