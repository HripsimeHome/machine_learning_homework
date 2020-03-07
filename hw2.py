# Classification example

person1 = {"skin": "white", "skull": "long-head", "eye-color": "blue"}
person2 = {"skin": "yellow", "skull": "short-head","eye-color": "black"}
person3 = {"skin": "black", "skull": "dolicephalic", "eye-color": "brown"}

def check_race(person):
    if person["skin"] == "white" and person["skull"] == "long-head" and person["eye-color"] == "blue":
        print("This is Caucasian race.")
    elif person["skin"] == "yellow" and person["skull"] == "short-head" and person["eye-color"] == "black":
        print("This is Mongoloid race.")
    elif person["skin"] == "black" and person["skull"] == "dolicephalic" and person["eye-color"] == "brown":
        print("This is Negroid race.")
    else:
        print("There is no such race.")

check_race(person1)
check_race(person2)
check_race(person3)


# Regression example

employee1 = {"performance": 90, "activity": 100, "position": "Developer"}
employee2 = {"performance": 60, "activity": 70, "position": "QA"}

def salary(employee):
    salary = employee["performance"]
    if employee["position"] == "Developer":
        salary += 10
    else:
        salary += 30
    print("The salary is: ", salary)

salary(employee1)
salary(employee2)


# Clusterization example

dress1 = {"style": "Classic", "Color": "Black"}
dress2 = {"style": "Casual", "Color": "Blue"}
dress3 = {"style": "Retro", "Color": "Grey"}

dress_list = [dress1, dress2, dress3]

def divide_groups(dresses):
    group1 = []
    group2 = []
    group3 = []
    for dress in dresses:
        if dress["style"] == "Classic":
            group1.append(dress)
            print("This is Group1: ", group1)
        elif dress["style"] == "Casual":
            group2.append(dress)
            print("This is Group2: ", group2)
        elif dress["style"] == "Retro":
            group3.append(dress)
            print("This is Group3: ", group3)
        else:
            print("There is no such group.")

divide_groups(dress_list)


# Web Scraping example

from googlesearch import search
import requests
URL = "https://www.ameriabank.am"
page_source = requests.get(URL)

from bs4 import BeautifulSoup
soup = BeautifulSoup(page_source.text, 'html.parser')

# Exchange Rates table from Ameria Bank
print(soup.find('table',  id="exchange").text)