import csv
import os

def export_vehicle_data(filename, vehicles):
    """Export vehicle data to a CSV file."""
    if os.path.exists(filename):
        os.remove(filename)  # Remove the file if it already exists to avoid appending to old data  
    with open(filename, mode='w', newline='')as file:
        writer = csv.writer(file)
        writer.writerow(['Brand', 'Model', 'Year', 'Owner', 'Battery Capacity'])
        
        for v in vehicles:
            #Handle owner info safely
            owner = v.get_owner()
            if owner is None:
                owner = "No owner assigned"
            batter_capacity = getattr(v, 'battery_capacity', 'N/A')
            writer.writerow([v.brand, v.model, v.year, owner, batter_capacity]) 
    return f"Vehicle data exported to {filename} successfully."