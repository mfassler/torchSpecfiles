#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-image
Version:	1.1.alpha0
Release:	1%{?dist}
Summary:	image manipulations for torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/image

BuildRequires:	git, luajit-devel
BuildRequires:	libpng-devel, libjpeg-devel
Requires:	luajit, luajit-torch-dok
Requires:	libpng, libjpeg

%description
This package provides routines to load/save and manipulate images
using Torch's Tensor data structure.


%prep
%setup -D -c -T -n torch
if [ ! -d image ]; then
    git clone https://github.com/torch/image.git
fi


%build
cd image
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_INSTALL_PREFIX=/usr \
 -DTorch_INSTALL_LUA_PATH_SUBDIR=/usr/lib64/lua/5.1
make


%install
cd image/build
make install DESTDIR=%{buildroot}
mkdir -p %{buildroot}%{lua_dir}/
mkdir -p %{buildroot}%{_libdir}/lua/5.1
mv %{buildroot}/usr/lib/lib* %{buildroot}%{_libdir}/lua/5.1/
mv %{buildroot}/usr/lua/image %{buildroot}%{lua_dir}
rmdir %{buildroot}/usr/lib
rmdir %{buildroot}/usr/lua


%files
%{_libdir}/lua/5.1/lib*.so
%{lua_dir}/image


%changelog

