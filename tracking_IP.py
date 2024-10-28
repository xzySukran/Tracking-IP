import requests
import re

G = '\033[32m'  
C = '\033[36m'  
Y = '\033[33m'  
R = '\033[31m'  
M = '\033[35m'  
B = '\033[34m'  
W = '\033[0m'   

hand_ascii = f"""
{Y} _______                _     _                {B}  _____ _____  
{Y}|__   __|          ____  | | (_)        ____   {B} |_   _|  __ \ 
{Y}   | |  __ _ _ __/  __ | | ___  _ __   / () |  {B}   | | | |__) |
{G}   | |/  _` | '__| |   | |/ /  | '_ \  \ __ |  {M}   | | |  ___/ 
{G}   | |  (_| | |  | |__ |   < | | | | |    | |  {M}  _| |_| |  
{R}   |_|\ __,_|_|  \ __,_|_|\ _\ |_| |_|  __| |  {C} |_____|__| 
                                      {R}/ ___ |  {Y}↘
                                                {R}©Razor{C}Xzy
                                            {W}
"""

def validate_ip(ip_address):
    ip_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")
    return ip_pattern.match(ip_address) is not None

def get_geoip(ip_address):
    if not validate_ip(ip_address):
        print(f"{Y}Invalid IP Address: {ip_address}{W}")
        return

    try:
        response = requests.get(f"https://ipinfo.io/{ip_address}/json")
        data = response.json()

        if 'bogon' in data:
            print(f"{Y}{ip_address} is a bogon IP (reserved or invalid).{W}")
        else:
            print(f"\n{C}IP Address: {W}{data.get('ip', 'N/A')}")
            print(f"{C}Hostname: {W}{data.get('hostname', 'N/A')}")
            print(f"{C}City: {W}{data.get('city', 'N/A')}")
            print(f"{C}Region: {W}{data.get('region', 'N/A')}")
            print(f"{C}Country: {W}{data.get('country', 'N/A')}")

            loc = data.get('loc', 'N/A')
            if loc != 'N/A':
                try:
                    latitude, longitude = map(float, loc.split(','))
                    # Print formatted coordinates
                    print(f"{C}Latitude: {W}{latitude:.6f}")
                    print(f"{C}Longitude: {W}{longitude:.6f}")
                    
                    google_maps_link = f"https://www.google.com/maps?q={latitude:.6f},{longitude:.6f}"
                    print(f"{C}Google Maps Link: {W}{google_maps_link}")
                except ValueError:
                    print(f"{R}Error processing latitude and longitude values.{W}")
            else:
                print(f"{C}Location (lat/long): {W}{loc}")

            print(f"{C}Organization: {W}{data.get('org', 'N/A')}")
            print(f"{C}Postal Code: {W}{data.get('postal', 'N/A')}")
            print(f"{C}Timezone: {W}{data.get('timezone', 'N/A')}")

            # Additional info
            print(f"\n{Y}| ©OwnerCode by RaorXzy")
            print(f"   ↳ github : https://github.com/muhammadsukran")
            print(f"      ↳ M.SU{W}")

    except requests.RequestException as e:
        print(f"{Y}Error querying IP information: {e}{W}")

print(hand_ascii)

ip_address = input(f"{Y}Public IP Address: {W}")

get_geoip(ip_address)

