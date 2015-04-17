#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-qttorch
Version:	0.0.1
Release:	1%{?dist}
Summary:	QT-me, baby (torch)

Group:		Development/Languages
License:	BSD (linked against qt?...)
URL:		https://github.com/torch/qttorch

BuildRequires:	git, cmake, luajit-devel, qt-devel
Requires:	luajit, qt

%description
torch, qt-style


%prep
%setup -D -c -T -n torch
if [ ! -d qttorch ]; then
    git clone https://github.com/torch/qttorch.git
fi

cd qttorch
git checkout master 
git pull


%build
cd qttorch
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_INSTALL_PREFIX=/usr \
 -DCMAKE_CXX_FLAGS=" -I /usr/include/qtlua"

make


%install
cd qttorch/build
make install DESTDIR=%{buildroot}

# FIXME: stupid hack...
mkdir -p %{buildroot}%{_libdir}/lua/5.1
mkdir -p %{buildroot}%{lua_dir}
mv %{buildroot}/usr/lib/libq* %{buildroot}%{_libdir}/lua/5.1/
rmdir %{buildroot}/usr/lib
mv %{buildroot}/usr/lua/qttorch %{buildroot}%{lua_dir}/
rmdir %{buildroot}/usr/lua

%files
%{_libdir}/lua/5.1/*
%{lua_dir}/*


%changelog

