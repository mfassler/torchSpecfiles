#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-torch7
Version:	0.0.1
Release:	1%{?dist}
Summary:	Math library for Lua

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/torch7

BuildRequires:	git, cmake, luajit-devel, luajit-torch-cwrap, openblas-devel
Requires:	luajit, luajit-torch-paths, openblas

%description
Data structures for multi-dimensional tensors.  (and mathematical operations
over these)   Additionally, it provides many utilities for 
accessing files, serializing objects of arbitrary types and other useful
utilities.

%prep
%setup -D -c -T -n torch
if [ ! -d torch7 ]; then
    git clone https://github.com/torch/torch7.git
fi
cd torch7

#git checkout master
#git pull
git checkout random.lua
git checkout TensorMath.lua
# prepend a shebang to these two files and make them executable
sed -i -e '1i #!/usr/bin/env luajit' random.lua
sed -i -e '1i #!/usr/bin/env luajit' TensorMath.lua
chmod +xxx random.lua
chmod +xxx TensorMath.lua

## FIXME: stupid hack
git checkout cmake/TorchPaths.cmake
sed -i -e '18i SET(Torch_INSTALL_PREFIX "/usr")' cmake/TorchPaths.cmake
sed -i -e '18i SET(CMAKE_INSTALL_PREFIX "/usr")' cmake/TorchPaths.cmake


%build
cd torch7
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_INSTALL_PREFIX=/usr \
 -DLUA=luajit \
 -DLUA_INCDIR=%{_includedir}/luajit-2.0 \
 -DLUADIR=%{lua_dir} \
 -DLUA_LIBDIR=%{_libdir} \
 -DLIBDIR=%{_libdir}/lua/5.1 \
 -DLUA_BINDIR=%{_bindir}

make


%install
cd torch7/build
make install DESTDIR=%{buildroot}


%files
%{_includedir}/luajit-2.0/TH
%{_includedir}/luajit-2.0/luaT.h
%{lua_dir}/torch
%{_libdir}/lua/5.1/*
%{_libdir}/libTH.so
%{_libdir}/libluaT.so
/usr/share/cmake/torch


%changelog

