from utils import *

def output_format(file_name, car_info):
    file_path = file_name

    # Write arrays to the CSV file
    with open(file_path, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(car_info)