#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-nngraph
Version:	0.0.1
Release:	1%{?dist}
Summary:	Neural Network package for Torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/nngraph

BuildRequires:	git, luajit-devel
Requires:	luajit, luajit-torch-torch7, luajit-torch-graph

%description
Neural Network package for Torch


%prep
%setup -D -c -T -n torch
if [ ! -d nngraph ]; then
    git clone https://github.com/torch/nngraph.git
fi


%build
cd nngraph
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr

make


%install
cd nngraph/build
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{lua_dir}
mv %{buildroot}/usr/lua/nngraph %{buildroot}%{lua_dir}/
rmdir %{buildroot}/usr/lua


%files
%{lua_dir}/nngraph


%changelog

