from location import Location
from distance_table import DistanceTable

dist_table = DistanceTable()

class Package:
    def __init__(self, package_id, **package_data):
        self.id = int(package_id)
        self.address = package_data.get("delivery_address")
        self.city = package_data.get("delivery_city")
        self.weight = package_data.get("package_weight")
        self.state = package_data.get("delivery_state")
        self.zip_code = package_data.get("delivery_zip_code")
        self.deadline = package_data.get("delivery_deadline")
        self.notes = package_data.get("delivery_notes")
        self.status = package_data.get("delivery_status")
        self.location: Location | None = None

    def __str__(self):
        return f"Package {self.id}, {self.status} -> {self.address} : Delivered by {self.deadline}"

    def set_location(self, location: Location):
        self.location = location