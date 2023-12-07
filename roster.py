# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando","RJ", "Elliot"],
          "Height": [83,72,73],
          "Weight": [240,180,180]
          }
data = pd.DataFrame(player)

#calculate bmi = weight in kg / height in meters squared
data["bmi"] = round((data["Weight"]/2.205 / (data["Height"]/39.37)**2),2)

print(data)
data.to_csv("bmi.csv")