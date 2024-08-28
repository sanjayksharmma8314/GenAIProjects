import csv
import os
from datetime import datetime

def save_to_csv(data, output_dir, site_name):
    date_str = datetime.now("%Y-%m-%d")
    filename = os.path.join(output_dir , f"{site_name}"_{date_str}.csv)

    with open(filename, "w", newline="") as csv file:
