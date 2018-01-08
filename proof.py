import matplotlib.pyplot as plt 
import numpy as np 
import math as m

Samples = [5,100,200,500,900]

Range = 3.0

R1 = np.arange(0.0, Range+Range/Samples[0], Range/Samples[0])
R2 = np.arange(0.0, Range, Range/Samples[1])
R3 = np.arange(0.0, Range, Range/Samples[2])
R4 = np.arange(0.0, Range, Range/Samples[3])
R5 = np.arange(0.0, Range, Range/Samples[4])



def sin(t):
	return np.sin(2*np.pi*t)

def Sin(k,t):
	return np.sin(2*np.pi*k*t)

plt.figure(1)
plt.subplot(211)
plt.plot(R1,sin(R1),'bo',R2,sin(R2),'r--')
plt.stem(R1,sin(R1))
plt.title(r'expected fundamental',fontsize=10)


plt.subplot(212)
plt.plot(R1,sin(R1),'bo',R2,sin(R2),'r--',R3,Sin(-0.666,R3),'g--')
plt.stem(R1,sin(R1))
plt.title(r'extracted fundamental',fontsize=10)





plt.show()

