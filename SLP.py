import torch

class SLP(torch.nn.Module):
    """
    A single Layer perceptron class to approximate functions
    """
    def __init__(self,input_shape,output_shape,device = torch.device('cpu')):
        """
        Parameters:
        1. input_shape : Shape/dimension of the inpput
        2. output_shape : shape/dimesnion of the output
        3. device : cpu or cuda device
        """
        super(SLP,self).__init__()
        self.device = device
        self.input_shape = input_shape[0]
        self.hidden_shape = 40
        self.linear1 = torch.nn.Linear(self.input_shape,self.hidden_shape)
        self.out = torch.nn.Linear(self.hidden_shape,output_shape)

    def forward(self,x):
        x = torch.from_numpy(x).float().to(self.device)
        x = torch.nn.functional.relu(self.linear1(x))
        x = self.out(x)
        return x