from solver import Evolve_RG
import numpy as np
import matplotlib.pyplot as plt
from synch_constants import *
from matplotlib import rc
from matplotlib.lines import Line2D

rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

fig = plt.figure()

#ls = ['univ-1e13', 'univ-1e14', 'univ-1e15']

#We procedurally generate the names of the pickle files
Q = 2e46*ergpersec
l = 'univ-1e14'
names = 'example-'+l+'-Q-'+f'{Q:.1e}'+'.pickle'

env= Evolve_RG.load(names)

#We decalre different zs
zs = [0, 0.2, 0.5, 1]
colors_z = ['hotpink', 'seagreen', 'firebrick', 'royalblue']

for z,c in zip(zs,colors_z):
    #z = zs[0]
    #c = colors_z[0]
    env.z=z

    env.finds_loss()
    env.findic_loss()
    env.findbs_loss()

    env.findlosscorrection()

    plt.plot(env.tv/Myr,env.loss*env.losscorrs,label='Synchrotron',color=c,ls='--')
    plt.plot(env.tv/Myr,env.ic_loss*env.losscorrs,label='Inverse-Compton',color=c,ls='-.')
    plt.plot(env.tv/Myr,env.bs_loss,label='Bremsstrahlung',color='black',ls=':')

plt.plot(env.tv/Myr,len(env.tv)*[env.Q],ls='-',label='Input power',color='black')

legend_handles = [Line2D([0], [0], color=c, lw=2) for c in colors_z]
legend_labels = ['$z = ' + f'{z:.1f}' + '$' for z in zs]
fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 0.985), ncol=len(zs), fontsize='small')

linetype = ['-','--','-.',':']
legend_handles = [Line2D([0], [0], color='black', ls=lt, lw=2) for lt in linetype]
legend_labels = ['Input power', 'Synchrotron', 'Inverse-Compton', 'Bremsstrahlung']
plt.legend(legend_handles, legend_labels, loc='lower right', fontsize='small')

plt.xscale('log')
plt.yscale('log')
plt.xlim((1e-4,300))
plt.ylim((1e31,3e39))
plt.ylabel('Power (W)')
plt.xlabel('Time (Myr)')
plt.savefig('figures/fig_7_plot_losses_many_z.pdf')
