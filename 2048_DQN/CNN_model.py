import torch
import torch.nn as nn
import torch.nn.functional as F
import torch.optim as optim
import numpy as np
from tqdm import tqdm
import random

class Deep_CNN(nn.Module):
    def __init__(self):
        super(Deep_CNN,self).__init__()
        #input is 16x4x4
        self.conv1 = nn.Conv2d(16, 32, kernel_size=2, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=2, stride=1)
        self.droupout1 = nn.Dropout(0.2)
        self.conv3 = nn.Conv2d(64, 200, kernel_size=2, stride=1)
        self.droupout2 = nn.Dropout(0.2)
        
        #200 x 1 x 1

        self.deep1 = nn.Linear(200,128)
        self.deep2 = nn.Linear(128,32)
        self.deep3 = nn.Linear(32,4)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.droupout1(x)
        x = F.relu(self.conv3(x))
        x = self.droupout2(x)
        x = x.view(x.size(0), -1) 
        x = F.relu(self.deep1(x))
        x = F.relu(self.deep2(x))
        return self.deep3(x) 
    
class Deep_CNN(nn.Module):
    def __init__(self):
        super(Deep_CNN,self).__init__()
        #input is 16x4x4
        self.conv1 = nn.Conv2d(16, 32, kernel_size=2, stride=1)
        self.conv2 = nn.Conv2d(32, 64, kernel_size=2, stride=1)
        self.droupout1 = nn.Dropout(0.2)
        self.conv3 = nn.Conv2d(64, 200, kernel_size=2, stride=1)
        self.droupout2 = nn.Dropout(0.2)
        
        #200 x 1 x 1

        self.deep1 = nn.Linear(200,128)
        self.deep2 = nn.Linear(128,32)
        self.deep3 = nn.Linear(32,4)

    def forward(self, x):
        x = F.relu(self.conv1(x))
        x = F.relu(self.conv2(x))
        x = self.droupout1(x)
        x = F.relu(self.conv3(x))
        x = self.droupout2(x)
        x = x.view(x.size(0), -1) 
        x = F.relu(self.deep1(x))
        x = F.relu(self.deep2(x))
        return self.deep3(x) 