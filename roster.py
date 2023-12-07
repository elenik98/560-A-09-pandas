# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

roster = ["Bacot", "Davis", "Cadeau"]
player = {"Last Name": roster,
          "First Name": ["Armando","RJ", "Elliot"],
          "Height": [83,72,73],
          "Weight": [240,180,180]
          }
data = pd.DataFrame(player)
print(data)