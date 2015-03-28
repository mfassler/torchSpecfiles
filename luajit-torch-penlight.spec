%global luaver 5.1
%global luapkgdir %{_datadir}/lua/%{luaver}

# there's a circular (build) dependency with lua-ldoc
%global with_docs 1

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		luajit-torch-penlight
Version:	1.3.1
Release:	5%{?dist}
Summary:	Penlight Lua Libraries
License:	MIT
URL:		https://github.com/stevedonovan/Penlight
Source0:	https://github.com/stevedonovan/Penlight/archive/%{version}/Penlight-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	lua >= %{luaver}
#BuildRequires:	lua-filesystem
#BuildRequires:	lua-markdown
Requires:	luajit
Requires:	luajit-torch-luafilesystem

%global __requires_exclude_from %{_docdir}

%description
Penlight brings together a set of generally useful pure Lua modules,
focusing on input data handling (such as reading configuration
files), functional programming (such as map, reduce, placeholder
expressions,etc), and OS path management.  Much of the functionality
is inspired by the Python standard libraries.


%prep
%setup -q -n Penlight-%{version}


%build
# nothing to do here


%install
mkdir -p %{buildroot}%{luapkgdir}
cp -av lua/pl %{buildroot}%{luapkgdir}

# fix scripts
chmod -x %{buildroot}%{luapkgdir}/pl/dir.lua



%files
%{luapkgdir}/pl



%changelog
* Fri Mar 27 2015 Mark Fassler
- parallel install for lua-5.1, for use with luajit with torch7

* Sun Jan 18 2015 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-5
- Own the package doc dir.
- Remove extra .md suffix from generated HTML files.

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-4
- build with docs

* Fri Jan 16 2015 Tom Callaway <spot@fedoraproject.org> - 1.3.1-3
- rebuild for lua 5.3

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Nov  3 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.3.1-1
- Update to 1.3.1.
- Use a single package doc dir.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.1.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue May 14 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.0-2
- rebuild with docs

* Sun May 12 2013 Tom Callaway <spot@fedoraproject.org> - 1.1.0-1.1
- rebuild for lua 5.2, no docs

* Thu Mar 21 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.1.0-1
- Update to 1.1.0.

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.3-4.a
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jan 10 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-3.a
- Add BR on lua-filesystem (needed when running the tests).
- Fix line-endings for the examples.

* Wed Jan  9 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-2.a
- Fix typos.
- Package examples as a separate subpackage.
- Run tests.

* Fri Jan  4 2013 Thomas Moschny <thomas.moschny@gmx.de> - 1.0.3-1.a
- New package.
