# Do not modify these lines
from datetime import date
from helpers import get_countries

__winc_id__ = "00a4ab32f1024f5da525307a1959958e"
__human_name__ = "dictionariesv2"

# Add your code after this line


def create_passport(name, date_of_birth, place_of_birth, height, nationality):

    return {"name": name,
            "date_of_birth": date_of_birth,
            "place_of_birth": place_of_birth,
            "height": height,
            "nationality": nationality
            }

def add_stamp(passport, country):
     if "stamps" not in passport:
          passport["stamps"] = [str(country)]
     if country is not passport["nationality"]:
          if country not in passport["stamps"]:
               passport["stamps"].append(country)
     return passport


def add_biometric_data(passport, name, value, date):
     if 'biometric' not in passport:
          if name not in passport:
               passport.update({"biometric":{name: {"date": date, "value": value}}})
     elif name not in passport:
         passport["biometric"].update({name: {"date": date, "value": value}})
     else:
         passport["biometric"][name][date] = date
         passport["biometric"][name][value] = value
          
     return passport


omari = create_passport("Omari Muchumba", "1995-07-16", "Kampala", 184.31, "Uganda")
omari = add_biometric_data(omari, "eye_color_left", "blue", "2020-05-05")
omari = add_biometric_data(omari, "eye_color_right", "blue", "2020-05-05")
print(omari)

