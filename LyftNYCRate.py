from math import sin, cos, atan2, radians, sqrt

# Approx. radius of earth in km (Required for distance calculation)
R = 6373.0

# Fares' service id : 0=Lyft, 1=XL, 2=Lux Black, 3=Lux Black XL
# Rates are : base fare, cost per mile, cost per min, max fare & min fare respectively
fares = [[2.29,1.58,0.32,450.0,7.19], [3.46,2.56,0.45,450.0,9.43], [6.29,3.37,0.59,700.0,13.47], [12.58,4.05,0.72,700.0,22.45]]


# Function
def calculate_rate(lat_src, lon_src, lat_dest, lon_dest, wait_time, service_id):

    # NYC Coordinate range. Source : https://on.nyc.gov/2s80jgV
    if ((lon_src or lon_dest) < -74.257159 or (lon_src or lon_dest) > -73.699215) or ((lat_src or lat_dest) < 40.495992 or (lat_src or lat_dest) > 40.915568):
        print("WARNING : Coordinates specified may not be in NYC")

    # Distance calculation
    delta_lat = radians(lat_dest) - radians(lat_src)
    delta_lon = radians(lon_dest) - radians(lon_src)
    a = sin(delta_lat / 2)**2 + cos(radians(lat_src)) * cos(radians(lat_dest)) * sin(delta_lon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = (R*c)*0.621371  # km to m

    # Fare definitions
    base_fare = fares[service_id][0]
    cost_distance = (distance*fares[service_id][1])
    cost_wait = wait_time*fares[service_id][2]
    min_fare = fares[service_id][4]
    max_fare = fares[service_id][3]

    total_cost = base_fare + cost_distance + cost_wait

    # Max and Min fare conditions
    if total_cost > max_fare:
        return max_fare
    elif total_cost < min_fare:
        return min_fare
    else:
        return round(total_cost, 2)


# Insert your parameters below (source lat, source lon, destination lat, destination lon, trip wait time, service id)
print("Total cost = ", calculate_rate(40.5, -73.8, 40.7, -73.9, 2, 0))