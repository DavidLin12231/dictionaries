from geopy.distance import geodesic

cities = {
"tokyo": (35.6762, 139.6503),
"shanghai": (31.2304, 121.4737),
"beijing": (39.9042, 116.4074),
"osaka": (34.6937, 135.5023),
"taipei": (25.0330, 121.5654),
"moscow": (55.7558, 37.6173) }

#Don't edit above this line

def tickets(destination, origin='taipei', faretype='economy', num=1):
    d = cities[destination]
    o = cities[origin]
    distance = round(geodesic(d, o).km,1)
    base_cost = 15*distance*num
    if faretype=='economy':
        total = base_cost
    elif faretype == 'business':
        total = base_cost*1.5
    elif faretype == 'first':
        total = base_cost*2.5
    return(total)

ori = input("Enter your origin: ")
de = input("Enter your destination: ")
ft = input("Enter your Fare Type: ")
nu = int(input("Enter number of tickets: "))

x = tickets(de, ori, ft, nu)
print(x)
