import csv
from pathlib import Path
from package import Package
from distance_table import DistanceTable

### Hash Table data structure with tasks A & B ###
class PackageHashTable:
    def __init__(self, size=40, csv_file="wgups_package_file.csv"):
        self.packages: list[Package | None] = [None] * size
        self.distance_table = DistanceTable()
        self.load_from_csv(csv_file)

    #####################
    ### Requirement A ###
    #####################
    def add_package(self, package_id, package_weight=None, delivery_address=None, delivery_city=None, delivery_state=None, delivery_zip_code=None, delivery_deadline=None, delivery_status=None, delivery_notes=None):
        package = Package(
            package_id,
            package_weight = package_weight,
            delivery_address = delivery_address,
            delivery_city = delivery_city, 
            delivery_state = delivery_state, 
            delivery_zip_code = delivery_zip_code,
            delivery_deadline = delivery_deadline,
            delivery_status = delivery_status,
            delivery_notes = delivery_notes
        )

        if delivery_address is not None:
            package_location = self.distance_table.get_location(delivery_address)
        else:
            package_location = None

        if package_location is not None:
            package.set_location(package_location)
        else:
            print(f"Location not found with address: {delivery_address}")



        # Hash Package ID with modulo operator and store at index
        index = package.id % len(self.packages)
        self.packages[index] = package

    #####################
    ### Requirement B ###
    #####################
    def get_package(self, package_id: int) -> Package | None:
        # Return Package object at index
        package_id = int(package_id)
        if package_id < 1 or package_id > len(self.packages):
            return None
        index = package_id % len(self.packages)
        return self.packages[index]
        
    # Load package data from csv task file
    def load_from_csv(self, csv_file):
        self.csv_file = Path(csv_file)
        if not self.csv_file.exists():
            raise FileNotFoundError(f"CSV file not found: {self.csv_file}")
        
        with open(csv_file, "r", encoding="utf-8") as file:
            rows = list(csv.reader(file))

        # Track packages that must be delivered together
        package_group = []

        start_loading = False
        for row in rows:
            if "Package" in row[0] and "ID" in row[0]:
                for i, header in enumerate(row):
                    row[i] = header.replace("\n", " ").strip()

                package_id_index = row.index("Package ID")
                address_index = row.index("Address")
                city_index = row.index("City")
                state_index = row.index("State")
                zip_index = row.index("Zip")
                deadline_index = row.index("Delivery Deadline")
                weight_index = row.index("Weight KILO")
                notes_index = row.index("page 1 of 1PageSpecial Notes")
                start_loading = True
                continue
            
            # Load packages after the header row is parsed
            if start_loading:
                package_id = int(row[package_id_index])
                delivery_notes = row[notes_index]

                if "Delayed" in delivery_notes:
                    delivery_status = "delayed"
                else:
                    delivery_status = "at the hub"

                # Add package using index from header row
                self.add_package(
                    package_id,
                    package_weight = row[weight_index],
                    delivery_address = row[address_index],
                    delivery_city = row[city_index],
                    delivery_state = row[state_index],
                    delivery_zip_code = row[zip_index],
                    delivery_deadline = row[deadline_index],
                    delivery_status = delivery_status,
                    delivery_notes = row[notes_index]
                )

                if "Must be delivered with" in delivery_notes:
                    package_group.append(self.get_package(package_id))

    def print_packages(self):
        for package in self.packages:
            print(package)

if __name__ == "__main__":
    pht = PackageHashTable()
    for package in pht.packages:
        if package is not None:
            print(type(package.location))