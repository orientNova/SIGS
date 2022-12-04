import torch.nn as nn
import torch.nn.functional as F

class LeNet(nn.Module): #继承nn.Module
    def __init__(self):
        super(LeNet, self).__init__()           #多继承问题 待查
        self.conv1 = nn.Conv2d(3, 16, 5)        #彩色图片3通道 16卷积核 卷积核大小5 (32-5-2*0)/1+1=28
        self.pool1 = nn.MaxPool2d(2, 2)         #池化核2 stride=2 图像边长缩小为1/2 28*28->16*16
        self.conv2 = nn.Conv2d(16, 32, 5)
        self.pool2 = nn.MaxPool2d(2, 2)
        self.fc1 = nn.Linear(32*5*5, 120)       #展平之后输入进全连接层
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, 10)

    def forward(self, x):            #正向传播过程
        x = F.relu(self.conv1(x))    # input(3, 32, 32) output(16, 28, 28)
        x = self.pool1(x)            # output(16, 14, 14)
        x = F.relu(self.conv2(x))    # output(32, 10, 10)
        x = self.pool2(x)            # output(32, 5, 5)
        x = x.view(-1, 32*5*5)       # output(32*5*5)           #展平操作 -1第一个维度 
        x = F.relu(self.fc1(x))      # output(120)
        x = F.relu(self.fc2(x))      # output(84)
        x = self.fc3(x)              # output(10)
        return x

#测试
'''
import torch
input1 = torch.rand([32,3,32,32]) #batch depth height width
model = LeNet()
print(model)
output1 = model(input1)
'''


#LeNet结构
'''

(3, 32, 32)                 图像RGB 3通道32*32
----------conv1----------
----------relu----------
(16, 28, 28)
----------pool1----------
(16, 14, 14)
----------conv2----------
----------relu----------
(32, 10, 10)
----------pool2----------
(32, 5, 5)                  展平之后输入进全连接层
----------fc1----------
----------relu----------
(120)
----------fc2----------
----------relu----------
(84)
----------fc3----------
(10)

'''



'''
卷积尺寸计算
O = (I - K + 2*P)/S + 1
Output = (Input - Kernel + 2*Padding)/Stride + 1

#Conv2d
torch.nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0, 
dilation=1, groups=1, bias=True, padding_mode='zeros', device=None, dtype=None)

#MaxPool2d 
torch.nn.MaxPool2d(kernel_size, stride=None, padding=0, dilation=1, 
return_indices=False, ceil_mode=False)

#Linear
torch.nn.Linear(in_features, out_features, 
bias=True, device=None, dtype=None)


'''
