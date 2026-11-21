import heapq

graph = {
    "Pune":{
        "Satara": 110,
        "Ahilyanagar":120,
        "Mumbai":150
    },
    "Mumbai":{
        "Pune":150,
        "Nashik":170,
        "Palghar":100
    },
    "Satara":{
        "Pune":110,
        "Kolhapur":130,
        "Solapur":190
    },
    "Kolhapur":{
        "Satara":130,
        "Sangli":90
    },
    "Sangli":{
        "Kolhapur":50,
        "Solapur":180
    },
    "Ahilyanagar":{
        "Pune":120,
        "Nashik":160,
        "Chhatrapati Sambhajinagar":220,
        "Solapur":250
    },
    "Nashik":{
        "Mumbai":170,
        "Ahilyanagar":160,
        "Palghar":150
    },
    "Palghar":{
        "Mumbai":100,
        "Nashik":150
    },
    "Chhatrapati Sambhajinagar":{
        "Ahilyanagar":220
    },
}

def shortest_route(graph,source,destination):
    distance = {district : float("inf") for district in graph}
    distance[source] = 0
    previous = {}
    priority_queue = [(0,source)]

    while priority_queue:
        current_distance, current_district = heapq.heappop(priority_queue)

        if current_distance > distance[current_district]:
            continue

        if current_district == destination:
            break

        for neighbor, road_distance in graph[current_district].items():
            new_distance = current_distance + road_distance

            if new_distance<distance[neighbor]:
                distance[neighbor] = new_distance
                previous[neighbor] = current_district
                heapq.heappush(priority_queue,(new_distance,neighbor))

    if distance[destination] == float("inf"):
        return none, float("inf")

    route = []
    current = destination

    while current in previous:
        route.append(current)
        current = previous[current]

    route.append(source)
    route.reverse()

    return route, distance[destination]

print("Available Cities")
for district in graph:
    print("-", district)

source = input("\n Source city:").strip()
destination = input("Destination city:").strip()

if source not in graph or destination not in graph:
    print("Wrong name, Write name according to the list only")
else:
    route, total_distance = shortest_route(graph,source,destination)

    if route is None:
        print("Route is unavailable between these two cities")

    else:
        print("\n Most least distance route:")
        print(" -> ".join(route))
        print("Total distance", total_distance, " km")


