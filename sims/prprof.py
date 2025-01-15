# Plot a couple of pressure profiles

import matplotlib.pyplot as plt
from synch_constants import *
from solver import Evolve_RG
import numpy as np

from matplotlib import rc
rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

labels=['$M_{500} = 10^{13}$ M$_{\odot}$','$M_{500} = 10^{14}$ M$_{\odot}$','$M_{500} = 10^{15}$ M$_{\odot}$']
colours=['blue','violet', 'red']
envs=[Evolve_RG('universal',M500=1e13), Evolve_RG('universal',M500=1e14), Evolve_RG('universal',M500=1e15)]

dist=np.logspace(-3,3.3,100)
for env,l,c in zip(envs,labels,colours):
    plt.plot(dist,env.pr(dist*kpc),label=l,color=c)
plt.xlabel('Distance (kpc)')
plt.ylabel('Pressure (Pa)')
plt.xscale('log')
plt.yscale('log')
#plt.grid(linewidth=0.1)
plt.legend(loc=0)
plt.tight_layout()
plt.savefig('figures/fig_1_prprof.pdf')
