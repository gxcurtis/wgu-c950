from location import Location

class DistanceTable:
    def __init__(self, csv_file="wgups_distance_table.csv"):
            # List to hold Location instances
            self.locations = []
            # Load data from provided distance table csv file
            self.load_from_csv(csv_file)

    # Parse location string into Location instance
    def set_locations(self, locations_list: list):
        for location in locations_list:
            location_data = location.split("\n")
            location_name = location_data[0].strip()
            location_address = location_data[1].strip().strip(",")
            self.locations.append(Location(location_name, location_address))

    # Helper function for parsing distance table csv data
    def load_from_csv(self, csv_file):
        csv_file = Path(csv_file)
        if not csv_file.exists():
            raise FileNotFoundError(f"CSV file not found: {csv_file}")
        
        with open(csv_file, "r", encoding="utf-8") as file:
            csv_data = list(csv.reader(file))
  
        locations_table_head = csv_data[7][2:] # Row 7, Column 3+
        self.set_locations(locations_table_head)

        # Parse data beginning at row 8
        rows = csv_data[8:]
        # Get distance data from row/column, or inversely, column/row
        for i, row in enumerate(rows):
            self.locations[i].set_zip_code(row[:2])
            for j, col in enumerate(row[2:]):
                try:
                    distance = float(col)
                except ValueError:
                    inverse_row = rows[j][2:]
                    distance = float(inverse_row[i])
                # Don't add self as location 
                if distance == 0.0:
                    continue
                self.locations[i].add_neighbor(self.locations[j], distance)
            # Sort neighbor references by distance (closest to furthest)
            self.locations[i].sort_neighbors()
