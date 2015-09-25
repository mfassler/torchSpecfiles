Name:		Nervana-neon
Version:	1.0.0rc1
Release:	1%{?dist}
Summary:	Python-based Deep Learning Framework

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/neon

BuildRequires:	PyYAML >= 3.11, Nervana-maxas >= 1.06
Requires:	Nervana-imgworker, PyYAML >= 3.11, h5py

%description
Python-based Deep Learning Framework


%prep
%setup -D -c -T -n NervanaSystems
if [ ! -d neon ]; then
    git clone https://github.com/NervanaSystems/neon.git
fi
cd neon

git checkout master
git pull

# 2015-09-19, v1.0.0rc1
git checkout 18863f1c79133153


%build
cd neon
rm -rf dist
python setup.py bdist


%install
cd neon/dist
tarDir=`pwd`

mkdir -p %{buildroot}
cd %{buildroot}
tar -xzf $tarDir/neon*tar.gz


%files
%{_bindir}/neon
%{_bindir}/nvis
/usr/lib/python2.7/site-packages/neon*
#%{python_sitearch}/neon*


%changelog

