import matplotlib.pyplot as plt
from numpy import *
import numpy as np
import pandas as pd


def equation(x):
    return x**3 - x-1


decimal = 4
df = pd.DataFrame(columns=['a', 'b', 'x', 'f(x)', 'Remarks'])
error = 1/2*10**-decimal

print("Maximum error = ", error)
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
        df.loc[i, ['Remarks']] = 'f(x)>0, replace b by x'
    else:
        a = x
        df.loc[i, ['Remarks']] = 'f(x)<0 replace a by x'

    result = x
    if (i != 0):

        if df['f(x)'].iloc[i] == df['f(x)'].iloc[i-1] or abs(y) < error:
            break

print(df)
print(x)


# Creating vectors X and Y
x1 = np.linspace(-2, 2, 100)
y1 = x1**3 - x1-1
y2 = 0*x1

fig = plt.figure(figsize=(10, 5))
# Create the plot
plt.plot(x1, y1)
plt.plot(x1, y2)
plt.scatter(x, equation(x), cmap='green')
plt.title("Bisection Method")

# Show the plot
plt.show()
