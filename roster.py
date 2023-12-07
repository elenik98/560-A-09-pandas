# https://goheels.com/sports/mens-basketball/roster

import pandas as pd

player = {"Last Name": ["Bacot", "Davis", "Cadeau"],
          "First Name": ["Armando","RJ", "Elliot"],
          "Height": [83,72,73],
          "Weight": [240,180,180]
          }
data = pd.DataFrame(player)
print(data)