# Standard
from importlib import import_module

# Third-party
import torch

# Custom module & package
from utils.util_common import get_cli_args, read_yaml

def train():
    pass

def model_setup(config_model: dict)-> torch.nn.Module:
    module = import_module(f"model.{config_model['pname']}")
    model = getattr(module, config_model['cname'])(config_model['pretrained'])
    return model

def param_setup():
    pass
    # loss = loss_setup()
    # optimizer = optimizer_setup()
    # scheduler = scheduler_setup()
    # return loss, optimizer

if __name__ == "__main__":
    args = get_cli_args()
    config = read_yaml(args.config)
    model = model_setup(config['model'])
    
    