class CityNavigationSystem:
    def __init__(self):
        # graph representation: {location: {neighbor: distance}}
        self.city_graph = {}

    def add_location(self, location):
        # add a location (node) to the city graph
        if location not in self.city_graph:
            self.city_graph[location] = {}
            print(f"Location '{location}' added to the city network.")
        else:
            print(f"Location '{location}' already exists in the city network.")

    def add_road(self, location1, location2, distance):
        # add a road (edge) between two locations with a given distance
        if location1 in self.city_graph and location2 in self.city_graph:
            self.city_graph[location1][location2] = distance
            self.city_graph[location2][location1] = distance
            print(f"Road added between '{location1}' and '{location2}' with distance {distance}.")
        else:
            print("One or both locations do not exist in the city network.")

    def display_city_map(self):
        # display the city map as a graph
        print("\nCity Map:")
        for location, neighbors in self.city_graph.items():
            connections = ", ".join([f"{neighbor} ({distance} km)" for neighbor, distance in neighbors.items()])
            print(f"{location} -> {connections}")

    def find_shortest_route(self, start, end):
        # find the shortest route using Dijkstra's algorithm
        if start not in self.city_graph or end not in self.city_graph:
            print("One or both locations do not exist in the city network.")
            return

        # priority queue to store (distance, current location, path)
        queue = [(0, start, [])]
        visited = set()

        while queue:
            current_distance, current_location, path = queue.pop(0)

            if current_location in visited:
                continue

            # add current location to the path
            path = path + [current_location]

            # if the destination is reached
            if current_location == end:
                print(f"\nShortest route from '{start}' to '{end}':")
                print(" -> ".join(path))
                print(f"Total distance: {current_distance} km")
                return

            visited.add(current_location)

            # explore neighbors
            for neighbor, distance in self.city_graph[current_location].items():
                if neighbor not in visited:
                    queue.append((current_distance + distance, neighbor, path))

        print(f"No route found from '{start}' to '{end}'.")


if __name__ == "__main__":
    city = CityNavigationSystem()

    # adding locations
    city.add_location("Gulberg")
    city.add_location("Johar Town")
    city.add_location("Model Town")
    city.add_location("DHA")
    city.add_location("Lahore Cantt")
    city.add_location("Shadman")
    city.add_location("Barkat Market")

    # adding roads (distance in KM)
    city.add_road("Gulberg", "Johar Town", 5)
    city.add_road("Gulberg", "DHA", 7)
    city.add_road("Johar Town", "Model Town", 3)
    city.add_road("Model Town", "DHA", 4)
    city.add_road("DHA", "Lahore Cantt", 6)
    city.add_road("Lahore Cantt", "Shadman", 2)
    city.add_road("Shadman", "Barkat Market", 1)
    city.add_road("Gulberg", "Lahore Cantt", 8)
    city.add_road("Johar Town", "Barkat Market", 6)
    city.add_road("Model Town", "Barkat Market", 7)

    # display the city map
    city.display_city_map()

    # find the shortest route
    city.find_shortest_route("Gulberg", "Barkat Market")
