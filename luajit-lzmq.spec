#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-lzmq
Version:	0.4.2
Release:	1%{?dist}
Summary:	Lua bindings to ZeroMQ

Group:		Development/Languages
License:	MIT/X11
URL:		https://github.com/zeromq/lzmq

BuildRequires:	git, cmake, luajit-devel, zeromq3-devel
Requires:	luajit, zeromq3

%description
Lua bindings to ZeroMQ


%prep
%setup -D -c -T -n zeromq
if [ ! -d lzmq ]; then
    git clone https://github.com/zeromq/lzmq.git
fi

cd lzmq
git checkout master 
git pull
git checkout v0.4.2



%build
cd lzmq
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_INSTALL_PREFIX=/usr \
 -DLUA_INCLUDE_DIR=%{_includedir}/luajit-2.0 \
 -DLIBDIR=%{_libdir}/lua/5.1 \
 -DINSTALL_LIB=%{_libdir}/lua/5.1 \
 -DINSTALL_CMOD=%{_libdir}/lua/5.1

# -DLUA_LIBRARIES=%{_libdir}/lua/5.1

#CMAKE_INSTALL_NAME_DIR=@executable_path/../lib
#CMAKE_INSTALL_RPATH=$ORIGIN/../lib
#INSTALL_BIN=bin
#INSTALL_CMOD=lib/lua
#INSTALL_DATA=share/lzmq
#INSTALL_LIB=lib
#INSTALL_SHARE=share

make



%install
cd lzmq/build
make install DESTDIR=%{buildroot}
## FIXME: stupid hack
rm -rf %{buildroot}/usr/share/lzmq
mkdir -p %{buildroot}%{lua_dir}
mv %{buildroot}%{_libdir}/lua/5.1/lua/lzmq %{buildroot}%{lua_dir}
rmdir %{buildroot}%{_libdir}/lua/5.1/lua


%files
%{lua_dir}
%{_libdir}/lua/5.1/lzmq*


%changelog

