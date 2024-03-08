from geopy.geocoders import Nominatim
import requests

headers = {

    "Api-Key": "service.d5bfe74756f8445b80e4697eb0c43c26"

}


def get_lat_lon_info(lat, lon):
    # # calling the nominatim tool
    # geoLoc = Nominatim(user_agent="GetLoc")
    #
    # # passing the coordinates
    # locname = geoLoc.reverse(f"{lat},{lon}")
    #
    # # printing the address/location name
    # print(locname.address)
    # return locname.address

    u = requests.get(f'https://api.neshan.org/v5/reverse?lat={lat}&lng={lon}', headers=headers)

    return u.json()
