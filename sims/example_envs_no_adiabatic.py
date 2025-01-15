# Plot a couple of pressure profiles

from synch_constants import *
from solver import Evolve_RG
import numpy as np
import os.path

xi=0.4
q=2.1
labels=['univ-1e13', 'univ-1e14', 'univ-1e15']
envs=[Evolve_RG('universal',M500=1e13,xi=xi,q=q), Evolve_RG('universal',M500=1e14,xi=xi,q=q), Evolve_RG('universal',M500=1e15,xi=xi,q=q)]

tmin=0
tmax=300
tv=np.logspace(-5,np.log10(tmax),100)*Myr
Q = 2e46*ergpersec

#primero, calculamos para cada modelo la correction no adiabatica
for env,l, in zip(envs,labels):
    inname='example-'+l+'-Q-'+f'{Q:.1e}'+'.pickle'
    outname='example-'+l+'-Q-'+f'{Q:.1e}'+'-noad'+'.pickle'
    if os.path.isfile(inname):
        env=Evolve_RG.load(inname)
    else:
        env.solve(Q,tv)
    env.findb()
    env.findsynch(150e6)
    env.findcorrection((150e6,330e6,1.4e9,5e9,8e9,15e9),do_adiabatic=False)
    env.save(outname)
