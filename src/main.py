from src.config_loader import load_config
from src.data_fetcher import fetch_data
from src.csv_operations import save_to_csv
from src.utils import setup_logging

def main():
    setup_logging = ('logs/fetch_logs.log')

    config = load_config()

    for site in config['sites']:
        data = fetch_data(site)
        if data:
            save_to_csv(data, config['output_dir'], site['name'])


if __name__ = "__main__":
    main()