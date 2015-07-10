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

git checkout setup.cfg
git checkout master
git pull


%build
cd neon
# BUG:  this "-e" thing isn't working for me...
#make -e GPU=cudanet

sed -i -e 's/^GPU/#GPU/g' setup.cfg
echo 'GPU = cudanet' >> setup.cfg
#echo 'GPU = nervanagpu' >> setup.cfg

make


%install
cd neon

mkdir -p %{buildroot}/usr/lib/python2.7/site-packages
PYTHONPATH=%{buildroot}/usr/lib/python2.7/site-packages
python setup.py install --prefix=%{buildroot}/usr

rm -f %{buildroot}/usr/lib/python2.7/site-packages/PyYAML-3.11-py2.7-linux-x86_64.egg
rm %{buildroot}/usr/lib/python2.7/site-packages/easy-install.pth
rm %{buildroot}/usr/lib/python2.7/site-packages/site.py*
mv %{buildroot}/usr/lib/python2.7/site-packages/neon-0.8.2-py2.7.egg/neon %{buildroot}/usr/lib/python2.7/site-packages/


%files
%{_bindir}/hyperopt
%{_bindir}/neon
/usr/lib/python2.7/site-packages/neon*
#%{python_sitearch}/neon*


%changelog

