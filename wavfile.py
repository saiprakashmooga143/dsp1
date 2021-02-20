import numpy as np 
import scipy.io.wavfile
from matplotlib import pyplot as plt
fs,s=scipy.io.wavfile.read('100001.wav')
print(fs)
plt.plot(s)
plt.show()
