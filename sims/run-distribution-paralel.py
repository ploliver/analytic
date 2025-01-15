from solver import Evolve_RG
from astropy.table import Table
import sys
from synch_constants import *
import os
from multiprocessing import Pool

def process_source(n):
    """
    Process a single source from the table
    """
    t = Table.read('source-table.txt', format='ascii')
    lookback = 1200
    
    r = t[n]
    print(f'Processing source {n}: {r}')
    
    env = Evolve_RG('universal', M500=r['M500'], xi=0.40, q=2.1)
    tlimit = lookback - r['Tstart']
    tv = np.logspace(-6, np.log10(tlimit), 100) * Myr
    outfile = f'run-{n}.pickle'
    
    if not os.path.isfile(outfile):
        env.solve(r['Q'], tv, tstop=r['lifetime']*Myr)
        env.findb()
        env.findsynch(150e6)
        env.findcorrection(
            (150e6, 150e6*(1+r['z']), 1400e6*(1+r['z'])),
            do_adiabatic=True,
            z=r['z'],
            timerange=(99,)
        )
        env.save(outfile)
    
    return outfile

if __name__ == '__main__':
    # Read the table once to get the number of sources
    t = Table.read('source-table.txt', format='ascii')
    num_sources = len(t)
    
    # Create list of source indices to process
    if len(sys.argv) > 1:
        # If specific indices are provided via command line
        source_indices = [int(idx) for idx in sys.argv[1:]]
    else:
        # Process all sources
        source_indices = list(range(num_sources))
    
    # Number of processes to use
    num_processes = os.cpu_count()  # Uses all available CPU cores
    
    print(f"Starting parallel processing with {num_processes} processes")
    print(f"Processing {len(source_indices)} sources")
    
    # Create a pool of workers and map the processing function to all sources
    with Pool(processes=num_processes) as pool:
        results = pool.map(process_source, source_indices)
    
    print("All calculations completed")
    print("Output files:", results)