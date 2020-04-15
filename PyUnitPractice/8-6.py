def city_country(city_name,country_name):
    city_full_name = '"'+city_name.title()+','+country_name.title()+'"'
    return city_full_name

city_n = input("what's your favorite city?")
country_n = input("what that city from?")
full_n = city_country(city_n,country_n)
print(full_n)