# Return type should be a list of tuples
def nearestVegetarianRestaurant(totalRestaurants, allLocations,
                                numRestaurants):
    # WRITE YOUR CODE HERE
    loc = []
    for x,y in allLocations:
        loc.append((x,y))
    loc.sort(key = lambda l: l[0]**2 + l[1]**2)
    return loc[:numRestaurants]

print(nearestVegetarianRestaurant(5, [[0,0], [1,1],[2,3],[3,1],[2,2],[1,3]], 3))