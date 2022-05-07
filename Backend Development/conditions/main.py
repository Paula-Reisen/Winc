# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line
def farm_action(weather, time_of_the_day, cow_milking_status, location_of_the_cows, seasons, slurry_tank, grass_status):
    if weather == 'Rain' and time_of_the_day == 'night' and location_of_the_cows == 'pasture':
        return('take cows to cowshed')
    elif cow_milking_status == True and location_of_the_cows == 'cowshed':
               return('milk cows')
    elif cow_milking_status == True and location_of_the_cows == 'pasture':
                return('take cows to cowshed\nmilk cows\ntake cows back to pasture')
    elif slurry_tank == True and (weather != 'sunny' or weather != 'windy'):
        if location_of_the_cows == 'cowshed':
            return('fertilize pasture')
        else:
            return('take cows to cowshed\nfertilize pasture\ntake cows back to pasture')
    elif grass_status == True and seasons == 'spring' and weather == 'sunny':
        if location_of_the_cows == 'cowshed':
            return('mow grass')
        else:
            return('take cows to cowshed\nmow grass\ntake cows back to pasture')
    else:
        return('wait') 

farm_action('sunny', 'day', True, 'pasture', 'spring', False, True)
farm_action('rainy', 'night', False, 'cowshed', 'winter', False, True)
