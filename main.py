import requests
import sys
import email_script
import builtins

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

#Checking input of user
def input_function():
    """loops until server response is not 200, input checker"""
    print(
        "\n\nHello! It's super awesome weather app, in which you can check weather for a certain city around the world"
        " and send it as email!\n")
    while True:

        builtins.CITY = input("Weather of which city you want to check ?\n").strip().lower()
        builtins.COUNTRY = input("Please enter country code in format: United Kingdom = uk, Poland = pl\n").strip().lower()

        resp = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
        if resp.status_code != 200:
            print("Hey, you messed with the city or the country. Write correct city name and country in proper format")
            continue
        else:
            break

# func used in main func to come back
def options():
    """Allows user to choose other option --> comming back to 1-6 section"""
    while True:
        OPTION = input("Do You want to check other aspect of the weather?\n").strip().lower()

        if OPTION == "yes" or OPTION == "y":
            return decision()
        elif OPTION =="no" or OPTION =="n":
            sys.exit("Well that would be it! Thanks for using my ap!")
        else:
            print("Hey mate, write yes or no")

# Setting weather functions
def temp():
    """Temp function with conversion to C degree"""
    R = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + CITY + "," + COUNTRY + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
    JSON_OBJECT = R.json()
    TEMP_K = (JSON_OBJECT["main"]["temp"])
    TEMP_C = TEMP_K - 273.15
    return TEMP_C

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

def general():
    """Prints all aspects of the weather"""
    A = "Current tempreture is: {} C.\n".format(temp())
    B = "Current wind speed is: {} m/s\n".format(wind())
    C = "Current cloudiness is: {}\n".format(cloud())
    D = "Current pressure is: {} hpa\n".format(pressure())

    FULL = A + B + C + D
    return FULL

# main function
def decision():
    """Lets make user choose between 6 possibilities and force specific input"""
    while True:
        print(MSG_TEMPLATE)
        CHOICE = int(input())
        if CHOICE not in MSG_TEMPLATE_NUMBERS:
            print("Hey, you can choose only 1-6")
            print(MSG_TEMPLATE)
        else:
            break
    if CHOICE == 1:
        print("Here is the general weather for {} in {}: \n".format(CITY, COUNTRY))
        print(general())
        print(options())
    elif CHOICE == 2:
        print("Current tempreture in {} is: {} C.".format(CITY, temp()))
        print(options())
    elif CHOICE == 3:
        print("Current wind speed in {} is: {} m/s".format(CITY, wind()))
        print(options())
    elif CHOICE == 4:
        print("Current cloudiness in {} is: {}".format(CITY, cloud()))
        print(options())
    elif CHOICE ==5:
        print("Current pressure in {} is: {} hpa".format(CITY, pressure()))
        print(options())
    else:
        email_script.sending_email()

#output for the email script
def send():
    """Prints msg in email script"""
    A = "Current tempreture is: {} C.\n".format(temp())
    B = "Current wind speed is: {} m/s\n".format(wind())
    C = "Current cloudiness is: {}\n".format(cloud())
    D = "Current pressure is: {} hpa\n".format(pressure())

    FULL = A + B + C + D
    return FULL

if __name__ == "__main__":
    input_function()
    decision()






