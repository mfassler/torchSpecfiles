#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-cutorch
Version:	0.0.1
Release:	1%{?dist}
Summary:	CUDA backend for Torch7

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/cutorch

BuildRequires:	nvcc, cuda, cmake, luajit-torch-torch7
Requires:	cuda, luajit, luajit-torch-torch7

%description
CUDA backend for Torch7

%prep
%setup -D -c -T -n torch
if [ ! -d cutorch ]; then
	git clone https://github.com/torch/cutorch.git
fi
cd cutorch
#git checkout master
#git pull



%build
cd cutorch
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr

# -DLIBDIR=%{_libdir}/lua/5.1 \
# -DLUA=luajit \
# -DLUADIR=%{lua_dir} \
# -DLUA_BINDIR=%{_bindir}
# -DLUA_INCDIR=%{_includedir}/luajit-2.0 \
# -DLUA_LIBDIR=%{_libdir} \

### FFS, the make process runs twice...
#make


%install
cd cutorch/build
make install DESTDIR=%{buildroot}

cd %{buildroot}
mkdir -p %{buildroot}%{_libdir}/lua/5.1
mkdir -p %{buildroot}%{lua_dir}

mv usr/lib/libcutorch.so usr/lib64/lua/5.1/
mv usr/lua/cutorch %{buildroot}%{lua_dir}
rmdir usr/lib
rmdir usr/lua


%files
%{lua_dir}/cutorch
%{_includedir}/luajit-2.0/THC
%{_libdir}/lua/5.1/libcu*
%{_libdir}/libTHC.so



%changelog

