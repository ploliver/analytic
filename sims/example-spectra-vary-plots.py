from solver import Evolve_RG
import numpy as np
import matplotlib.pyplot as plt
from synch_constants import *
from matplotlib import rc
from matplotlib.lines import Line2D

rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

#First, we are going to plot the same plot but for z \in {0, 0.2, 0.5, 1, 2}
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5.5))

done_uncorr=False

#We procedurally generate the names of the pickle files
Q=2e46*ergpersec 
zs = [0, 0.2, 0.5, 1]
ls = ['univ-1e13', 'univ-1e14', 'univ-1e15']
c_ls = ['blue','violet', 'red']
alph_zs = [0.9, 0.75, 0.6, 0.45]
names = [] 
labels = []
plot_uncorrected=[]
colors = []
alphas = []
for i in range(-1, 4):
    for l, c in zip(ls, c_ls):
        if i == -1:
            name='example-'+l+'-Q-'+f'{Q:.1e}'+'-noad.pickle'
            label="150 MHz uncorrected"
            plot_uncorrected.append(True)
            alphas.append(1)
        else:
            name='example-'+l+'-Q-'+f'{Q:.1e}'+'-z-'+f'{zs[i]:.1f}'+'.pickle'
            label='$z = ' + f'{zs[i]:.1f}$'
            plot_uncorrected.append(False)
            alphas.append(alph_zs[i])
        names.append(name)
        labels.append(label)
        colors.append(c)

for name,label,pu,c,a in zip(names,labels,plot_uncorrected,colors,alphas):
    env=Evolve_RG.load(name)
    nfreq=len(env.freqs)
    tv=env.tv
    lums=np.zeros_like(env.corrs)
    if pu:
        ax1.plot(tv/Myr,env.synch,ls='--',color=c,label='uncorrected' +name)
    else:
        for i in range(nfreq):
            lums[:,i]=env.synch*(env.freqs[i]/env.nu_ref)**-env.alpha*env.corrs[:,i]
    ploti=0
    ax1.plot(tv/Myr,lums[:,ploti],label=label, color=c, alpha=a)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    lines = [Line2D([0], [0], color=c, linestyle='-') for c in c_ls]
    labels = ['$M_{500} = 1 \\times 10^{13}$', '$M_{500} = 1 \\times 10^{14}$', '$M_{500} = 1 \\times 10^{15}$']
    ax1.legend(lines, labels, fontsize='small')
    ax1.set_xlabel('Time (Myr)')
    ax1.set_ylabel('Radio luminosity (W Hz$^{-1}$)')

    if pu:
        ax2.plot(tv/Myr,[0.55]*len(tv),ls='--',color=c,label='150 MHz uncorrected')
    else: 
        ploti=1
        ax2.plot(tv/Myr,-np.log(lums[:,ploti]/lums[:,ploti-1])/np.log(env.freqs[ploti]/env.freqs[ploti-1]),label=label, color=c, alpha=a)
    lines = [Line2D([0], [0], color=c, linestyle='-') for c in c_ls]
    labels = ['$M_{500} = 1 \\times 10^{13}$', '$M_{500} = 1 \\times 10^{14}$', '$M_{500} = 1 \\times 10^{15}$']
    ax2.legend(lines, labels, fontsize='small')
    ax2.set_xscale('log')
    ax2.set_xlabel('Time (Myr)')
    ax2.set_ylabel('Spectral index 150-330 MHz')

plt.tight_layout()
plt.savefig('figures/fig_4_example-spectra-vary_M.pdf')

#Redo the plot but varying Q for M_500 = 1e14
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12,5.5))

# inset Axes to zoom in on the image
x1, x2, y1, y2 = 8e1, 4e2, 0.81, 1.01 # subregion of the original image
axins = ax2.inset_axes(
    [0.3, 0.3, 0.2, 0.68], #x0, y0, width, height
    xlim=(x1, x2), ylim=(y1, y2), xticklabels=[], yticklabels=[])
