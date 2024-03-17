#Try testing with simple operations (like tensor addition) to confirm GPU usage.
import torch
print(torch.cuda.is_available())

# Create two tensors.
a = torch.rand(1000, 1000, device="cuda")
b = torch.rand(1000, 1000, device="cuda")

# Perform addition on the GPU.
c = a + b
print(c)

