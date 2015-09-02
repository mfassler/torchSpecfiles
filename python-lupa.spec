Name:		python-lupa
Version:	1.1
Release:	1%{?dist}
Summary:	Python wrapper around Lua and LuaJIT

Group:		Development/Languages
License:	MIT
URL:		https://pypi.python.org/pypi/lupa
Source0:	lupa-%{version}.tar.gz

#BuildRequires:	PyYAML >= 3.11
#Requires:	Nervana-imgworker, PyYAML >= 3.11

%description
Python wrapper around Lua and LuaJIT


%prep
%setup -q -n lupa-%{version}


%build
rm -rf dist
python setup.py bdist


%install
cd dist
tarDir=`pwd`

mkdir -p %{buildroot}
cd %{buildroot}
tar -xzf $tarDir/lupa*tar.gz


%files
/usr/lib64/python2.7/site-packages/lupa*


%changelog