axins.set_yscale('log')
axins.set_xscale('log')
axins.get_xaxis().set_visible(False)
axins.get_yaxis().set_visible(False)

done_uncorr=False

#We procedurally generate the names of the pickle files
Qmin = 2e42*ergpersec
Qmax = 2e46*ergpersec
nQ = 5
Qs = [Qmin*10**i for i in range(nQ)]
zs = [0, 0.2, 0.5, 1]
l = 'univ-1e14'
c_Qs = ['red','orange','green','blue','purple']

alph_zs = [0.9, 0.75, 0.6, 0.45]
names = [] 
labels = []
plot_uncorrected=[]
colors = []
alphas = []
for i in range(4):
    for Q, c in zip(Qs, c_Qs):
        if i == -1:
            name='example-'+l+'-Q-'+f'{Q:.1e}'+'-noad.pickle'
            label="150 MHz uncorrected"
            plot_uncorrected.append(True)
            alphas.append(1)
        else:
            name='example-'+l+'-Q-'+f'{Q:.1e}'+'-z-'+f'{zs[i]:.1f}'+'.pickle'
            label='$z = ' + f'{zs[i]:.1f}$'
            plot_uncorrected.append(False)
            alphas.append(alph_zs[i])
        names.append(name)
        labels.append(label)
        colors.append(c)

for name,label,pu,c,a in zip(names,labels,plot_uncorrected,colors,alphas):
    env=Evolve_RG.load(name)
    nfreq=len(env.freqs)
    tv=env.tv
    lums=np.zeros_like(env.corrs)
    if pu:
        ax1.plot(tv/Myr,env.synch,ls='--',color=c,label='uncorrected' +name)
    else:
        for i in range(nfreq):
            lums[:,i]=env.synch*(env.freqs[i]/env.nu_ref)**-env.alpha*env.corrs[:,i]
    ploti=0
    ax1.plot(tv/Myr,lums[:,ploti],label=label, color=c, alpha=a)
    ax1.set_xscale('log')
    ax1.set_yscale('log')
    lines = [Line2D([0], [0], color="black", alpha=a, linestyle='-') for a in alph_zs]
    labels = ['$z = ' + f'{z:.1f}' + '$' for z in zs]
    ax1.legend(lines, labels, fontsize='small')
    ax1.set_xlabel('Time (Myr)')
    ax1.set_ylabel('150-MHz radio luminosity (W Hz$^{-1}$)')
    if pu:
        ax2.plot(tv/Myr,[0.55]*len(tv),ls='--',color=c,label='150 MHz uncorrected')
    else: 
        ploti=1
        ax2.plot(tv/Myr,-np.log(lums[:,ploti]/lums[:,ploti-1])/np.log(env.freqs[ploti]/env.freqs[ploti-1]),label=label, color=c, alpha=a)
        axins.plot(tv/Myr,-np.log(lums[:,ploti]/lums[:,ploti-1])/np.log(env.freqs[ploti]/env.freqs[ploti-1]),label=label, color=c, alpha=a)
    lines = [Line2D([0], [0], color="black", alpha=a, linestyle='-') for a in alph_zs]
    labels = ['$z = ' + f'{z:.1f}' + '$' for z in zs]
    ax2.legend(lines, labels, fontsize='small')
    ax2.set_xscale('log')
    ax2.set_xlabel('Time (Myr)')
    ax2.set_ylabel('Spectral index 150-330 MHz') 

legend_handles = [Line2D([0], [0], color=c, lw=2) for c in colors]
legend_labels = ['$Q = 2 \\times 10^{' + f'{int(np.log10(Qs[i]/2)):02d}' + '}$ W' for i in range(len(Qs))]
fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=len(Qs), fontsize='small')

ax2.indicate_inset_zoom(axins, edgecolor="black")

plt.tight_layout()
plt.subplots_adjust(top=0.915)  # Increase the top margin to make space for the legend
plt.savefig('figures/fig_4_example-spectra-vary_Q.pdf')
