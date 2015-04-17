#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-itorch
Version:	0.0.1
Release:	1%{?dist}
Summary:	iPython kernel for Lua / Torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/facebook/iTorch

BuildRequires:	git, cmake, luajit-devel
Requires: luajit, luajit-torch-torch7
Requires: luajit-uuid, luajit-cjson, luajit-lzmq, luajit-lbase64
Requires: python-jinja2
Requires: python-tornado >= 4.0
Requires: python-jsonschema

%description
iPython kernel for Lua / Torch


%prep
%setup -D -c -T -n facebook
if [ ! -d iTorch ]; then
    git clone https://github.com/facebook/iTorch.git
fi
cd iTorch

#git checkout master
#git pull



%build
cd iTorch
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr

make


%install
cd iTorch/build
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_datadir}/itorch/files
mkdir -p %{buildroot}%{lua_dir}

cp -a ../itorch ../itorch_launcher %{buildroot}%{_bindir}
cp -a ../kernelspec  %{buildroot}%{_datadir}/itorch/files/

sed -i "s@LUA_BINDIR@/usr/bin@" %{buildroot}%{_datadir}/itorch/files/kernelspec/kernel.json

cp -a ../ipynblogo.png ../custom.js ../custom.css %{buildroot}%{_datadir}/itorch/files/

mv %{buildroot}/usr/lua/itorch %{buildroot}%{lua_dir}
rmdir %{buildroot}/usr/lua




%files
%{_bindir}/*
%{_datadir}/itorch
%{lua_dir}/itorch

%changelog




