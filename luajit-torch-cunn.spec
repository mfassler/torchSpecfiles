#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-cunn
Version:	0.0.1
Release:	1%{?dist}
Summary:	CUDA backend for Torch7

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/cunn

BuildRequires:	nvcc, cuda, cmake, luajit-torch-torch7
Requires:	cuda, luajit, luajit-torch-torch7

%description
CUDA backend for Torch7

%prep
%setup -D -c -T -n torch
if [ ! -d cunn ]; then
	git clone https://github.com/torch/cunn.git
fi
cd cunn
#git checkout master
#git pull



%build
cd cunn
rm -rf build
mkdir build
cd build

cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr

### FFS, the make process runs twice...
#make


%install
cd cunn/build
make install DESTDIR=%{buildroot}

cd %{buildroot}
mkdir -p %{buildroot}%{_libdir}/lua/5.1
mkdir -p %{buildroot}%{lua_dir}

mv usr/lib/libcunn.so usr/lib64/lua/5.1/
mv usr/lua/cunn %{buildroot}%{lua_dir}
rmdir usr/lib
rmdir usr/lua


%files
%{lua_dir}/cunn
%{_libdir}/lua/5.1/libcu*



%changelog

