#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-deepmind-alewrap
Version:	0.0.1
Release:	1%{?dist}
Summary:	A lua wrapper for the Arcade Learning Environment/xitari

Group:		Development/Languages
License:	BSD
URL:		https://github.com/deepmind/alewrap

BuildRequires:	git, luajit-devel, xitari
Requires:	luajit, luajit-torch-torch7, xitari

%description
A lua wrapper for the Arcade Learning Environment/xitari


%prep
%setup -D -c -T -n deepmind
if [ ! -d alewrap ]; then
    git clone https://github.com/deepmind/alewrap.git
fi


%build
cd alewrap
rm -rf build
mkdir build
cd build
cmake .. \
 -DCMAKE_BUILD_TYPE=Release \
 -DCMAKE_PREFIX_PATH=/usr \
 -DCMAKE_INSTALL_PREFIX=/usr
make


%install
cd alewrap/build
make install DESTDIR=%{buildroot}

mkdir -p %{buildroot}%{lua_dir}
mkdir -p %{buildroot}%{_libdir}/lua/5.1

mv %{buildroot}/usr/lua/alewrap %{buildroot}%{lua_dir}/
mv %{buildroot}/usr/lib/lib* %{buildroot}%{_libdir}/lua/5.1/

rmdir %{buildroot}/usr/lib
rmdir %{buildroot}/usr/lua


%files
%{lua_dir}/alewrap
%{_libdir}/lua/5.1/lib*

%changelog

