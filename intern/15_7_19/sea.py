import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
def sinplot( flip =1):
    x = np.linspace(0,14,100)
    for  i in range(1,100):
        plt.plot(x,np.sin(x+i*.5)*(7- i )*flip)

sns.set()
sinplot()