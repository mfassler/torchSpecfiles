#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-xlua
Version:	1.0.1
Release:	1%{?dist}
Summary:	A set of useful extensions to Lua

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/xlua

BuildRequires:	git
Requires:	luajit

%description
Lua is pretty compact in terms of built-in functionalities:
this package extends the table and string libraries, 
and provide other general purpose tools (progress bar, ...).


%prep
%setup -D -c -T -n torch
if [ ! -d xlua ]; then
    git clone https://github.com/torch/xlua.git
fi


%build
cd xlua


%install
cd xlua
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lua_dir}/xlua
cp -a README.md *.lua %{buildroot}%{lua_dir}/xlua


%files
%{lua_dir}/xlua/init.lua
%{lua_dir}/xlua/OptionParser.lua
%{lua_dir}/xlua/Profiler.lua
%{lua_dir}/xlua/README.md


%changelog

