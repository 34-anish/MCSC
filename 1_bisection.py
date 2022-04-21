import matplotlib.pyplot as plt
import seaborn
from matplotlib.pyplot import plot, show
from numpy import *
import numpy as np
import pandas as pd


def equation(x):
    return x**3 - x-1


decimal = 4
df = pd.DataFrame(columns=['a', 'b', 'x', 'f(x)'])
error = 1/2*10**-decimal
print(error)
a = 1
b = 2
for i in range(15):
    df.loc[i, ['a']] = a
    df.loc[i, ['b']] = b
    x = round((a+b)/2, decimal+1)
    df.loc[i, ['x']] = x
    y = round(equation(x), decimal+1)

    df.loc[i, ['f(x)']] = y
    if y > 0:
        b = x
    else:
        a = x

    result = x
    if abs(y) < error:
        break
print(df)
print(x)


# Import libraries

# Creating vectors X and Y
x = np.linspace(-2, 2, 100)
y = x**3 - x-1

fig = plt.figure(figsize=(10, 5))
# Create the plot
plt.plot(x, y)
plt.scatter(x, y)

# Show the plot
plt.show()
