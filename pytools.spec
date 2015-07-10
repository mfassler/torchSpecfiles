Name:		pytools
Version:	2015.1.2
Release:	1%{?dist}
Summary:	Python wrapper for Nvidia CUDA

Group:		Development/Languages
License:	MIT
URL:		https://pypi.python.org/pypi/pytools
Source0:	pytools-2015.1.2.tar.gz

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
tar -xzf $tarDir/pytools*tar.gz


%files
/usr/lib/python2.7/site-packages/pytools*



%changelog

