import torch

y = torch.ones(3,3,5,requires_grad=True)
y = torch.log_softmax(y, dim=1)
y = torch.exp(y)
print(torch.empty(0))

print(y)