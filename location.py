
class Location:
    def __init__(self, name: str, address: str):
        self.name = name
        self.address = address
        self.zip_code = None
        self.neighbors = []
        self.package = None

    def add_neighbor(self, neighbor_location: "Location", neighbor_distance: float):
        neighbor = Neighbor(neighbor_location, neighbor_distance)
        self.neighbors.append(neighbor)

    def sort_neighbors(self):
        sorted_neighbors = sorted(self.neighbors, key=lambda n: n.distance)
        self.neighbors = sorted_neighbors

    def set_package(self, package):
        self.package = package


class Neighbor:
    def __init__(self, neighbor: Location, distance: float):
        self.location = neighbor
        self.distance = distance