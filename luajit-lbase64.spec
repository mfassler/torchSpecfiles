#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-lbase64
Version:	0.2
Release:	1%{?dist}
Summary:	A base64 library for Lua

Group:		Development/Languages
License:	Public Domain
URL:		http://webserver2.tecgraf.puc-rio.br/~lhf/ftp/lua/#lbase64
Source:		http://webserver2.tecgraf.puc-rio.br/~lhf/ftp/lua/5.1/lbase64.tar.gz

BuildRequires:	git
Requires:	luajit

%description
A base64 library for Lua


%prep
%setup -n base64


%build
make so LUAINC=/usr/include/luajit-2.0  G=-fPIC

%install
mkdir -p %{buildroot}%{_libdir}/lua/5.1
cp -a *.so %{buildroot}%{_libdir}/lua/5.1


%files
%{_libdir}/lua/5.1/*


%changelog

