#!/bin/sh

module load conda/2021-11-30
conda activate

# Loading Darshan
module load darshan
export DARSHAN_LOG_DIR=/lus/grand/logs/darshan/thetagpu/$(date +%Y/%-m/%-d)
export DARSHAN_DISABLE_SHARED_REDUCTION=1
export DXT_ENABLE_IO_TRACE=4
export LD_PRELOAD="$DARSHAN_PRELOAD $LD_PRELOAD"
export DARSHAN_DIR=$(dirname $(dirname $DARSHAN_PRELOAD))
[[ -e tmp ]] || mkdir tmp
git clone git@github.com:zhenghh04/vanidl.git tmp/vanidl
cd tmp/vanidl
python setup.py build
python setup.py install --user
cd -
