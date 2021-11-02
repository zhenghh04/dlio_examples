# Deep learning I/O profiling on ThetaGPU

## Login to ThetaGPU
```bash
ssh -CY user@theta.alcf.anl.gov
ssh -CY thetagpusn1
qsub -n 4 -q full-node -A datascience -t 1:00:00 -I --attrs=pubnet
```
## Environment setup
```
# Loading TensorFlow / PyTorch module
module load conda/2021-09-22
conda activate
# Loading Darshan
module load darshan
export DARSHAN_DISABLE_SHARED_REDUCTION=1
export DXT_ENABLE_IO_TRACE=1
export LD_PRELOAD="$DARSHAN_PRELOAD $LD_PRELOAD"
export DARSHAN_DIR=$(dirname $(dirname $DARSHAN_PRELOAD))
```
## Installing VaniDL
```bash
git clone git@github.com:zhenghh04/vanidl.git vanidl_src
cd vanidl_src
python setup.py build
python setup.py install --user
```
## Running examples
```
./aprun.wrapper -n 32 -N 8 python tensorflow2_keras_mnist.py --device gpu
```
This will generate the following example darshan output in the following directory
/lus/grand/logs/darshan/thetagpu/YYYY/MM/DD/*.darshan

## Generating 

import vanidl
from vanidl.analyzer import *
profile = VaniDL()
#Load darshan file
status = profile.Load("./res.darshan")
#Get Job Summary
summary = profile.GetSummary()

