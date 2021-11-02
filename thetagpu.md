# DLIO on ThetaGPU


## Environment setup
```bash
# Loading TensorFlow / PyTorch module
module load conda/2021-09-22
conda activate
# Loading Darshan
module load darshan
export DARSHAN_DISABLE_SHARED_REDUCTION=1
export DXT_ENABLE_IO_TRACE=4
export LD_PRELOAD="$DARSHAN_PRELOAD $LD_PRELOAD"
```
## Installing VaniDL
