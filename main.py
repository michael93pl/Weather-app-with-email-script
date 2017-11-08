import requests
import sys

# MSG template used for looping options

MSG_TEMPLATE = """
What Do You want to check exactly?\n
1. Weather in general\n
2. Tempreture\n
3. Wind\n
4. Cloudiness\n
5. Pressure\n
6. Send weather 
                """

# Template for input
MSG_TEMPLATE_NUMBERS = [1, 2, 3, 4, 5, 6]

# Some general code with input about city and country

print("\n\nHello! It's super awesome weather app, in which you can check weather for a certain city around the world"
          " and send it as email!\n")

CITY = input("Weather of which city you want to check ?\n").strip().lower()
COUNTRY = input("Please enter country code in format: United Kingdom = uk, Poland = pl\n").strip().lower()

print(MSG_TEMPLATE)

# func used in main func to come back
def options():
    """Allows user to choose other option --> comming back to 1-6 section"""
    while True:
        OPTION = input("Do You want to check other aspect of the weather or send everything via email?\n").strip().lower()

        if OPTION == "yes" or OPTION == "y":
            return decision()
        elif OPTION =="no" or OPTION =="n":
            sys.exit("Well that would be it! Thanks for using my ap!")
        else:
            print("Hey mate, write yes or no")

# Setting class with functions for each answer
class Weather:
    """Ask if is there a reason to add Class here and how could u do it with classes? Also, how about decode 3 lines in each func"""


    def __init__(self, R):
        self.R = R = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")

    def temp(self):
        """Temp function with conversion to C degree"""

        JSON_OBJECT = self.R.json()
        TEMP_K = (JSON_OBJECT["main"]["temp"])
        TEMP_C = TEMP_K - 273.15
        return (TEMP_C)

    def wind():
        """Wind function"""

        R = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
        JSON_OBJECT = R.json()
        WIND = str((JSON_OBJECT["wind"]["speed"]))
        return WIND

    def cloud():
        """Cloud function --> ASKING WHY THE HELL 0 WORKS HERE!"""

        R = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
        JSON_OBJECT = R.json()
        CLOUD = (JSON_OBJECT["weather"][0]["description"])
        return CLOUD

    def pressure():
        """Pressure function"""

        R = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
        JSON_OBJECT = R.json()
        PRESSURE = (JSON_OBJECT["main"]["pressure"])
        return PRESSURE


# main function

def decision():
    """Lets make user choose between 6 possibilities and force specific input"""
    while True:
        CHOICE = int(input())
        if CHOICE not in MSG_TEMPLATE_NUMBERS:
            print("Hey, you can choose only 1-6")
            print(MSG_TEMPLATE)
        else:
            break
    if CHOICE == 1:
        print("Here is the general weather for {} in {}: ".format(CITY, COUNTRY))
        print(options())
    elif CHOICE == 2:
        print("Current tempreture in {} is: {} C.".format(CITY, Weather.temp()))
    elif CHOICE == 3:
        print("Current wind speed in {} is: {} m/s".format(CITY, Weather.wind()))
    elif CHOICE == 4:
        print("Current cloudiness in {} is: {}".format(CITY, Weather.cloud()))
    elif CHOICE ==5:
        print("Current pressure in {} is: {} hpa".format(CITY, Weather.pressure()))
    else:
        print("blablabla")

def something():
    resp = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")

    if resp.status_code !=200:
        raise Exception("GET / oauth/ {}".format(resp.status_code))
    else:
        pass



if __name__ == "__main__":
    decision()

    something()





