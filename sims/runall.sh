# script to run all the simulations, as written in README.txt
# This script assumes a working installation of Python 3.11

# First, we remove any old pickle files
rm *.pickle

# Then we add analytic to PYTHONPATH, depends on your OS
export PYTHONPATH=/path/to/analytic:$PYTHONPATH

# Fig 1 Pressure profiles
echo Running: Fig 1, Pressure profiles
python3.11 prprof.py

# Fig 2 Example environments 
echo Running: Fig 2, Example environments
python3.11 example_environments.py
python3.11 example_env_plots.py

# Fig 3 HK13 comparison
# echo Running: Fig 3, HK13 comparison
# python3.11 hk13beta.py
# python3.11 plot_pluto_hk13.py

# Fig 4 Synchrotron vs time
echo Running: Fig 4, Synchrotron vs time
python3.11 example_envs_highz.py
python3.11 example_envs_no_adiabatic.py
python3.11 example-spectra-plots.py
python3.11 example-spectra-vary-plots.py

# Fig 7 Losses
echo Running: Fig 7, Losses
python3.11 plot_losses.py

# Done
echo Done