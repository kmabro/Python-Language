# or
"""
temp = 25;
is_raining = False

if temp > 35 or temp < 0 or is_raining:
    print("thw outdoor event is cancelled")
else:
    print("The outdoor is still scheduled")
"""

# and
"""
temp = 20
is_sunny = True
if temp >= 28 and is_sunny:
     print("It is HOT outside")
     print("It is Sunny")
elif temp <=0 and is_sunny:
    print("It is COLD outside")
    print("It is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is Sunny")
"""

# not
temp = 0
is_sunny = False
if temp >= 28 and is_sunny:
     print("It is HOT outside")
     print("It is Sunny")
elif temp <=0 and is_sunny:
    print("It is COLD outside")
    print("It is Sunny")
elif 28 > temp > 0 and is_sunny:
    print("It is WARM outside")
    print("It is Sunny")
elif temp >= 28 and not is_sunny:
        print("It is HOT outside")
        print("It is Cloudy")
elif temp <= 0 and not is_sunny:
        print("It is COLD outside")
        print("It is Cloudy")
elif 28 > temp > 0 and not is_sunny:
        print("It is WARM outside")
        print("It is Cloudy")