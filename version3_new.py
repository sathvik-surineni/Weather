variable = {}
with open('weatherfile.txt', 'r') as file:
    for line in file:
        name, value = line.replace(' ', '').split('=')
        variable[name] = int(value)
W=(0.5)*(variable['temperature']**2)-(0.2)*variable['humidity']+(0.1)*variable['windspeed']-15
print(W)
if W>300:
    print("Sunny")
elif 200<W<=300:
    print("Cloudy")
elif 100<W<=200:
    print("Rainy")
else:
    print("Stormy") 