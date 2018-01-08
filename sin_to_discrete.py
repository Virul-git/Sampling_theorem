import matplotlib.pyplot as plt 
import numpy as np 
import math as m

Samples = [5,500,500,500,500]

Range = 1.0

R1 = np.arange(0.0, Range, Range/Samples[0])
R2 = np.arange(0.0, Range, Range/Samples[1])
R3 = np.arange(0.0, Range, Range/Samples[2])
R4 = np.arange(0.0, Range, Range/Samples[3])
R5 = np.arange(0.0, Range, Range/Samples[4])



def sin(t):
	return np.sin(2*np.pi*t)

def Sin(k,t):
	return np.sin(2*np.pi*k*t)


def d_sin(n_sines):
	d_sin = np.zeros(Samples[2])
	for j in range(n_sines):
		d_sin = d_sin+Sin(((-1**j)*((j//2)*5)+1),R2)
	d_sin = d_sin/n_sines
	return d_sin

plt.figure(1)
plt.subplot(221)
plt.plot(R1,sin(R1),'bo',R2,d_sin(5),'k--')
plt.title(r'5 sine waves',fontsize=10)

plt.subplot(222)
plt.plot(R1,sin(R1),'bo',R2,d_sin(10),'k--')
plt.title(r'10 sine waves',fontsize=10)


plt.subplot(223)
plt.plot(R1,sin(R1),'bo',R2,d_sin(20),'k--')
plt.title(r'20 sine waves',fontsize=10)


plt.subplot(224)
plt.plot(R1,sin(R1),'bo',R2,d_sin(200),'k--')
plt.title(r'200 sine waves',fontsize=10)



plt.show()

