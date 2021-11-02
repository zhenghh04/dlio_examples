# Deep learning I/O profiling on ThetaGPU

## Login to Theta
```bash
ssh -CY user@theta.alcf.anl.gov
qsub -n 4 -q debug-cache-quad -A datascience -t 1:00:00 -I 
```
## Environment setup ([setup_knl.sh](./setup_knl.sh))
```bash
# Loading TensorFlow / PyTorch module
module load datascience/tensorflow-2.3
# Loading Darshan
module load darshan
export DARSHAN_DISABLE_SHARED_REDUCTION=1
export DXT_ENABLE_IO_TRACE=4
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
./aprun.wrapper -n 32 -N 8 python tensorflow2_keras_mnist.py --device cpu
```
This will generate the following example darshan output in the following directory
/lus/theta-fs0/logs/darshan/theta/$(date +%Y/%-m/%-d)

## Generating profiling results (more details, [vanidl_profile.py](./vanidl_profile.py))
```
import vanidl
from vanidl.analyzer import *
profile = VaniDL()
#Load darshan file
status = profile.Load("./res.darshan")
#Get Job Summary
summary = profile.GetSummary()
# Print high level summary
profile.PrintSummary()
```
