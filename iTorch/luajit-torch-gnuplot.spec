#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-gnuplot
Version:	0.0.1
Release:	1%{?dist}
Summary:	helps you generate Lua/C wrappers

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/gnuplot

BuildRequires:	git
Requires:	luajit

%description
The __wrap__ package helps you to automate the generation of Lua/C wrappers
around existing C functions, such that these functions would be callable
from Lua. This package is used by the __torch__ package, but does not depend on
anything, and could be used by anyone using Lua.


%prep
%setup -D -c -T -n torch
if [ ! -d gnuplot ]; then
    git clone https://github.com/torch/gnuplot.git
fi


%build
cd gnuplot


%install
cd gnuplot
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lua_dir}/gnuplot
cp -a README.md *.lua %{buildroot}%{lua_dir}/gnuplot


%files
%{lua_dir}/gnuplot


%changelog

