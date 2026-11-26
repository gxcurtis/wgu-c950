import re

class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.zip_code = None
        self.neighbors = []
        self.package = None

    def __str__(self):
        return f"{self.name}, {self.address} {self.zip_code}"

    def set_zip_code(self, first_two_address_strings: list):
        if match1 := re.search(r'841\d{2}', first_two_address_strings[0]):
            self.zip_code = match1.group()
        elif match2 := re.search(r'841\d{2}', first_two_address_strings[1]):
            self.zip_code = match2.group()
        else:
            self.zip_code = None
    
    def set_package(self, package):
        self.package = package

    def add_neighbor(self, neighbor_location: "Location", neighbor_distance: float):
        neighbor = Neighbor(neighbor_location, neighbor_distance)
        self.neighbors.append(neighbor)

    def sort_neighbors(self):
        sorted_neighbors = sorted(self.neighbors, key=lambda n: n.distance)
        self.neighbors = sorted_neighbors

    def print_neighbors(self):
        for neighbor in self.neighbors:
            print(f"{self.name} -> {neighbor.location.name}: {neighbor.distance} miles")

class Neighbor:
    def __init__(self, neighbor: Location, distance: float):
        self.location = neighbor
        self.distance = distance


if __name__ == "__main__":
    pass