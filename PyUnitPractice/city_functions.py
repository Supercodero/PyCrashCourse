def city_function(city_name,country_name,population=''):
    if population:
        city_full_name = city_name.title()+','+country_name.title()+' - population '+str(population)
    else:
        city_full_name = city_name.title()+','+country_name.title()
    return city_full_name