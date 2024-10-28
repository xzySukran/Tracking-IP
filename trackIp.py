import requests
import re

# Fungsi untuk memverifikasi format IP menggunakan regex
def validate_ip(ip_address):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(ip_address) is not None

# Fungsi untuk mendapatkan GeoIP dari ipstack.com
def get_geoip_from_ipstack(ip_address, access_key):
    if not validate_ip(ip_address):
        print(f"IP Address tidak valid: {ip_address}")
        return

    try:
        response = requests.get(f"http://api.ipstack.com/{ip_address}?access_key={access_key}")
        data = response.json()

        if response.status_code == 200 and 'latitude' in data:
            print(f"\nIP Address: {data.get('ip', 'N/A')}")
            print(f"City: {data.get('city', 'N/A')}")
            print(f"Region: {data.get('region_name', 'N/A')}")
            print(f"Country: {data.get('country_name', 'N/A')}")
            print(f"Latitude: {data.get('latitude', 'N/A')}")
            print(f"Longitude: {data.get('longitude', 'N/A')}")
            print(f"Organization: {data.get('connection', {}).get('isp', 'N/A')}")
        else:
            print("Gagal mendapatkan data lokasi atau data tidak tersedia.")
    except requests.RequestException as e:
        print(f"Error querying IP information: {e}")

# Contoh penggunaan
ip_address = input("Masukkan IP Address target: ")
access_key = '63fc66ef5479e76f96588aef2aeef901'  # Ganti dengan API key Anda dari ipstack
get_geoip_from_ipstack(ip_address, access_key)

