Name:		Nervana-neon82
Version:	0.8.2
Release:	1%{?dist}
Summary:	Python-based Deep Learning Framework

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/neon

BuildRequires:	PyYAML >= 3.11
Requires:	Nervana-imgworker, PyYAML >= 3.11, python-posix_ipc

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

# 2015-07-08, v0.8.2:
git checkout 5d28ddfc512afbfb3

# The very next commit breaks RecurrentLSTMLayer for nervanagpu:
#git checkout 19829290a7 #breaks


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
%{_bindir}/hyperopt
%{_bindir}/neon
/usr/lib/python2.7/site-packages/neon*
#%{python_sitearch}/neon*


%changelog

