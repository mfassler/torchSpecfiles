


These are the dependencies for DQN from Google Deepmind.  I have tested these
with Fedora 20 and Fedora 21.  


The paper is here:
[Human-level control through deep reinforcement learning] (http://www.readcube.com/articles/10.1038%2Fnature14236)




## Installation instructions

### As root:

```bash
yum install rpm-build git cmake gcc-c++ openblas openblas-devel fftw-devel libjpeg-turbo-devel libpng-devel luajit luajit-devel wget

```

### As a regular user:
```bash
cp Example.rpmmacros ~/.rpmmacros
rpmbuild -bb luajit-torch-sundown.spec
rpmbuild -bb luajit-torch-cwrap.spec
rpmbuild -bb luajit-torch-paths.spec

```

### As root:
```bash
cd /home/$yourUserName/rpmbuild/RPMS/
rpm -i luajit-torch-sundown-*
rpm -i luajit-torch-cwrap-*
rpm -i luajit-torch-paths-*
```

### As a regular user:
```bash
rpmbuild -bb luajit-torch-torch7.spec
```

### As root:
```bash
rpm -i luajit-torch-torch7-*
```

### As a regular user:
```bash
rpmbuild -bb luajit-torch-graph.spec
rpmbuild -bb luajit-torch-nn.spec
rpmbuild -bb luajit-torch-nngraph.spec
rpmbuild -bb luajit-torch-dok.spec
cd ~/rpmbuild/SOURCES/
wget http://cloud.github.com/downloads/keplerproject/luafilesystem/luafilesystem-1.6.2.tar.gz
wget https://github.com/stevedonovan/Penlight/archive/1.3.1/Penlight-1.3.1.tar.gz
cd -
rpmbuild -bb luajit-torch-luafilesystem.spec
rpmbuild -bb luajit-torch-penlight.spec
rpmbuild -bb luajit-torch-sys.spec
rpmbuild -bb luajit-torch-xlua.spec
rpmbuild -bb luajit-torch-image.spec
rpmbuild -bb luajit-torch-env.spec
rpmbuild -bb luajit-torch-trepl.spec
rpmbuild -bb xitari.spec
```

### As root:
```bash
rpm -i luajit-torch-graph-*
rpm -i luajit-torch-nn-*
rpm -i luajit-torch-nngraph-*
rpm -i luajit-torch-dok-*
rpm -i luajit-torch-luafilesystem-*
rpm -i luajit-torch-penlight-*
rpm -i luajit-torch-sys-*
rpm -i luajit-torch-xlua-*
rpm -i luajit-torch-image-*
rpm -i luajit-torch-env-*
rpm -i luajit-torch-trepl-*
rpm -i xitari-*
```

### As a regular user:
```bash
rpmbuild -bb luajit-deepmind-alewrap.spec
```

### As root:
```bash
rpm -i luajit-deepmind-alewrap-*
```


## Play with DQN

After you install the dependencies, here is the code that you can play with:
https://sites.google.com/a/deepmind.com/dqn/



## To use both "trepl" and "qt" together:
```bash
qlua -e "require('trepl')()"
```


