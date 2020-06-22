import torch

a = torch.full([4],1/4.)
print(a)

a*torch.log2(a)

