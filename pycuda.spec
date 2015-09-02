Name:		pycuda
Version:	2015.1.3
Release:	1%{?dist}
Summary:	Python wrapper for Nvidia CUDA

Group:		Development/Languages
License:	MIT
URL:		https://pypi.python.org/pypi/pycuda
Source0:	pycuda-2015.1.3.tar.gz

#BuildRequires:	
#Requires:	

%description
Python wrapper for Nvidia CUDA


%prep
%setup -q


%build
./configure.py
python setup.py bdist

%install
cd dist
tarDir=`pwd`

mkdir -p %{buildroot}
cd %{buildroot}
tar -xzf $tarDir/pycuda*tar.gz


%files
/usr/lib64/python2.7/site-packages/pycuda*



%changelog

