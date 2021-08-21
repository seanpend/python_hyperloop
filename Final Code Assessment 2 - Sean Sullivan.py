import csv
#used to read csv file
import sys
#used for exit function
import turtle
import matplotlib.pyplot as plt
import pandas as pd
#these 3 modules are used for the graphical representation

#boolean values to determine when a route is found and if it is selected
selected = False
route_found = False

#transport speeds for time calculation
transport_speed = {
    "Hyperloop": 1000,
    "Plane": 841,
    "High Speed Rail": 300,
    "Rail": 220,
    "Car": 112
}

#stores routes in dict
routeDict = {}

#text file to write output into
origin_data = open("routeinfo.txt", "a")

#read in the csv file
with open("REA.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    #loops over each row in csv file
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            key = row[0:1]
            key = key[0]
            value = row[1:2]
            value = value[0]          
            routeDict[key] = value
            line_count += 1 
 
#loops through routes in csv file to print routes to user        
print("Select a route:")            
for i in routeDict:
    print(i)

#takes user input for city
while not selected:
    city = input("Please enter your city:")
    city = city.title()
    #if user enters NA or Na as city input program ends
    if (city in {"NA", "Na"}):
        print("\nExit Selected \nHave a good day :)\n \n")
        sys.exit()  
    #takes user input for confirm choice y/n   
    confirm_choice = input("Origin City: " + city + "\n" + "Confirm City: Y or N \n")
    confirm_choice = confirm_choice.upper()
    #if y program continues if n asks user for input again
    if (confirm_choice == "Y"):
        selected = True
    else:
        selected = False

#loops over routes in dict
#prints the route name and distance if value is found in dict
#writes to txt file the route name and distance if found
for route in routeDict:
    if ((city + " to ") in route):
        route_name = route
        route_distance = routeDict[route]
        route_found = True
        print("The Available Route is: " + route)
        print("The Distance is: " + routeDict[route]+"km")
        origin_data.write("The Available Route is: " + route + "\n")
        origin_data.write("The Distance is: " + routeDict[route]+"km" + "\n")
 
#values stored to calculate the fastest transport        
fastest_hours = 999
fastest_minutes = 60
fastest_transport = "None"

#loops over different transport in transport_speed dict
if route_found:       
    for speed in transport_speed:
        #Speeds given in km/hr
        #Distances in km
        #calculates the hours and calculates the minutes
        hours = int(route_distance) // int(transport_speed[speed])
        minutes = round((int(route_distance) / int(transport_speed[speed]) - hours) * 60)
        
        #calculates fastest speed by comparing current mode of transport to the last one calculated
        #until a fastest transport is determined by looping through all the modes of transport
        if (hours < fastest_hours):
            fastest_hours = hours
            fastest_minutes = minutes
            fastest_transport = speed
        elif (hours == fastest_hours and minutes < fastest_minutes):
            fastest_minutes = minutes
            fastest_transport = speed                      
        
        #prints the time taken by each mode of transport
        #writes the time taken by each mode of transport to txt file
        print("This trip will take " + str(hours) + " hour(s) and " + str(minutes) + " minutes by " + speed + "\n")
        origin_data.write("This trip will take " + str(hours) + " hour(s) and " + str(minutes) + " minutes by " + speed + "\n")

#prints the fastest mode of transport
#writes the fastest mode of transport to txt file
print("The Fastest Method Of Transport Is: " + fastest_transport)       
origin_data.write("The Fastest Method Of Transport Is: " + fastest_transport + "\n")  

#prints if route isn't found from the user input       
if not route_found:
    print("Route was not found. No routes exist for this city.")

#closes and saves the txt file
origin_data.close()   
'''
Horizontal Bar Chart with Turtle
Information and Code used as a guide from Runestone Academy 
6.11 A Turtle Bar Chart
https://runestone.academy/runestone/books/published/thinkcspy/Functions/ATurtleBarChart.html
(Miller & Ranum, 2013)
'''
#class to draw the bars for graph
def drawBar(t, height):
    #Get turtle t to draw one bar, of height
    t.begin_fill()              
    t.left(90)
    t.forward(height)
    t.color("white")
    t.write(str(hours) + " Hour(s) and " + str(minutes) + " Minutes \n by "+ str(speed), font=("Arial", 10, "normal"))
    t.color("blue")
    t.fillcolor("red")
    t.right(90)
    t.forward(40)
    t.right(90)
    t.forward(height)
    t.left(90)
    t.end_fill()                
    t.penup()
    t.forward(100)
    t.pendown()

mode_speed = [112, 220, 300, 841, 1000]  #transport speeds
maxheight = max(mode_speed)
numbars = len(mode_speed)
border = 0

if route_found:
    wn = turtle.Screen()             #window setup and attributes
    wn.setworldcoordinates(0-border, 0-border, 260*numbars+border, maxheight+border)
    wn.bgcolor("black")
    wn.title("Route Estimator Chart")
    tess = turtle.Turtle()           #create tess and add titles
    tess.penup()
    tess.forward(400)
    tess.pendown()
    tess.pensize(100)
    tess.color("green")
    tess.write("Recommended Transport is " + str(fastest_transport), font=("Arial", 16, "normal"))
    tess.penup()
    tess.right(180)
    tess.forward(400)
    tess.right(90)
    tess.forward(950)
    tess.right(90)
    tess.forward(400)
    tess.pendown()
    tess.write("The Route is " + str(route_name), font=("Arial", 16, "normal"))
    tess.penup()
    tess.right(180)
    tess.forward(400)
    tess.left(90)
    tess.forward(150)
    tess.pendown()
    tess.color("blue")
    tess.fillcolor("red")
    tess.pensize(3)



if route_found:       
    for speed in transport_speed:
        #loops over transport speeds for tess to draw the bars
        hours = int(route_distance) // int(transport_speed[speed])
        minutes = round((int(route_distance) / int(transport_speed[speed]) - hours) * 60)
        hours_graph = hours * 60
        turtle_height = hours_graph + minutes 
        drawBar(tess, turtle_height)

    #exits turtle screen on click
    wn.exitonclick()
'''
Horizontal Bar Chart with matplotlib
Information and Code used as a guide from matplotlib.org
https://matplotlib.org/3.1.0/gallery/lines_bars_and_markers/barh.html
(Hunter, et al., 2012)
'''
if route_found:
    for speed in transport_speed:
            hours = int(route_distance) // int(transport_speed[speed])
            minutes = round((int(route_distance) / int(transport_speed[speed]) - hours) * 60)
            hours_graph = hours * 60
            total_minutes = hours_graph + minutes
            x = speed
            y = total_minutes
            plt.barh(x,y,label ='Travel Time')
            #plots horizontal bars for each speed in transport_speed
if route_found:
    plt.xlabel('Time required in Minutes')
    plt.ylabel('Mode of Transport')
    plt.title('Route Estimator with Matplot')
    plt.show()
    #plots the horizontal graph
'''
Horizontal Bar Chart with Pandas
Information and Code used as a guide from pandas.pydata.org
https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.bar.html
(Pandas development team, 2008)
'''
pd_minutes=[]
pd_transport=[]
#empty lists used to store values for the panda dataframe
if route_found:
    for speed in transport_speed:
            hours = int(route_distance) // int(transport_speed[speed])
            minutes = round((int(route_distance) / int(transport_speed[speed]) - hours) * 60)
            hours_graph = hours * 60
            total_minutes = hours_graph + minutes
            pd_minutes.append(total_minutes)
            pd_transport.append(speed)
            #values added to the empty lists
            
if route_found:                                   
    pd_time = pd_minutes
    pd_index = pd_transport
    df = pd.DataFrame({'Minutes' : pd_time}, index=pd_index)
    ax = df.plot.barh(y='Minutes')
    ax.set_xlabel("Time required in Minutes")
    ax.set_ylabel("Mode of Transport")
    ax.set_title("Route Estimator with Pandas")
    ax
    #horizontal graph plotted using the pandas dataframe data






