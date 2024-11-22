""" import csv
import numpy as np
import matplotlib.pyplot as plt

from scipy.stats import norm
import numpy as np



def mean(x):
    return sum(x)/len(x)

def std(x):
    u= mean(x)
    return mean( [ (i-u)**2 for i in x ])**0.5


def p():  
    for x in range(4):     
        m= mean(dataset[x])
        s= std(dataset[x])
        print(f"{measures[x]:}")
        print(f"mean: {m:.4f}")
        print(f"std: {s:.4f}")
        print(f"\n")



def value_amg_species():
    
    
    for i in range(4):
        print(f"{measures[i]:}")
        for elem in types :
            new=[v for v, t in zip(dataset[i], dataset[4]) if(elem==t)]
            m= mean(new)
            s= std(new)
            print(f"type: {elem}")
            print(f"mean: {m}")
            print(f"std: {s}")
            print("\n")
            

        print("\n")
    
        
        
        
       
        
                




dataset= [[],[],[],[],[]]
measures= ["sepal length", "sepal width", "petal length", "petal width"]

with open("iris.csv") as file:
    for line in csv.reader(file):
        if(len(line)==5):
            for i in range(0,4):
                dataset[i].append(float(line[i]))
            dataset[4].append(line[4])

types= list(set(dataset[4]))
print(types)
p()
value_amg_species()


def plot_histogram():
    colors=['b','g','r']
    for index, m in enumerate(measures):
        plt.figure()
        plt.title(m)
        for type , color in zip(types, colors):
            value=[v for v, t in zip(dataset[index], dataset[4]) if type== t]
            plt.hist(value, density=True, alpha=0.2, color=color)
            u=mean(value)
            s=std(value)
            x=np.linspace(u-5*s, u+5*s, 100)
            plt.plot(x, norm(u, s).pdf(x), color=color, label=type)
            plt.xlabel(f"{m} (cm)")
            plt.ylabel("density")
        plt.legend()
    plt.show()



plot_histogram() """


"""                           exercise 2        """

import json

with open ("bike.json") as f:
    bike_db= json.load(f)
    print(bike_db['network']['stations'])


def test():
    #print(bike_db['network']['stations'][0]['extra']['status'])
    for k in bike_db['network']['stations']:
        print(f"{k}\n")
        
    


def count_active_stations():
    count_act_st=0
    count_free_bikes=0
    count_free_docks=0
    for index, x in enumerate(bike_db['network']['stations']):
        if x['extra']['status']=="online":
            count_act_st+=1
        if x['free_bikes']>0:
            count_free_bikes+= x['free_bikes']
        if x['empty_slots']>0:
            count_free_docks+= x['empty_slots']
    print(f"active station: {count_act_st}")
    print(f"free_bikes: {count_free_bikes}")
    print(f"empty_slots: {count_free_docks}")


from math import cos, acos, sin

def distance_coords(lat1, lng1, lat2, lng2):
    deg2rad = lambda x: x * 3.141592 / 180
    lat1, lng1, lat2, lng2 = map(deg2rad, [ lat1, lng1, lat2, lng2 ])
    R = 6378100 # Radius of the Earth, in meters
    return R * acos(sin(lat1) * sin(lat2) + cos(lat1) * cos(lat2) * cos(lng1 - lng2))

lat=45.074512
long=7.694419

""" def closet_station():
    min_dist=None;
    for index, x in enumerate(bike_db['network']['stations']):
        distance= distance_coords( bike_db['network']['stations'][index]['latitude'], bike_db['network']['stations'][index]['longitude'], lat, long)
        if distance < min_dist: 
            if bike_db['network']['stations'][index]['free_bikes']>0:
                min_dist=distance
                name=bike_db['network']['stations'][index]['name']
    if min_dist !=None:
        print(name) """


def distance_from_point(dataset, lat, lng):
    closest = (None, None)
    for station in dataset["network"]["stations"]:
        closest_station, closest_distance = closest
        current_distance = distance_coords(lat, lng, station["latitude"], station["longitude"])
        # if closest_distance is None, then we are at the first
        # loop execution where the station has available bikes.
        # In that case, we save the current station as the 
        # closest one (as we do not have any other stations available).
        # From the next cycle on, to update `closest`, we need
        # the station to actually be closer than the already saved one.
        if station["free_bikes"] > 0 and (closest_distance is None or current_distance < closest_distance):
            closest = (station, current_distance)
    return closest

station, distance = distance_from_point(bike_db, 45.074512, 7.694419)
print("Closest station:", station["name"])
print("Distance:", distance, "meters")
print("Number of available bikes:", station["free_bikes"])

#closet_station()

#test() 
count_active_stations()

