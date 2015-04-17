#!/bin/bash

ipybase=$(ipython locate)
# ... $ipybase is typically ~/.config/ipython


rm -rf $ipybase/profile_torch
#rm -rf $ipybase/profile_itorch
rm -rf $ipybase/kernels/itorch

ipython profile create torch

mkdir -p $ipybase/profile_torch/static/base/images
mkdir -p $ipybase/profile_torch/static/custom/
mkdir -p $ipybase/kernels/itorch


echo 'c.KernelManager.kernel_cmd = ["/usr/bin/itorch_launcher","{connection_file}"]' >>$ipybase/profile_torch/ipython_config.py

echo "c.Session.key = b''" >>$ipybase/profile_torch/ipython_config.py
echo "c.Session.keyfile = b''" >>$ipybase/profile_torch/ipython_config.py

## This can also be done globally, from the .rpm itself I beleive:
cp -a /usr/share/itorch/files/kernelspec/* $ipybase/kernels/itorch/

cp -a /usr/share/itorch/files/ipynblogo.png $ipybase/profile_torch/static/base/images/
cp -a /usr/share/itorch/files/custom.js $ipybase/profile_torch/static/custom/
cp -a /usr/share/itorch/files/custom.css $ipybase/profile_torch/static/custom/


#original:
#cp -r ~/.ipython/profile_torch ~/.ipython/profile_itorch

# i think this is what they want:
cp -a $ipybase/profile_torch $ipybase/profile_itorch



