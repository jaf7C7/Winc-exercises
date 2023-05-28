# Do not modify these lines
__winc_id__ = '25596924dffe436da9034d43d0af6791'
__human_name__ = 'conditions'

# Add your code after this line


def farm_action(weather, time_of_day, cows_need_milking, cow_location, season,
                slurry_tank_full, grass_is_long):
    if (cow_location == 'pasture' and (time_of_day == 'night' or
                                       weather == 'rainy')):
        action = 'take cows to cowshed'
    elif cows_need_milking:
        action = 'milk cows'
    elif slurry_tank_full and (weather != 'sunny' or weather != 'windy'):
        action = 'fertilize pasture'
    elif (grass_is_long and season == 'spring' and weather == 'sunny' and
            cow_location != 'pasture'):
        action = 'mow grass'
    else:
        action = 'wait'

    if (cow_location != 'cowshed' and (action == 'milk cows'
                                       or action == 'fertilize pasture'
                                       or action == 'mow grass')):
        action = f'take cows to cowshed\n{action}\ntake cows back to pasture'

    return action
