from math import radians, sin, cos, sqrt, atan2
from datetime import datetime
import requests
import smtplib 

my_email = 'your_mail_here'
password = 'your_password_here'  # Replace with your actual password
frind_email = ['example_1@gmail.com','example_2@gmail.com']

# http://api.open-notify.org/iss-now.json

iss=requests.get(url='http://api.open-notify.org/iss-now.json').json()
iss_position=iss['iss_position']
iss_latitude=float(iss_position['latitude'])
iss_longitude=float(iss_position['longitude'])
print(f'iss_latitude: { iss_latitude } , iss_longitude: {iss_longitude}')

parameter={
    'lat':23.748268, # my latitude
    'lng':90.387938, # my longitute
    'formatted':0,   # time value format
}


# https://sunrise-sunset.org/api
response=requests.get(url="https://api.sunrise-sunset.org/json",params=parameter)

sunrise=response.json()['results']['sunrise']
sunset=response.json()['results']['sunset']
s1=sunrise.split('T')[1].split(':')[0]
s2=sunset.split('T')[1].split(':')[0]
print(s1[:5],s2[:5])

# Time
current_hour= datetime.now().hour
def see_in_night():
    if (current_hour>= int(s1[:2]) or current_hour <= int(s2[:2])):
        print("It's night time, you can see the ISS")
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for fnd_email in frind_email:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=fnd_email,
                    msg=f"Subject:Look Up!\n\nThe ISS is above you in the sky. \nLatitude: {iss_latitude}\nLongitude: {iss_longitude}\nYou can see the ISS now!"
                )
    else:
        print("It's day time, you can't see the ISS")
    

def haversine_distance(lat1, lon1, lat2, lon2):
    R = 6371  # Radius of Earth in km
    dlat = radians(lat2 - lat1)
    dlon = radians(lon2 - lon1)

    a = sin(dlat / 2)**2 + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    return R * c  # distance in kilometers

distance= haversine_distance(parameter['lat'], parameter['lng'], iss_latitude, iss_longitude)

# ISS can will be see in local latitude and longitute +5 or -5
if (parameter['lat']+5 >= iss_latitude >= parameter['lat']-5):
    if (parameter['lng']+5 >= iss_longitude >= parameter['lng']-5):
        print("You can see the ISS in your local area")
        see_in_night()
    else :
        print("It's cross the local Longitude area",iss_longitude)
        print("Your Longitude:",parameter['lng'])
        print("Distance:",distance)
else: 
    print("It's cross the local Latitude area",iss_latitude)
    print("Your Latitude:",parameter['lat'])
    print("Distance:",distance)




    