#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-graph
Version:	0.0.1
Release:	1%{?dist}
Summary:	Graph package for Torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/graph

BuildRequires:	git, luajit-devel
Requires:	luajit, luajit-torch-torch7

%description
Graph package for Torch


%prep
%setup -D -c -T -n torch
if [ ! -d graph ]; then
    git clone https://github.com/torch/graph.git
fi


%build
cd graph
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr
make


%install
cd graph/build
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{lua_dir}
mv %{buildroot}/usr/lua/graph %{buildroot}%{lua_dir}/
rmdir %{buildroot}/usr/lua


%files
%{lua_dir}/graph


%changelog

