# SKA SDC2 Team “SoFiA”

## Overview

This reporsitory contains information, scripts and setup files in relation to the participation of team “SoFiA” in the SKA Science Data Challenge 2 which closed on 31 July 2021. Our team used the Source Finding Application (SoFiA) development version 2.3.1, dated 22 July 2021, which is available for download from [GitHub](https://github.com/SoFiA-Admin/SoFiA-2/tree/11ff5fb01a8e3061a79d47b1ec3d353c429adf33).

## Running SoFiA

All of the configuration files required to run SoFiA on the full data cube are located in the `sofia` folder. It is assumed that 80 instances of SoFiA are run in parallel on an HPC cluster with adequate resources and the Slurm workload manager available. Each instance of SoFiA requires 27 GB of RAM and ideally 8 parallel threads.

In order to launch the SoFiA run, all files contained in the folder `sofia` must be copied into the directory where the SDC2 data cube (`sky_full_v2.fits`) is located. It is further assumed that SoFiA is installed and can be launched with the command `sofia`. SoFiA can then be executed by simply running the

```
run_sofia.sh
```

shell script. This will use Slurm to create 80 batch jobs, each of which is running on a smaller region of the data cube of about 11.8 GB in size. Depending on the specification of the HVC cluster and available resources, this could take several hours to complete. Once all instances are finished, the output catalogues and image products from each run should have been written into the same directory. The `output.directory` setting in the individual SoFiA parameter files can be used to define a different output directory if desired.

## Team Members

* Kelley Hess
* Thijs van der Hulst
* Russell Jurek
* Slava Kitaeff
* Dave Pallot
* Paolo Serra
* Austin Shen
* Tobias Westmeier (chair)
