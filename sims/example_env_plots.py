from solver import Evolve_RG
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from synch_constants import *
from matplotlib import rc

rc('font',**{'family':'serif','serif':['Times'],'size':14})
rc('text', usetex=True)

axes=[]
naxes=4
fig = plt.figure(figsize=(12,9))
for i in range(naxes):
    axes.append(plt.subplot(naxes//2,naxes//2,i+1))
for ax in axes:
    ax.set_xscale('log')

axes[0].set_yscale('log')
axes[2].set_yscale('log')

# Create a legend above all subplots
legend_handles = []
legend_labels = []

Qmin=2e42*ergpersec
Qmax=2e46*ergpersec
nQ=5

names=['univ-1e14']
linestyles=['-']
labels=['Universal']
Qs=[Qmin*10**i for i in range(nQ)] #[2e+35, 2e+36, 2e+37, 2e+38, 2e+39]
#rainbow colors
colors=['red','orange','green','blue','purple']

for n,ls,l in zip(names,linestyles,labels):
    for Q,c in zip(Qs,colors):
        outname='example-'+n+'-Q-'+f'{Q:.1e}'+'.pickle'
        env=Evolve_RG.load(outname)
        tv=env.tv

        axes[0].plot(tv/Myr,env.R/kpc,color=c,label=l+' $R$')
        rlobep=np.sqrt(env.vl/(4*np.pi*env.R))
        #axes[0].plot(tv/Myr,env.Rp/kpc,ls='--',color=c,label=l+' $R_\\perp$')
        #axes[0].plot(tv/Myr,rlobep/kpc,ls='--',color=c,label=l+' $R_{\\perp, lobe}$')
        axes[1].plot(tv/Myr,env.rlobe,color=c)
        axes[2].plot(tv/Myr,env.m1,color=c)
        axes[2].plot(tv/Myr,env.mp1,color=c,ls=':', lw=1)
        axial=2*rlobep/env.R
        axes[3].plot(tv/Myr,axial,color=c,label=l)

        # Collect handles and labels for the legend (only once per Q)
        if n == names[0]:  # Only add legend entries for the first model to avoid duplicates
            legend_handles.append(plt.Line2D([0], [0], color=c, lw=2))
            legend_labels.append('$Q = ' + f'{Q/10**int(np.log10(Q)):.1f}' +'\\times 10^{'+str(int(np.log10(Q)))+'}$ W')

axes[0].plot(tv/Myr,40*(tv/Myr)**0.6,ls=':',color='green',label='$R \propto t^{3/5}$')
#axis1.set_ylim(R/kpc/5,5*R/kpc)
#axis2.set_ylim(enow/5,enow*20)
axlabs=['Source size (kpc)','$V_L/V$','Mach number of expansion, ${\cal M}$','$r_{axial}$']
for ax,l in zip(axes,axlabs):
    ax.set_xlim((tv[0]/Myr,tv[-1]/Myr))
    ax.set_xlabel('$t$ (Myr)')
    ax.set_ylabel(l)
    #ax.grid(linewidth=0.1)


axes[0].legend(loc=4, handles=[Line2D([0], [0], label='$R$ for universal models', color='k', ls='-'), Line2D([0], [0], label='$R \propto t^{3/5}$', color='green', ls=':')], fontsize='small')
axes[2].legend(loc=1, handles=[Line2D([0], [0], label='Longitudinal advance', color='k', ls='-'), Line2D([0], [0], label='Perpendicular advance', color='k', ls=':', lw=1)], fontsize='small')
#for i in [0,3]:
#    axes[i].legend(loc=4,fontsize='small')
#axes[2].plot([tv[0]/Myr,tv[-1]/Myr],[1,1],ls='--')

# Create a legend above all subplots for Q values and colors
fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=len(Qs), fontsize='small')

plt.tight_layout()

# Adjust the layout to make space for the legend
plt.subplots_adjust(top=0.95)  # Increase the top margin to make space for the legend

plt.savefig('figures/fig_2_example_env_Q.pdf')

#Repeat the plot, but varying the M500 value 

axes=[]
naxes=4
fig = plt.figure(figsize=(12,9))
for i in range(naxes):
    axes.append(plt.subplot(naxes//2,naxes//2,i+1))
for ax in axes:
    ax.set_xscale('log')

axes[0].set_yscale('log')
axes[2].set_yscale('log')

# Create a legend above all subplots
legend_handles = []
legend_labels = []

Q=2e46*ergpersec

names=['univ-1e13', 'univ-1e14', 'univ-1e15']
linestyles=['-']
labels=['Universal']
colors=['blue','violet', 'red']
M500 = 1e13

for n,ls,l,c in zip(names,linestyles,labels,colors):
    for Q,c in zip(Qs,colors):
        outname='example-'+n+'-Q-'+f'{Q:.1e}'+'.pickle'
        env=Evolve_RG.load(outname)
        tv=env.tv

        axes[0].plot(tv/Myr,env.R/kpc,color=c,label=l+' $R$')
        rlobep=np.sqrt(env.vl/(4*np.pi*env.R))
        #axes[0].plot(tv/Myr,env.Rp/kpc,ls='--',color=c,label=l+' $R_\\perp$')
        #axes[0].plot(tv/Myr,rlobep/kpc,ls='--',color=c,label=l+' $R_{\\perp, lobe}$')
        axes[1].plot(tv/Myr,env.rlobe,color=c)
        axes[2].plot(tv/Myr,env.m1,color=c)
        axes[2].plot(tv/Myr,env.mp1,color=c,ls=':', lw=1)
        axial=2*rlobep/env.R
        axes[3].plot(tv/Myr,axial,color=c,label=l)

        # Collect handles and labels for the legend (only once per Q)
        if n == names[0]:  # Only add legend entries for the first model to avoid duplicates
            legend_handles.append(plt.Line2D([0], [0], color=c, lw=2))
            legend_labels.append('$M_{500} = ' + f'{M500/10**int(np.log10(M500)):.1f}' +'\\times 10^{'+str(int(np.log10(M500)))+'} \, M_{\\odot}$')

axes[0].plot(tv/Myr,40*(tv/Myr)**0.6,ls=':',color='green',label='$R \propto t^{3/5}$')
#axis1.set_ylim(R/kpc/5,5*R/kpc)
#axis2.set_ylim(enow/5,enow*20)
axlabs=['Source size (kpc)','$V_L/V$','Mach number of expansion, ${\cal M}$','$r_{axial}$']
for ax,l in zip(axes,axlabs):
    ax.set_xlim((tv[0]/Myr,tv[-1]/Myr))
    ax.set_xlabel('$t$ (Myr)')
    ax.set_ylabel(l)
    #ax.grid(linewidth=0.1)


axes[0].legend(loc=4, handles=[Line2D([0], [0], label='$R$ for universal models', color='k', ls='-'), Line2D([0], [0], label='$R \propto t^{3/5}$', color='green', ls=':')], fontsize='small')
axes[2].legend(loc=1, handles=[Line2D([0], [0], label='Longitudinal advance', color='k', ls='-'), Line2D([0], [0], label='Perpendicular advance', color='k', ls=':', lw=1)], fontsize='small')
#for i in [0,3]:
#    axes[i].legend(loc=4,fontsize='small')
#axes[2].plot([tv[0]/Myr,tv[-1]/Myr],[1,1],ls='--')

# Create a legend above all subplots for Q values and colors
fig.legend(legend_handles, legend_labels, loc='upper center', bbox_to_anchor=(0.5, 1.0), ncol=len(Qs), fontsize='small')

plt.tight_layout()

# Adjust the layout to make space for the legend
plt.subplots_adjust(top=0.95)  # Increase the top margin to make space for the legend

plt.savefig('figures/fig_2_example_env_M500.pdf')