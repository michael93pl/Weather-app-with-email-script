import requests

# MSG template used for looping options

MSG_TEMPLATE = """
What Do You want to check exactly?\n
1. Weather in general\n
2. Tempreture\n
3. Precipitation\n
4. Wind\n
5. Cloudiness\n
6. Pressure\n
7. Send weather 
                """
# Template for input
MSG_TEMPLATE_NUMBERS = [1, 2, 3, 4, 5, 6, 7]

# Some general code with input about city and country

print("Hello! It's super awesome weather app, in which you can check weather for a certain city around the world"
          " and send it as email!")

CITY = input("Weather of which city you want to check ?\n").strip().lower()
COUNTRY = input("Please enter country code in format: United Kingdom = uk, Poland = pl\n").strip().lower()

print(MSG_TEMPLATE)

# Setting class with functions for each answer
class Weather:
    def __init__(self, temp, precip, wind, cloud, pressure):
        self.temp = temp
        self.precip = precip
        self.wind = wind
        self.cloud = cloud
        self.pressure = pressure

    def temp():
        R = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")

        JSON_OBJECT = R.json()
        TEMP_K = (JSON_OBJECT["main"]["temp"])

        TEMP_C = TEMP_K - 273.15
        return (TEMP_C)


# main function

def decision():
    """Lets make user choose between 7 possibilities and force specific input"""
    while True:
        CHOICE = int(input())
        if CHOICE not in MSG_TEMPLATE_NUMBERS:
            print("Hey, you can choose only 1-7")
            print(MSG_TEMPLATE)
        else:
            break
    if CHOICE == 1:
        print("Here is the general weather for {} in {}: ".format(CITY, COUNTRY))
    elif CHOICE == 2:
        print(" Current tempreture in {} is: {} C.".format(CITY, Weather.temp()))
    elif CHOICE == 3:
        print("Precipitation: ")
    elif CHOICE == 4:
        print("Wind: ")
    elif CHOICE == 5:
        print("Cloudiness: ")
    elif CHOICE ==6:
        print("Pressure: ")
    else:
        print("blablabla")

def something():
    resp = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")

    if resp.status_code !=200:
        raise Exception("GET / oauth/ {}".format(resp.status_code))
    else:
        print("Shit worked out!")
        print(resp.json())



if __name__ == "__main__":
    decision()

    something()





