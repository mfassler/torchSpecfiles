
Name:		python-terminado
Version:	0.5
Release:	1%{?dist}
Summary:	python-tornado websock backend for the term.js Javascript terminal emulator library

Group:		Development/Libraries
License:	BSD
URL:		https://github.com/facebook/iTorch

BuildRequires:	git

%description
A rich architecture for interactive computing with:
 * Powerful interactive shells (terminal and Qt-based).
 * A browser-based notebook with support for code, text, mathematical expressions, inline plots and other rich media.
 * Support for interactive data visualization and use of GUI toolkits
 * Flexible, embeddable interpreters to load into your own projects
 * Easy to use, high performance tools for parallel computing


%prep
%setup -D -c -T -n takluyver
if [ ! -d terminado ]; then
    git clone https://github.com/takluyver/terminado.git
fi
cd terminado

git checkout master
git pull
git submodule init
git submodule update
git checkout 0.5



%build
cd terminado
#python setup.py bdist_rpm
python setup.py build


%install
cd terminado
python setup.py install --prefix=%{buildroot}/usr


%files
/usr/lib/python2.7/site-packages/*

%changelog




