import pandas as pd
 
City_Data = pd.read_csv("Resources/cities.csv")
 
city_html = City_Data.to_html()

text_file = open("Resources/Data.html", "w", encoding="utf-8")
text_file.write(city_html)
text_file.close()