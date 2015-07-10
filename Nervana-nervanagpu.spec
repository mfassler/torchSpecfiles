Name:		Nervana-nervanagpu
Version:	0.8.2
Release:	1%{?dist}
Summary:	Python-based Deep Learning Framework

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/nervanagpu

#BuildRequires:	PyYAML >= 3.11
Requires:	pycuda, pytools, appdirs

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

