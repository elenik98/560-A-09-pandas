# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau", "High", "Ryan", "Trimble", "Wojcik", "Washington", "Lebo", "Landry", "Withers", "James", "Farris", "Ingram"],
          "First Name": ["Armando", "RJ", "Elliot", "Zayden", "Cormac", "Seth", "Paxson", "Jalen", "Creighton", "Rob", "JaeLyn", "Okonkwo", "Duwe", "Harrison"],
          "Height": [83, 72, 73, 81, 77, 75, 77, 82, 73, 76, 81, 80, 79, 79],
          "Weight": [240, 180, 180, 225, 195, 195, 195, 230, 180, 190, 215, 240, 210, 235]
          }
data = pd.DataFrame(player)

#calculate bmi = weight in kg / height in meters squared
data["bmi"] = round((data["Weight"]/2.205 / (data["Height"]/39.37)**2),2)

print(data)
data.to_csv("bmi.csv")