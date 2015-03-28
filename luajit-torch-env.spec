#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-env
Version:	0.0.1
Release:	1%{?dist}
Summary:	Sets up default Torch environment

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/env

BuildRequires:	git
Requires:	luajit

%description
Environment setup for Torch.  Adds pretty printing and additional path 
handling to luajit.


%prep
%setup -D -c -T -n torch
if [ ! -d env ]; then
    git clone https://github.com/torch/env.git
fi


%build
cd env


%install
cd env
rm -rf %{buildroot}

mkdir -p %{buildroot}%{lua_dir}/env
cp -a *.lua %{buildroot}%{lua_dir}/env


%files
%{lua_dir}/env/init.lua


%changelog

