
Name:		python-ipython
Version:	3.1.0
Release:	1%{?dist}
Summary:	a rich architecture for interactive computing

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
%setup -D -c -T -n ipython
if [ ! -d ipython ]; then
    git clone https://github.com/ipython/ipython.git
fi
cd ipython

git submodule init
#git checkout master
#git pull
git submodule update
git checkout rel-3.1.0



%build
cd ipython
#python setup.py bdist_rpm
python setup.py build


%install
cd ipython
python setup.py install --prefix=%{buildroot}/usr


%files
%{_bindir}/*
/usr/lib/python2.7/site-packages/*
%{_mandir}/man1/*

%changelog




