import yaml
import os

def load_config(config_path = 'config/config.yaml'):
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config

def load_api_keys(api_key_path = 'config/api_keys.yaml'):
    with open(api_key_path, 'r') as file:
        api_keys = yaml.safe_dump(file)
    return api_keys

if __name__ == "__main__":
    config = load_config()
    api_keys = load_api_keys()

    openai_api_keys = api_keys['api_keys']['openai']
    huggingface_api_keys = api_keys['api_keys']['huggingface']

    print(f"OpenAI API Key: {openai_api_key}")
    print(f"Huggingface API Key: {huggingface_api_key}")