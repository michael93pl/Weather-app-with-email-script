import requests
import sys
import email_script
import builtins

# MSG template used for looping options
msg_template = """
What Do You want to check exactly?\n
1. Weather in general\n
2. Tempreture\n
3. Wind\n
4. Cloudiness\n
5. Pressure\n
6. Send weather 
                """
# Template for input
msg_template_numbers = [1, 2, 3, 4, 5, 6]

#Checking input of user
def input_function():
    """loops until server response is not 200, input checker"""
    print(
        "\n\nHello! It's super awesome weather app, in which you can check weather for a certain city around the world"
        " and send it as email!\n")
    while True:

        builtins.city = input("Weather of which city you want to check ?\n").strip().lower()
        builtins.country = input("Please enter country code in format: United Kingdom = uk, Poland = pl\n").strip().lower()


        resp = requests.get(
            "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
        if resp.status_code != 200:
            print("Hey, you messed with the city or the country. Write correct city name and country in proper format")
            continue
        else:
            break

# func used in main func to come back
def options():
    """Allows user to choose other option --> comming back to 1-6 section"""
    while True:
        option = input("Do You want to check other aspect of the weather?\n").strip().lower()

        if option == "yes" or option == "y":
            return decision()
        elif option =="no" or option =="n":
            sys.exit("Well that would be it! Thanks for using my ap!")
        else:
            print("Hey mate, write yes or no")

#api funcitions
def call_api():
    """Calling api and returning json object for weather functions"""
    r = requests.get(
        "http://api.openweathermap.org/data/2.5/weather?q=" + city + "," + country + "&appid=8d502f878a7d8c7f485816a3e1ac68b6")
    json_object = r.json()
    return json_object


# Setting weather functions
def temp():
    """Temp function with conversion to C degree"""
    temp_k = (call_api()["main"]["temp"])
    temp_c = temp_k - 273.15
    return temp_c

def wind():
    """Wind function"""
    wind = str((call_api()["wind"]["speed"]))
    return wind

def cloud():
    """Cloud function"""
    cloud = (call_api()["weather"][0]["description"])
    return cloud

def pressure():
    """Pressure function"""
    pressure = (call_api()["main"]["pressure"])
    return pressure

def general():
    """Prints all aspects of the weather"""
    a = "Current tempreture is: {} C.\n".format(temp())
    b = "Current wind speed is: {} m/s\n".format(wind())
    c = "Current cloudiness is: {}\n".format(cloud())
    d = "Current pressure is: {} hpa\n".format(pressure())

    full = a + b + c + d
    return full

# main function
def decision():
    """Lets make user choose between 6 possibilities and force specific input"""
    while True:
        print(msg_template)
        choise = int(input())
        if choise not in msg_template_numbers:
            print("Hey, you can choose only 1-6")
            print(msg_template)
        else:
            break
    if choise == 1:
        print("Here is the general weather for {} in {}: \n".format(city, country))
        print(general())
        print(options())
    elif choise == 2:
        print("Current tempreture in {} is: {} C.".format(city, temp()))
        print(options())
    elif choise == 3:
        print("Current wind speed in {} is: {} m/s".format(city, wind()))
        print(options())
    elif choise == 4:
        print("Current cloudiness in {} is: {}".format(city, cloud()))
        print(options())
    elif choise ==5:
        print("Current pressure in {} is: {} hpa".format(city, pressure()))
        print(options())
    else:
        email_script.sending_email()

#output for the email script
def send():
    """Prints msg in email script"""
    a = "Current tempreture is: {} C.\n".format(temp())
    b = "Current wind speed is: {} m/s\n".format(wind())
    c = "Current cloudiness is: {}\n".format(cloud())
    d = "Current pressure is: {} hpa\n".format(pressure())

    full = a + b + c + d
    return full

if __name__ == "__main__":
    input_function()
    decision()






