#!/bin/sh
module load datascience/tensorflow-2.3
module load darshan
export DARSHAN_LOG_DIR=/lus/theta-fs0/logs/darshan/theta/$(date +%Y/%-m/%-d)
export DARSHAN_DISABLE_SHARED_REDUCTION=1
export DXT_ENABLE_IO_TRACE=4
export DARSHAN_PRELOAD=/soft/perftools/darshan/darshan-3.3.0/lib/libdarshan.so
export LD_PRELOAD="$DARSHAN_PRELOAD $LD_PRELOAD"
export DARSHAN_DIR=$(dirname $(dirname $DARSHAN_PRELOAD))
[[ -e tmp ]] || mkdir tmp
git clone git@github.com:zhenghh04/vanidl.git tmp/vanidl
cd tmp/vanidl
python setup.py build
python setup.py install --user
cd -
