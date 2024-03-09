from geopy.geocoders import Nominatim
import requests
import geopy.distance

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


# coords_1 = (52.2296756, 21.0122287)
# coords_2 = (52.406374, 16.9251681)
def trip_cost_baxi(pickup, dropoff):
    print("pickup ", pickup[0])
    print("dropoff ", dropoff[0])
    km = geopy.distance.geodesic(pickup[0], dropoff[0]).km
    print(km)
    return km * 10000


def trip_cost_heavy(pickup, dropoff):
    print("pickup ", pickup[0])
    print("dropoff ", dropoff[0])
    km = geopy.distance.geodesic(pickup[0], dropoff[0]).km
    print(km)
    return km * 20000

def trip_cost_light(pickup, dropoff):
    print("pickup ", pickup[0])
    print("dropoff ", dropoff[0])
    km = geopy.distance.geodesic(pickup[0], dropoff[0]).km
    print(km)
    return km * 80000
