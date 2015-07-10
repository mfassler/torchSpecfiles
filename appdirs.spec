Name:		appdirs
Version:	1.4.0
Release:	1%{?dist}
Summary:	Python wrapper for Nvidia CUDA

Group:		Development/Languages
License:	MIT
URL:		https://pypi.python.org/pypi/appdirs
Source0:	appdirs-1.4.0.tar.gz

#BuildRequires:	
#Requires:	

%description
Python wrapper for Nvidia CUDA


%prep
%setup -q


%build
#./configure.py
python setup.py bdist

%install
cd dist
tarDir=`pwd`

mkdir -p %{buildroot}
cd %{buildroot}
tar -xzf $tarDir/appdirs*tar.gz


%files
/usr/lib/python2.7/site-packages/appdirs*



%changelog

