Name:		Nervana-neon
Version:	0.8.2
Release:	1%{?dist}
Summary:	Python-based Deep Learning Framework

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/neon

BuildRequires:	PyYAML >= 3.11
Requires:	Nervana-imgworker, PyYAML >= 3.11

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

