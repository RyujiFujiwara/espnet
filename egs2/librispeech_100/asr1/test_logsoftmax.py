import torch
import math

y = torch.tensor([0.5,0.4,0.6])
y = torch.log(y)
y_s = torch.exp(y)
y_t = [math.exp(x) for x in y]

print(y_s)
print(y_t)
print(math.prod(y_s))