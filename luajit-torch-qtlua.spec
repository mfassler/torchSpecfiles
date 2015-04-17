#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-qtlua
Version:	0.0.1
Release:	1%{?dist}
Summary:	Lua interface to QT library

Group:		Development/Languages
License:	BSD?...
URL:		https://github.com/torch/qtlua

BuildRequires:	git, cmake, luajit-devel, qt-devel
Requires:	luajit, qt, luajit-torch-qttorch

%description
Summary:	Lua interface to QT library


%prep
%setup -D -c -T -n torch
if [ ! -d qtlua ]; then
    git clone https://github.com/torch/qtlua.git
fi

cd qtlua
git checkout master 
git pull


%build
cd qtlua
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_INSTALL_PREFIX=/usr \
 -DLUA_BINDIR=%{_bindir} \
 -DLUA_LIBDIR=%{_libdir}/lua/5.1 \
 -DLUA_INCDIR=%{_includedir} \
 -DCONFDIR=%{_datadir} \
 -DLUADIR=%{lua_dir} \
 -DLIBDIR=%{_libdir}/lua/5.1 \
 -DLUA_INCLUDE_DIR=%{_includedir}/luajit-2.0

make


%install
cd qtlua/build
make install DESTDIR=%{buildroot}


%files
%{_bindir}/*
%{lua_dir}/qt*
%{_includedir}/qtlua
%{_libdir}/lua/5.1/libq*
%{_datadir}/cmake/Qt*


%changelog

