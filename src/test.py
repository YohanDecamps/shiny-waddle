import json
import random

data_name = input("give me the name of the data\n")

with open(data_name) as f:
   data_list = json.load(f)

data_dict = {}
for item in data_list:
   name = item["reg_name"]
   data_dict[name] = item

data_param = input("give me the field you wish to play\n")
random_country_name, random_country_data = random.choice(list(data_dict.items()))

found = False
while not found:
   country = input("gimme a country\n")

   try:
      data_dict[country]
   except KeyError:
      print(country, "not found")
      continue

   if data_dict[country][data_param] > random_country_data[data_param]:
      print("Too much", data_param, random_country_name)
   elif data_dict[country][data_param] < random_country_data[data_param]:
      print("Too few", data_param, random_country_name)
   else:
      found = True

print("GG well played")
