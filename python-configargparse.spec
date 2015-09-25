%if 0%{?fedora} > 12
%global with_python3 1
%else
%{!?__python2: %global __python2 /usr/bin/python2}
%{!?python2_sitelib: %global python2_sitelib %(%{__python2} -c "from distutils.sysconfig import get_python_lib; print (get_python_lib())")}
%endif

%global scrname ConfigArgParse

Name:           python-configargparse
Version:        0.9.3
Release:        1%{?dist}
Summary:        A Python module with support for argparse, config files, and env variables

License:        MIT
URL:            https://github.com/bw2/ConfigArgParse
Source0:        https://pypi.python.org/packages/source/C/%{scrname}/%{scrname}-%{version}.tar.gz
Buildarch:      noarch

BuildRequires:  python2-devel
BuildRequires:  python-setuptools

%if 0%{?with_python3}
BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%endif

%description
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.

%if 0%{?with_python3}
%package -n python3-configargparse
Summary:        A Python module with support for argparse, config files, and env variables

Requires:       python3
BuildArch:      noarch

%description -n python3-configargparse
Applications with more than a handful of user-settable options are best
configured through a combination of command line args, config files, hard
coded defaults, and in some cases, environment variables.

Python’s command line parsing modules such as argparse have very limited
support for config files and environment variables, so this module extends
argparse to add these features.
%endif

%prep
%setup -q -n %{scrname}-%{version}
find -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python2}|'
%if 0%{?with_python3}
rm -rf %{py3dir}
cp -a . %{py3dir}
find %{py3dir} -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
%endif

%build
%{__python2} setup.py build
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py build
popd
%endif # with_python3

%install
%if 0%{?with_python3}
pushd %{py3dir}
%{__python3} setup.py install --skip-build --root %{buildroot}
popd
%endif # with_python3
%{__python2} setup.py install --skip-build --root %{buildroot}

%files
%doc README.rst
%license LICENSE
%{python2_sitelib}/configargparse.py*
%{python2_sitelib}/%{scrname}*.egg-info

%if 0%{?with_python3}
%files -n python3-configargparse
%doc README.rst
%license LICENSE
%{python3_sitelib}/configargparse.py*
%{python3_sitelib}/%{scrname}*.egg-info
%{python3_sitelib}/__pycache__/configargparse*
%endif # with_python3

%changelog
* Thu Feb 05 2015 Fabian Affolter <mail@fabian-affolter.ch> - 0.9.3-1
- Initial package
