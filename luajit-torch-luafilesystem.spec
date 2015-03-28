%global luaver 5.1
%global lualibdir %{_libdir}/lua/%{luaver}

Name:           luajit-torch-luafilesystem
Version:        1.6.2
Release:        4%{?dist}
Summary:        File System Library for the Lua Programming Language

Group:          Development/Libraries
License:        MIT
URL:            http://www.keplerproject.org/luafilesystem/
Source0:        http://cloud.github.com/downloads/keplerproject/luafilesystem/luafilesystem-%{version}.tar.gz
%if 0%{?el5}
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
%endif

BuildRequires:  luajit-devel
Requires:       luajit

%description
LuaFileSystem is a Lua library developed to complement the set of functions
related to file systems offered by the standard Lua distribution.

LuaFileSystem offers a portable way to access the underlying directory
structure and file attributes.

%prep
%setup -q -n luafilesystem-%{version}


%build
make %{?_smp_mflags} PREFIX=%{_prefix} LUA_LIBDIR=%{lualibdir} CFLAGS="%{optflags} -fPIC -I/usr/include/luajit-2.0"


%install
rm -rf $RPM_BUILD_ROOT
make install PREFIX=$RPM_BUILD_ROOT%{_prefix} LUA_LIBDIR=$RPM_BUILD_ROOT%{lualibdir}


%check
LUA_CPATH=$RPM_BUILD_ROOT%{lualibdir}/\?.so luajit tests/test.lua


%if 0%{?rhel}
%clean
rm -rf $RPM_BUILD_ROOT
%endif


%files
%defattr(-,root,root,-)
# We don't want the docs to clash with the RPM for lua-5.2:
#%doc doc/us/*
#%doc README
%{lualibdir}/*


%changelog
* Fri Mar 27 2015 Mark Fassler 
- This is a cheap-and-dirty build to use with luajit, pretending to be a lua-5.1 module.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri May 10 2013 Tom Callaway <spot@fedoraproject.org> - 1.6.2-3
- rebuild for lua 5.2

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Oct  8 2012 Michel Salim <salimma@fedoraproject.org> - 1.6.2-1
- Update to 1.6.2
- Spec cleanup

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Aug 16 2011 Michel Salim <salimma@fedoraproject.org> - 1.5.0-1
- Update to 1.5.0
- Enable tests

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Sep 29 2009 Tim Niemueller <tim@niemueller.de> - 1.4.2-1
- Upgrade to latest stable release

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu May 08 2008 Tim Niemueller <tim@niemueller.de> - 1.4.1-1
- Upgrade to latest stable release

* Sat Apr 05 2008 Tim Niemueller <tim@niemueller.de> - 1.4.0-3
- Add patch to add missing include of stdlib.h

* Sat Apr 05 2008 Tim Niemueller <tim@niemueller.de> - 1.4.0-2
- Pass correct CFLAGS to make to produce proper debuginfo

* Fri Apr 04 2008 Tim Niemueller <tim@niemueller.de> - 1.4.0-1
- Initial package

