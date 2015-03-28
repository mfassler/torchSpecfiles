#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-nn
Version:	0.0.1
Release:	1%{?dist}
Summary:	Neural Network package for Torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/nn

BuildRequires:	git, luajit-devel, luajit-torch-torch7
Requires:	luajit, luajit-torch-torch7

%description


%prep
%setup -D -c -T -n torch
if [ ! -d nn ]; then
    git clone https://github.com/torch/nn.git
fi

%build
cd nn
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr
make



%install
cd nn/build
make install DESTDIR=%{buildroot}

# I guess luarocks would normally handle this?...
mkdir -p %{buildroot}%{_libdir}/lua/5.1
mkdir -p %{buildroot}%{lua_dir}
mv %{buildroot}/usr/lib/libnn.so %{buildroot}%{_libdir}/lua/5.1/
rmdir %{buildroot}/usr/lib
mv %{buildroot}/usr/lua/nn %{buildroot}%{lua_dir}/
rmdir %{buildroot}/usr/lua


%files
%{_libdir}/lua/5.1/libnn.so
%{lua_dir}/nn

%changelog

