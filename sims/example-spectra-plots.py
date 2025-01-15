from solver import Evolve_RG
import numpy as np
import matplotlib.pyplot as plt
from synch_constants import *
from matplotlib import rc
from matplotlib.lines import Line2D

rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

legend_handles = []
legend_labels = []

axes=[]
naxes=2
fig = plt.figure(figsize=(12,5))
for i in range(naxes):
    axes.append(plt.subplot(1,naxes,i+1))
for ax in axes:
    ax.set_xscale('log')
    ax.set_yscale('log')

colors=['red','orange','green','blue','purple']

labels=['univ-1e13', 'univ-1e14', 'univ-1e15']
Qmin = 2e42*ergpersec
Qmax = 2e46*ergpersec
nQ = 5
Qs = [Qmin*10**i for i in range(nQ)]

#First, we do the plot for the univ-1e14 model for all the Qs
l = 'univ-1e14'
envs=[Evolve_RG.load('example-'+l+'-Q-'+f'{Q:.1e}'+'.pickle') for Q in Qs]

#plt.figure(figsize=(12,5.5))
#plt.subplot(1,2,1)

#The joint plot is here just for reference if we need it to plot the spectral index
l = 'univ-1e14'
for Q,c in zip(Qs, colors):
    env=Evolve_RG.load('example-'+l+'-Q-'+f'{Q:.1e}'+'.pickle')
    nfreq=len(env.freqs)
    alphas = [(1/(i+1))**0.5 for i in range(nfreq)]
    tv=env.tv
    lums=np.zeros_like(env.corrs)
    axes[0].plot(tv/Myr,env.synch,ls='--',color='black',label='150 MHz uncorrected')
    for i in range(nfreq):
        lums[:,i]=env.synch*(env.freqs[i]/env.nu_ref)**-env.alpha*env.corrs[:,i]
    for i in range(0, nfreq):
        axes[0].plot(tv/Myr,lums[:,i],label='%.0f MHz' % (env.freqs[i]/1e6), alpha=alphas[i], color=c)
    plt.xscale('log')
    plt.yscale('log')
    plt.legend(loc=0,fontsize='small')
    plt.xlabel('Time (Myr)')
    plt.ylabel('Radio luminosity (W Hz$^{-1}$)')
    for i in range(1,nfreq):
        axes[1].plot(tv/Myr,-np.log(lums[:,i]/lums[:,i-1])/np.log(env.freqs[i]/env.freqs[i-1]),label='$\\alpha_{%.0f}^{%.0f}$' % (env.freqs[i]/1e6,env.freqs[i-1]/1e6), alpha=alphas[i-1], color=c)
plt.xscale('log')
plt.legend(loc=0,fontsize='small')
plt.xlabel('Time (Myr)')
plt.ylabel('Spectral index')

# Create a legend above all subplots for Q values and colors
legend_handles = [Line2D([0], [0], color=c, lw=2) for c in colors]
legend_labels = ['$Q = 2 \\times 10^{' + f'{int(np.log10(Qs[i]/2)):02d}' + '}$ W' for i in range(len(Qs))]
fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=len(Qs), fontsize='small')

#plt.tight_layout()
# Adjust the layout to make space for the legend
#plt.subplots_adjust(top=0.95)  # Increase the top margin to make space for the legend
plt.savefig('figures/fig_z_example-spectra.pdf')

#Redo the plot but only the radio luminosity
plt.figure()
legend_handles = []
legend_labels = []
for Q,c in zip(Qs, colors):
    env=Evolve_RG.load('example-'+l+'-Q-'+f'{Q:.1e}'+'.pickle')
    nfreq=len(env.freqs)
    alphas = [(1/(i+1))**0.5 for i in range(nfreq)]
    tv=env.tv
    lums=np.zeros_like(env.corrs)
    plt.plot(tv/Myr,env.synch,ls='--',color='black',label='150 MHz uncorrected')
    legend_handles.append(plt.Line2D([0], [0], color=c, lw=2))
    legend_labels.append('$Q = ' + f'{Q/10**int(np.log10(Q)):.1f}' +'\\times 10^{'+str(int(np.log10(Q)))+'}$ W')
    for i in range(nfreq):
        lums[:,i]=env.synch*(env.freqs[i]/env.nu_ref)**-env.alpha*env.corrs[:,i]
    for i in range(0, nfreq):
        plt.plot(tv/Myr,lums[:,i],label='%.0f MHz' % (env.freqs[i]/1e6), alpha=alphas[i], color=c)
legend_handles.append(plt.Line2D([0], [0], color="black", lw=2, ls='--'))
legend_labels.append('Uncorrected')
plt.xscale('log')
plt.yscale('log')
plt.legend(legend_handles, legend_labels, loc='lower right', ncol=2, fontsize='small')
#plt.legend(loc=0,fontsize='small')
plt.xlabel('Time (Myr)')
plt.ylabel('Radio luminosity (W Hz$^{-1}$)')
plt.subplots_adjust(top=0.95)  # Increase the top margin to make space for the legend
#plt.grid(linewidth=0.1)
plt.tight_layout()
plt.savefig('figures/fig_4_radio-luminosity.pdf')

#Redo the plot but changing models for constant Q
plt.figure()
Q=2e46*ergpersec
M_500_pow_start = 13
legend_handles = []
legend_labels = []
colors=['blue','violet', 'red']
for l,c in zip(labels, colors):
    env=Evolve_RG.load('example-'+l+'-Q-'+f'{Q:.1e}'+'.pickle')
    nfreq=len(env.freqs)
    alphas = [(1/(i+1))**0.5 for i in range(nfreq)]
    tv=env.tv
    lums=np.zeros_like(env.corrs)
    plt.plot(tv/Myr,env.synch,ls='--',color=c,label='150 MHz uncorrected')
    legend_handles.append(plt.Line2D([0], [0], color=c, lw=2))
    legend_labels.append('$M_{500} = 10^{' + str(M_500_pow_start) + '}\, M_{\\odot}$')
    M_500_pow_start += 1
    for i in range(nfreq):
        lums[:,i]=env.synch*(env.freqs[i]/env.nu_ref)**-env.alpha*env.corrs[:,i]
    for i in range(0, nfreq, 2):
        plt.plot(tv/Myr,lums[:,i],label='%.0f MHz' % (env.freqs[i]/1e6), alpha=alphas[i], color=c) 
        print(env.freqs[i]/1e6)
legend_handles.append(plt.Line2D([0], [0], color="black", lw=2, ls='--'))
legend_labels.append('No adiabatic correction')
plt.xscale('log')
plt.yscale('log')
plt.legend(legend_handles, legend_labels, loc='lower left', ncol=2, fontsize='small')
#plt.legend(loc=0,fontsize='small')
plt.xlabel('Time (Myr)')
plt.ylabel('Radio luminosity (W Hz$^{-1}$)')
plt.subplots_adjust(top=0.95)  # Increase the top margin to make space for the legend
#plt.grid(linewidth=0.1)
plt.tight_layout()
plt.savefig('figures/fig_4_radio-luminosity_z.pdf')

#clear the figure
# plt.figure()
# for env in envs:
#     plt.plot(env.R/kpc,env.B)
# plt.xscale('log')
# plt.yscale('log')
# plt.savefig('figures/fig_4_Bvst.pdf')