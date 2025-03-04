# Standard

# Third-party
import torch
import torch.nn as nn
import torch.nn.functional as F

from transformers import BeitFeatureExtractor, BeitForImageClassification

class BeitDetector(nn.Module):
    def __init__(self, pretrained):
        super().__init__()
        
        if pretrained:
            self.feature_extractor = BeitFeatureExtractor.from_pretrained(pretrained)
            self.classifier = BeitForImageClassification.from_pretrained(pretrained)
        else:
            self.feature_extractor = BeitFeatureExtractor.from_pretrained(pretrained)
            self.classifier = BeitForImageClassification.from_pretrained(pretrained)
        
    def forward(self, x):
        feature = self.backbone(x)