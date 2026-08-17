"""BUILDING A NEURAL NETWORK"""
# %%
"""importing torch and its libraries"""
import torch
import torch.nn as nn
import torch.nn.functional as F
from sklearn.linear_model import LogesticRegression
#%%
"""importing neccessary libraries"""
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
from sklearn.model_selection import train_test_split
# %%
"""Creating a model class that inherits nn.module"""
class Model(nn.Module):
  """
  Input layer (4features of flowers)->
  hidden layer 1->
  hidden layer 2->
  output(3 classes of irir flowers)
  """
  def __init__(self, inFeatures=4, h1=8, h2=9, outFeature=3):
    super().__init__()
    self.fc1=nn.Linear(inFeatures, h1)
    self.fc2=nn.Linear(h1, h2)
    self.out=nn.Linear(h2, outFeature)

  """
  forward(): function used to pass forward the data from one layer to the next layer
             this helps us calculate the gradients which further will be used when we 
             do backpropogation 

  `relu` --> Rectified Linear Unit
    `if output < 0 return 0`
  """
  def forward(self, x):
    x=F.relu(self.fc1(x))
    x=F.relu(self.fc2(x))
    x=self.out(x)
    return x
# %%
"""Picking a random seed for randomization"""
torch.manual_seed(32)
# %%
"""creating an instance of our model"""
model=Model()
# %%
"""loading our dataset as PandasDataFrame"""
url = "https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv"
my_dataframe = pd.read_csv(url)

# %%
"""
Label Encoding
As the network cant be worked with string we gave them reference values
"""
my_dataframe['species'] = my_dataframe['species'].replace("setosa", 0.0)
my_dataframe['species'] = my_dataframe['species'].replace("versicolor", 1.0)
my_dataframe['species'] = my_dataframe['species'].replace("virginica", 2.0)

# %%
"""Chossing the input and output for our neural network"""
X=my_dataframe.drop('species', axis=1)
y=my_dataframe['species']

# %%
"""
Converting it to numpy strings and stripping away
the column names, index, and all pandas metadata.
"""
X=X.values
y=y.values
# %%
"""train test split"""
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=32)

# %%
"""Converting the Numpy array to tensors to feed them to the model"""
X_train=torch.FloatTensor(X_train)
X_test=torch.FloatTensor(X_test)

# %%
"""
We do this as after `.replace()` the column might already be a tensor
or might still be a NumPy array - so we defensevly check it first.

This is defensive process without it the code would work absolutley 
fine in our case
"""
if isinstance(y_train, torch.Tensor):
    y_train = y_train.long()
else:
    y_train = torch.LongTensor(y_train)

if isinstance(y_test, torch.Tensor):
    y_test = y_test.long()
else:
    y_test = torch.LongTensor(y_test)

# %%
"""
Set criterion of model to measure the error how far off the
predicted values are form the actual data

`criterion` is the loss function

Iris is a multi-class classification problem (3 classes: setosa, versicolor, virginica).
  `CrossEntropyLoss` internally does two things:
  Softmax - converts raw outputs to probabilities
  LogLoss - penalizes wrong predictions

  So you don't need to add a Softmax layer at the end of your model, `CrossEntropyLoss` handles it.
"""
criterion = nn.CrossEntropyLoss()

# %%
"""
Optimizer: Adam(Adaptive Moment Estimation)
  `torch.optim.Adam` - the optimization algorithm chosen
  - Adam stands for Adaptive Moment Estimation
  - It's the most popular optimizer because it automatically adjusts the learning rate for each parameter
  - Works well in most cases without much tuning

  `model.parameters()` - tells the optimizer which weights to update
  - These are all the learnable weights and biases inside your model
  - The optimizer needs this so it knows what to adjust

  `lr=0.01` - learning rate
  - Controls how big a step the optimizer takes when updating weights
  - Too high --> overshoots, model never converges
  - Too low --> learns too slowly

"""
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)
# %%
"""
Model Traning
  - Model goes through the data n number of times(epochs)
  - Model does the prediction
  - Calculate models loss by compare the actual vs predicted value
  - Add the Loss at every epoch
  - Print Epoch and Loss after 10 iterations
  - `optimizer.zero_grad()`: clears old gradients
  - `loss.backward()`: calculates new gradients
  - `optimizer.step()`: Adam adusts the weights
"""
epochs = 100
losses = []
for i in range(epochs):
  # Go forward
  y_pred = model.forward(X_train)

  loss = criterion(y_pred, y_train)
  
  losses.append(loss.detach().numpy())
    # - .detach() — removes the tensor from the computation graph
    # - .numpy() — converts to NumPy so it can be stored/plotted
  
  if i %10==0:
    print(f"Epoch: {i} and loss:{loss}")
    
  optimizer.zero_grad()
  
  loss.backward()
  
  optimizer.step()

# %%
"""Plotting a graph comparing loss and epoch"""
plt.plot(range(epochs), losses)
plt.ylabel("loss/error")
plt.xlabel("epoch")


























# %%
"""Model Evaluation"""
with torch.no_grad():# basically turning of the backpropogation
  y_predict = model.forward(X_test) # they are the features form our test set
  loss = criterion(y_predict, y_test) #Find the loss or error
print(loss)
# %%
correct = 0
print("TENSORS                                          PREDICTED         ACTUAL")
with torch.no_grad():
  for i, data in enumerate(X_test):
    y_val = model.forward(data)
    if y_test[i]==0:
      x="Setosa"
    elif y_test[i]==1:
      x="Versicolor"
    else:
      x="Virginica"
    if y_val.argmax().item()==0:
      y="Setosa"
    elif y_val.argmax().item()==1:
      y="Versicolor"
    else:
      y="Virginica"
    # will tell us what type of flower class oir
    print(f"{i+1}.) {str(y_val)} \t {x} \t {y}")
    # Correct or not
    if y_val.argmax().item() == y_test[i]:
      correct+=1
print(f"\n we got correct:{correct}")
# Higher number indicates that which flower will be choosesn

# %%
"""feeding data to the model"""
new_iris = torch.tensor([4.7, 3.2, 1.3, 0.2])


# %%
with torch.no_grad():
    y_val = model.forward(new_iris)
    pred = y_val.argmax().item()

    if pred == 0:
        print("It is a Setosa")
    elif pred == 1:
        print("It is a Versicolor")
    else:
        print("It is a Virginica")

# %% [markdown]
# ### saving and loading our model

# %%
# save our model's weight and biases that we have trained in form of dictionary
torch.save(model.state_dict(), "iris_model.pt")

# %%
# Loading the saved model
new_model = Model()
new_model.load_state_dict(torch.load("iris_model.pt"))

# %%
# Mkaing sure the model is loaded
new_model.eval()

# %%
new_iris = torch.tensor([4.7, 3.2, 1.3, 0.2])

# %%
with torch.no_grad():
  y_eval = new_model.forward(new_iris)
  pred = y_eval.argmax().item()
  if pred == 0:
    print("It is a Setosa")
  elif pred == 1:
    print("It is a Versicolor")
  else:
    print("It is a Virginica")