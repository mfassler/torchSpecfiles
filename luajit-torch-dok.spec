#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-dok
Version:	0.0.1
Release:	1%{?dist}
Summary:	Support for the old torch7 dok system

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/dok

BuildRequires:	git
Requires:	luajit, luajit-torch-sundown

%description
Support for the old torch7 dok system


%prep
%setup -D -c -T -n torch
if [ ! -d dok ]; then
    git clone https://github.com/torch/dok.git
fi


%build
cd dok


%install
cd dok
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lua_dir}/dok
#cp -a README.md *.lua %{buildroot}%{lua_dir}/dok
cp -a  *.lua %{buildroot}%{lua_dir}/dok


%files
#%{lua_dir}/dok/README.md
%{lua_dir}/dok/init.lua
%{lua_dir}/dok/inline.lua


%changelog

