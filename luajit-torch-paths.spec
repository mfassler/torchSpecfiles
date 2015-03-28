#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-paths
Version:	0.0.1
Release:	1%{?dist}
Summary:	path manipulations for torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/paths

BuildRequires:	git, cmake, luajit-devel
Requires:	luajit

%description
path manipulations for torch


%prep
%setup -D -c -T -n torch
if [ ! -d paths ]; then
    git clone https://github.com/torch/paths.git
fi


%build
cd paths
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_INSTALL_PREFIX=%{buildroot} \
 -DLUA_INCDIR=/usr/include/luajit-2.0 \
 -DLIBDIR=/usr/lib64/lua/5.1
make


%install
cd paths/build
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{lua_dir}/
mv %{buildroot}/paths %{buildroot}%{lua_dir}


%files
%{_libdir}/lua/5.1/libpaths.so
%{lua_dir}/paths/init.lua


%changelog

