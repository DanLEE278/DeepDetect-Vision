# Standard
import argparse
import yaml

# Third-party


def get_cli_args()-> argparse:
    parser = argparse.ArgumentParser(description="Vision Deepfake Detection")
    parser.add_argument("--config",
                        "-c",
                        default="config/beit.yaml")
    return parser.parse_args()

def read_yaml(path_yaml:str)-> dict:
    with open(path_yaml, 'r') as file:
        config = yaml.safe_load(file)
    return config