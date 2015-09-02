Name:		Nervana-nervanagpu
Version:	0.3.3
Release:	1%{?dist}
Summary:	Python-based Deep Learning Framework

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/nervanagpu

#BuildRequires:	PyYAML >= 3.11
Requires:	numpy, pycuda, pytools, appdirs

%description
Python-based Deep Learning Framework


%prep
%setup -D -c -T -n NervanaSystems
if [ ! -d nervanagpu ]; then
    git clone https://github.com/NervanaSystems/nervanagpu.git
fi
cd nervanagpu

git checkout master
git pull

# 2015-08-25, version 0.3.3:
git checkout e6392353cd6f92


%build
cd nervanagpu
rm -rf dist
python setup.py bdist


%install
cd nervanagpu/dist
tarDir=`pwd`

mkdir -p %{buildroot}
cd %{buildroot}
tar -xzf $tarDir/nervanagpu*tar.gz


%files
/usr/lib/python2.7/site-packages/nervanagpu*
#%{python_sitearch}/nervanagpu*


%changelog

