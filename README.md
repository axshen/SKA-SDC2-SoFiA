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

## Post-processing

Once the SoFiA run is complete, several post-processing steps will be required to turn the 80 output catalogues from the individual instances into a single catalogue listing the specific source parameters required by the SDC2 scoring service. Two alternative options are available:

1. SoFiA-X
2. Python + Topcat

### Alternative 1: SoFiA-X

SoFiA-X is a wrapper around SoFiA 2 that can be used to upload the output files from parallel runs of SoFiA 2 into an online database. Duplicate detections in regions of overlap between individual instances will be automatically resolved, with the additional option of manual resolution in cases where the automatic resolution algorithm encounters a conflict.

SoFiA-X is publicly available for download from [GitHub](https://github.com/AusSRC/SoFiAX). Additional information on how to install and use SoFiA-X is available in the README file in the GitHub repository. As setting up SoFiA-X is non-trivial, we will refrain from providing further information here and instead refer the reader to the SoFiA-X repository for further instructions.

### Alternative 2: Python + Topcat

Another option of merging the output catalogues from the individual SoFiA instances is to use a combination of Python scripts and functionality provided by Topcat. A Python script for concatenating the individual output catalogue files is available in `scripts/concatenate_catalogues.py`. This script can simply be copied into the same directory where the indivual output catalogues are located and then be launched to concatenate all 80 catalogues into a single output catalogue named `merged_catalogue.xml`.

Once completed, the merged catalogue can be loaded into Topcat to remove any potential duplicate detections from regions of overlap between individual instances.

## Team Members

* Kelley Hess
* Thijs van der Hulst
* Russell Jurek
* Slava Kitaeff
* Dave Pallot
* Paolo Serra
* Austin Shen
* Tobias Westmeier (chair)
