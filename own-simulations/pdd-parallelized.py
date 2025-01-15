import numpy as np
import pickle
import os
from multiprocessing import Pool
from itertools import product

from synch_constants import *
from solver import Evolve_RG

def process_qm_pair(args):
    """
    Process a single Q,m pair
    """
    Q, m = args
    print(f'Doing the run for Q={Q}, M={m}')
    
    tmin = 0
    tmax = 500
    tv = np.logspace(-6, np.log10(tmax), 100) * Myr
    
    env = Evolve_RG('universal', M500=m, xi=0.40, q=2.1)
    outfile = f'save_{np.log10(Q):.1f}_{np.log10(m):.1f}.pickle'
    
    if not os.path.isfile(outfile):
        print('solving for', Q, m)
        env.solve(Q, tv)
        env.findb()
        env.findsynch(150e6)
        env.findcorrection((150e6, 1400e6), do_adiabatic=True)
        env.save(outfile)
    
    return outfile

if __name__ == '__main__':
    # Define the parameter space
    Qs = np.logspace(36, 40, 13)  # 13 values of Q
    masses = np.logspace(13, 15, 10)  # 10 values of M
    
    # Create all combinations of Q and m
    parameter_combinations = list(product(Qs, masses))
    
    # Number of processes to use (adjust based on your CPU cores)
    num_processes = os.cpu_count()  # Uses all available CPU cores
    
    print(f"Starting parallel processing with {num_processes} processes")
    print(f"Total combinations to process: {len(parameter_combinations)}")
    
    # Create a pool of workers and map the processing function to all combinations
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_qm_pair, parameter_combinations)
    
    print("All calculations completed")
    print("Output files:", results)