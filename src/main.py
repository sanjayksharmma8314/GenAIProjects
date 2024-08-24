from src.config_loader import load_config, load_api_keys

def main():
    config = load_config()
    api_keys = load_api_keys()

    openai_api_keys = api_keys['api_keys']['openai']
    huggingface_api_keys = api_keys['api_keys']['huggingface']


if __name__ == "__main__":
    main()