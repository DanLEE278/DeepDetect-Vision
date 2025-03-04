# Standard

# Third-party
import torch
import torch.nn as nn
import torch.nn.functional as F

from timm.models import create_model

class RepLKNetDetector(nn.Module):
    def __init__(self):
        super().__init__()
        self.backbone = create_model("replknet_v2_50", pretrained=True)
        self.backbone = torch.hub.load("facebookresearch/maws", model="vit_b16_maws")
        self.fc = None
        print("load complete")
    
    def forward(self):
        pass