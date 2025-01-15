from solver import Evolve_RG
import matplotlib.pyplot as plt
from synch_constants import *
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

q=2.1
labels=['univ-1e13', 'univ-1e14', 'univ-1e15']
Qmin = 2e42*ergpersec
Qmax = 2e46*ergpersec
nQ = 5
Qs = [Qmin*10**i for i in range(nQ)]
zs = [0, 0.2, 0.5, 1, 2]

#first, for each Q and M500 = 1e14, z = 0
l = 'univ-1e14'
z = 0
names = ['example-tstop-'+l+'Q-'+f'{Q:.1e}'+'.pickle'for Q in Qs]

fig = plt.figure(figsize=(12,5.5))

for name in names:
    env=Evolve_RG.load(name)
    env.gmin=10
    env.gmax=1e6
    env.q=q
    plt.xlim(0,300)
    env.findsynch(150e6)
    env.findic(2.4e17,z=z)
    if z>0:
        env.findcorrection([150e6],z=z,do_adiabatic=True)
    env.ic_findcorrection([2.4e17],z=z,do_adiabatic=True)
    
    plt.plot(env.tv/Myr,env.corr_synch[:,0]/1e10,label='Synchrotron (scaled)')
    plt.plot(env.tv/Myr,env.ic,label='IC uncorrected')
    plt.plot(env.tv/Myr,env.corr_ic[:,0],label='IC corrected')
    plt.legend(loc=0)
    plt.xlabel('Time (Myr)')
    plt.ylabel('Luminosity (W Hz$^{-1}$)')
    plt.yscale('log')
    plt.ylim((1e16,3.5e20))

plt.tight_layout()
plt.savefig('figures/fig_7_remnant_ic.pdf')
plt.show()
