#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-sys
Version:	0.0.1
Release:	1%{?dist}
Summary:	Lua system package for torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/sys

BuildRequires:	git, luajit-devel
Requires:	luajit

%description


%prep
%setup -D -c -T -n torch
if [ ! -d sys ]; then
    git clone https://github.com/torch/sys.git
fi


%build
cd sys
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_INSTALL_PREFIX=%{buildroot}

make


%install
cd sys/build
make install DESTDIR=%{buildroot}

## FIXME:  stupid hack
mkdir -p %{buildroot}%{_libdir}/lua/5.1
mkdir -p %{buildroot}%{lua_dir}/sys
cd %{buildroot}
mv `find | grep libsys\\.so` %{buildroot}%{_libdir}/lua/5.1/
mv `find |grep init\\.lua` %{buildroot}%{lua_dir}/sys/
#rm -rf home


%files
%{_libdir}/lua/5.1/libsys.so
%{lua_dir}/sys/init.lua


%changelog

