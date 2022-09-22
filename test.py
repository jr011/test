from torch import nn
import torch
import torch.nn.functional as F

# rnn = nn.LSTM(10, 20, 2)
# input = torch.randn(5, 3, 10)
# h0 = torch.randn(2, 3, 10)
# c0 = torch.randn(2, 3, 10)
# output, (hn, cn) = rnn(input, (h0, c0))  # output(5,3,20)
# print(output.shape)


class DropoutFC(nn.Module):
    def __init__(self):
        super(DropoutFC, self).__init__()
        self.fc = nn.Linear(100,20)

    def forward(self, input):
        out = self.fc(input)
        out = F.dropout(out, p=0.5)
        return out

device = 'cuda'

Net = DropoutFC().to(device)
Net.train()
input = torch.randn(100,device='cuda')
out = Net(input)
