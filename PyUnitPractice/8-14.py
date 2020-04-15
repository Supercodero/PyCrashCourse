def make_car(maker,version,**car_info):
    car = {}
    car['maker'] = maker
    car['version'] = version
    for k,v in car_info.items():
        car[k] = v
    return car

car = make_car('subaru','outback',color='blue',tow_package=True)
print(car)