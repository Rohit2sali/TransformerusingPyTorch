import torch
import torch.nn as nn
class LayerNorm(nn.Module):
    def __init__(self, d_model, eps): 
        super(LayerNorm, self).__init__()
        self.eps = eps 

        self.gamma = nn.Parameter(torch.ones(d_model))
        self.beta = nn.Parameter(torch.ones(d_model))

    def forward(self, input): 
        input = input.to(torch.float32)
        mean = torch.mean(input, dim=2, keepdim=True)
        std = torch.std(input, dim=2, keepdim=True)
        input = ((input - mean)/(std - self.eps) * self.gamma) + self.beta
        return input
