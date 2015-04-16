%global luaver 5.1
%global luapkgdir %{_datadir}/lua/%{luaver}

%{!?_pkgdocdir: %global _pkgdocdir %{_docdir}/%{name}-%{version}}

Name:		luajit-cjson
Version:	2.1.0
Release:	0%{?dist}
Summary:	A fast JSON encoding/parsing module
License:	MIT
URL:		http://www.kyne.com.au/~mark/software/lua-cjson.php
Source0:	http://www.kyne.com.au/~mark/software/download/lua-cjson-2.1.0.tar.gz
BuildRequires:	luajit-devel
Requires:	luajit


%description
CJSON module provides JSON support for Lua. It features:
 - Fast, standards compliant encoding/parsing routines
 - Full support for JSON with UTF-8, including decoding surrogate pairs
 - Optional run-time support for common exceptions to the JSON specification
    (infinity, NaN,..)
 - No dependencies on other libraries


%prep
%setup -q -n lua-cjson-%{version}


%build
make \
 PREFIX=/usr \
 LUA_INCLUDE_DIR=/usr/include/luajit-2.0 \
 LUA_CMODULE_DIR=%{_libdir}/lua/5.1 \
 %{?_smp_mflags}


%install
make install \
 PREFIX=/usr \
 LUA_INCLUDE_DIR=/usr/include/luajit-2.0 \
 LUA_CMODULE_DIR=%{_libdir}/lua/5.1 \
 DESTDIR=%{buildroot}

#make install-extra \
# PREFIX=/usr \
# LUA_INCLUDE_DIR=/usr/include/luajit-2.0 \
# LUA_CMODULE_DIR=%{_libdir}/lua/5.1 \
# DESTDIR=%{buildroot}


%files
%{_libdir}/lua/5.1/*


%changelog


