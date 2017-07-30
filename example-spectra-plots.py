from solver import Evolve_RG
import numpy as np
import matplotlib.pyplot as plt
from constants import *
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

env=Evolve_RG.load('example-beta.pickle')

plt.subplot(1,2,1)
nfreq=len(env.freqs)
tv=env.tv
lums=np.zeros_like(env.corrs)
for i in range(nfreq):
    lums[:,i]=env.synch*(env.freqs[i]/env.nu_ref)**-env.alpha*env.corrs[:,i]
    plt.plot(tv/Myr,lums[:,i],label='%.0f MHz' % (env.freqs[i]/1e6))
plt.xscale('log')
plt.yscale('log')
plt.legend(loc=0)
plt.xlabel('Time (Myr)')
plt.subplot(1,2,2)
for i in range(1,nfreq):
    plt.plot(tv/Myr,-np.log(lums[:,i]/lums[:,i-1])/np.log(env.freqs[i]/env.freqs[i-1]),label='$\\alpha_{%.0f}^{%.0f}$' % (env.freqs[i]/1e6,env.freqs[i-1]/1e6))
plt.xscale('log')
plt.legend(loc=0)
plt.xlabel('Time (Myr)')

plt.show()
