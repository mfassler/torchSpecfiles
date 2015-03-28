#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-cwrap
Version:	0.0.1
Release:	1%{?dist}
Summary:	helps you generate Lua/C wrappers

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/cwrap

BuildRequires:	git
Requires:	luajit

%description
The __wrap__ package helps you to automate the generation of Lua/C wrappers
around existing C functions, such that these functions would be callable
from Lua. This package is used by the __torch__ package, but does not depend on
anything, and could be used by anyone using Lua.


%prep
%setup -D -c -T -n torch
if [ ! -d cwrap ]; then
    git clone https://github.com/torch/cwrap.git
fi


%build
cd cwrap


%install
cd cwrap
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lua_dir}/cwrap
cp -a README.md *.lua %{buildroot}%{lua_dir}/cwrap


%files
%{lua_dir}/cwrap/README.md
%{lua_dir}/cwrap/cinterface.lua
%{lua_dir}/cwrap/init.lua
%{lua_dir}/cwrap/types.lua


%changelog

