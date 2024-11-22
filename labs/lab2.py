import csv
import matplotlib.pyplot as plt

col_name=[]
temp_db= [[],[],[],[],[],[],[]]

with open("./temp.csv") as file:
    db= csv.reader(file)
    col_name= next(db)
    
    for rows in db:
        if len(rows)== len(col_name):
            for i in range(len(temp_db)):
                temp_db[i].append(rows[i])


city_avg={}
city_un={}
cities= list(set(temp_db[3]))

def partiton():
    
    
    for city in cities:
        
        avg_temp=[temp_db[1][index] for index, c in enumerate(temp_db[3]) if c==city]
        avg_un= [temp_db[2][index] for index, c in enumerate(temp_db[3]) if c==city]
        city_avg[city]=avg_temp
        city_un[city]=avg_un

    

def count_missing(data):
    return sum([1 for d in data if d==""])


def fill_gaps(data):
    right_i = 0
    right_v = 0
    
    for i, value in enumerate(data):
        left_v = data[i-1] if i != 0 else 0
        
        # reuse the right_v value, useful when there are multiple consecutive missing values
        if i < right_i:
            data[i] = (left_v + right_v) / 2
            continue

        if value == '':
            try:
                # use a generator to search for the first occurrence 
                right_i, right_v = next((idx+i+1, float(v)) for idx, v in enumerate(data[i+1:]) if v != '')
            except StopIteration: # fired when the generator has no items left to iterate on
                right_i = len(data)
                right_v = 0
            data[i] = (left_v + right_v) / 2
        else:
            data[i] = float(data[i]) # parse to float all present values


def update_missing_value():
    for city in temp_db[3]:
        fill_gaps(city_avg[city])
        fill_gaps(city_un[city])


def update_by_specifc_city(city):
    fill_gaps(city_avg[city])



def pl():
    plt.rcParams['figure.dpi'] = 100
    for city in ['Rome', 'Bangkok']:
        plt.hist(city_avg[city], label=city)
    plt.legend()
    plt.xlabel('AverageTemperature')
    plt.show()


    



#print(city_avg['Abidjan'])
#print(count_missing(city_avg_un[0]))

#print(cities[0])


#update_missing_value()



partiton()
#print(city_avg['Rome'])
update_by_specifc_city("Rome")
update_by_specifc_city("Bangkok") 
pl() 

""" ki = [city.lower() for city in cities]
print(ki) """




