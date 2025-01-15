# script to run all the simulations, as written in README.txt

# First, we remove any old pickle files
rm *.pickle

# Then we add analytic to PYTHONPATH, depends on your OS so I'll write my command
export PYTHONPATH=/Users/pau/Documents/uni/uv/fisica_avanzada/estelar/group_work/simulation/analytic:$PYTHONPATH

# Fig 1 Pressure profiles
echo Running: Fig 1, Pressure profiles
python3.11 prprof.py

# Fig 2 Example environments
echo Running: Fig 2, Example environments
python3.11 example_environments.py
python3.11 example_env_plots.py

# Fig 3 HK13 comparison
echo Running: Fig 3, HK13 comparison
python3.11 hk13beta.py
python3.11 plot_pluto_hk13.py

# Fig 4 Synchrotron vs time
echo Running: Fig 4, Synchrotron vs time
python3.11 example_envs_highz.py
python3.11 example_envs_no_adiabatic.py
python3.11 example-spectra-plots.py
python3.11 example-spectra-vary-plots.py

# Fig 5 remnant
echo Running: Fig 5, remnant
python3.11 example_remnant.py
python3.11 example-tstop-spectra-plots.py

# Fig 6 Inverse-Compton LC
echo Running: Fig 6, Inverse-Compton LC
python3.11 plot_remnant_ic.py

# Fig 7 PDD, parallelization is for the weak...
echo Running: Fig 7, PDD
cd pdd
python3.11 ../pdd-parallelized.py
cd ..
python3.11 pdd_plots.py 0
#python3.11 pdd_plots.py highz

# Fig 8 histograms
echo Running: Fig 8, histograms
cd dist 
python3.11 ../make_distribution.py
python3.11 ../run-distribution-paralel.py

#python3.11 update_distribution.py # get key quantities from runs
#python $AP/flux_distribution.py # add fluxes
#python $AP/obs_table.py

#then

#python $AP/plot_hists.py

# Fig 9 remnant fraction
echo Running: Fig 9, remnant fraction
python3.11 remnant_fraction.py
pdfcrop remnant-fraction.pdf

# Fig 9 remnant fraction
python $AP/remnant_fraction.py
pdfcrop remnant-fraction.pdf

# Fig 10 radio power/jet power

python $AP/plot_ql150.py
python $AP/plot_ql150_lowz.py
pdfcrop plot_ql150.pdf
pdfcrop plot_ql150_lowz.pdf

# Fig 11 radio power/environment

python $AP/plot_l150m500_lowz.py
pdfcrop plot_150m500.pdf

# Fig age-size

python3.11 plot_agesize.py
