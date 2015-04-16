#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-uuid
Version:	0.2
Release:	1%{?dist}
Summary:	Generates uuids in pure Lua

Group:		Development/Languages
License:	Apache 2.0
URL:		https://github.com/Tieske/uuid

BuildRequires:	git
Requires:	luajit

%description
Generates uuids in pure Lua, but requires a 
good random seed or a unique string. Please check the documentation.


%prep
%setup -D -c -T -n Tieske
if [ ! -d uuid ]; then
    git clone https://github.com/Tieske/uuid.git
fi


%build
cd uuid


%install
cd uuid
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lua_dir}
cp -a src/uuid.lua %{buildroot}%{lua_dir}


%files
%{lua_dir}/uuid.lua


%changelog

