#!/bin/bash

git clone git@git.ustack.com:jimjiang/oslo-incubator.git ../oslo-incubator

position="../"$1

git init $position
sudo pip install tox

cp openstack-common.conf $position 
cp *.txt $position 
cp tox.ini $position 
cp setup.* $position
cp .testr.conf $position
find $position -name "*" -exec sed -i "s/example/$1/g"  {} \;

pushd ../oslo-incubator/
python update.py $position 
popd

examples=$position"/"$1
cp -r example/* $examples 
find $position -name "*.py" -exec sed -i "s/example/$1/g"  {} \;

pushd $position
git add .
git commit -am "Init Project"
tox -evenv -- echo 'done'
source .tox/venv/bin/activate
testr init
flake8
testr run
deactivate
popd $position
