#!/bin/sh

pwd
ls

export SCRATCH=`pwd`
cmsRun -j FrameworkJobReport.xml -p PSet.py 

echo "-"$SCRATCH"-"
if [ "$SCRATCH" != "" ]
then
  ls $SCRATCH/SiStripCommissioningSource*.root
  file=`ls $SCRATCH/SiStripCommissioningSource*.root | tail -1`
else
  ls /tmp/SiStripCommissioningSource*.root
  file=`ls /tmp/SiStripCommissioningSource*.root | tail -1`
fi
echo "mv $file SiStripCommissioningSource.root"
mv $file SiStripCommissioningSource.root 

