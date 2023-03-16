import networkx as nx
import heapq
from datetime import datetime, timedelta
import math


# Reads the file and inputs the values for order ID Delivery Address Time placed, and estimated time to finish
def extract_info(filename):
    orders = {}
    with open(filename, "r") as f:
        for line in f:
            values = line.strip().split(",")
            orderID = int(values[0].replace("Order ID: ", ""))
            deliveryAddress = values[1].replace(" Delivery Address: ", "")
            timePlaced = values[2].replace(" Time Placed: ", "")
            estimatedTime = values[3].replace(" Estimated Time to Prepare: ", "")
            estimatedTime = estimatedTime.replace(" minutes", "")
            # calculates the estimated time to finish
            timeFinish = (
                datetime.strptime(timePlaced, "%I:%M %p")
                + timedelta(minutes=int(estimatedTime))
            ).strftime("%I:%M %p")
            orders[orderID] = {
                "Delivery Address": deliveryAddress,
                "Time Order is Ready": timeFinish,
            }
    return orders


# sorts the orders by the time they will be ready
def sort_by_ready(order):
    return dict(sorted(order.items(), key=lambda item: item[1]["Time Order is Ready"]))


orders = extract_info("orders.txt")
# creates the sorted order dictionary the orders are sorted by estimated time to prepare
sortedOrders = sort_by_ready(orders)
adjMatrix = [
    [0, 2, math.inf, math.inf, math.inf, math.inf],
    [2, 0, 3, 2, 1, math.inf],
    [math.inf, 3, 0, 1, 2, math.inf],
    [math.inf, 2, 1, 0, 1, 4],
    [math.inf, 1, 2, 1, 0, 3],
    [math.inf, math.inf, math.inf, 4, 3, 0],
]  # restaurant index = 0 main st index =1 elm st index = 2 oak st index = 3 pine st index = 4 cedar_st index  = 5

# I chose to implment the floyd_warshall method from chosing the shortest path
def floyd_warshall(adjMatrix):
    global nextVert, adjc_matrix
    n = len(adjMatrix)
    nextVert = [[None for j in range(n)] for i in range(n)]
    for i in range(n):
        for j in range(n):
            if adjMatrix[i][j] != math.inf:
                nextVert[i][j] = j
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if adjMatrix[i][k] != math.inf and adjMatrix[k][j] != math.inf:
                    if adjMatrix[i][k] + adjMatrix[k][j] < adjMatrix[i][j]:
                        adjMatrix[i][j] = adjMatrix[i][k] + adjMatrix[k][j]
                        nextVert[i][j] = nextVert[i][k]
    adjc_matrix = adjMatrix


# takes two vertcies and determines the shortest path in between them
def shortest_path(u, v):
    global nextVert
    path = [convert_num_st(u)]
    while u != v:
        u = nextVert[u][v]
        # append the distance from the last node I deliverd to back to the restaurant
        path.append(convert_num_st(u))
    return path


# takes in two verticies and determines the distance to travel in between them
def cal_dist(u, v):
    global adjc_matrix
    return adjc_matrix[u][v]


# calculates the amount of time to deliver items for two inputted vertcies
def calc_time(u, v):
    x = cal_dist(u, v) / 35
    minutes = int(x * 60)
    return timedelta(minutes=minutes)


# converts the numbers pretaining to destinations to street names
def convert_num_st(x):
    if x == 0:
        return "Restaurant"
    elif x == 1:
        return "123 Main St"
    elif x == 2:
        return "456 Elm St"
    elif x == 3:
        return "789 Oak St"
    elif x == 4:
        return "159 Pine St"
    elif x == 5:
        return "753 Cedar St"


# converts the street names to the numbers pretaining to them
def convert_name_st(x):
    if x == "Restaurant":
        return 0
    elif x == "123 Main St":
        return 1
    elif x == "456 Elm St":
        return 2
    elif x == "789 Oak St":
        return 3
    elif x == "159 Pine St":
        return 4
    elif x == "753 Cedar St":
        return 5


# snake case for functiton camel case for variabels
def order_processing(sortedOrders):
    orders = list(sortedOrders.keys())
    totalDistance = 0
    i = 0
    while i < len(orders):
        currDeliveryAddress = convert_name_st(
            sortedOrders[orders[i]]["Delivery Address"]
        )
        currReady = datetime.strptime(
            sortedOrders[orders[i]]["Time Order is Ready"], "%I:%M %p"
        )
        distTime = calc_time(0, currDeliveryAddress)
        if i < len(orders) - 1:
            nextKey = orders[i + 1]

            if (currReady + (distTime * 2)) > datetime.strptime(
                sortedOrders[nextKey]["Time Order is Ready"], "%I:%M %p"
            ):
                next_Delivery_Address = convert_name_st(
                    sortedOrders[nextKey]["Delivery Address"]
                )
                if cal_dist(0, next_Delivery_Address) >= cal_dist(
                    0, currDeliveryAddress
                ):
                    path = (
                        shortest_path(0, currDeliveryAddress)
                        + shortest_path(currDeliveryAddress, next_Delivery_Address)[1:]
                        + shortest_path(next_Delivery_Address, 0)[1:]
                    )
                    print(path)
                    totalDistance += (
                        cal_dist(0, currDeliveryAddress)
                        + cal_dist(currDeliveryAddress, next_Delivery_Address)
                        + cal_dist(next_Delivery_Address, 0)
                    )
                    i = i + 1
                # take two orders
                else:
                    path = (
                        shortest_path(0, next_Delivery_Address)
                        + shortest_path(next_Delivery_Address, currDeliveryAddress)[1:]
                        + shortest_path(currDeliveryAddress, 0)[1:]
                    )
                    totalDistance += (
                        cal_dist(0, next_Delivery_Address)
                        + cal_dist(currDeliveryAddress, next_Delivery_Address)
                        + cal_dist(currDeliveryAddress, 0)
                    )
                    print(path)
                    i = i + 1
            else:
                path = (
                    shortest_path(0, currDeliveryAddress)
                    + shortest_path(currDeliveryAddress, 0)[1:]
                )
                totalDistance += cal_dist(0, currDeliveryAddress) * 2
                print(path)
        else:
            path = (
                shortest_path(0, currDeliveryAddress)
                + shortest_path(currDeliveryAddress, 0)[1:]
            )
            totalDistance += cal_dist(0, currDeliveryAddress) * 2
            print(path)
        i = i + 1

    print("Total Distance Traveled: " + str(totalDistance))


floyd_warshall(adjMatrix)
order_processing(sortedOrders)
