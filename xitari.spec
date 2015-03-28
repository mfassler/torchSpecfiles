
Name:		xitari
Version:	0.0.1
Release:	1%{?dist}
Summary:	Emulator for the Atari 2600

Group:		Applications/Emulators
License:	GPL
URL:		https://github.com/deepmind/xitari

%description


%prep
%setup -D -c -T -n deepmind
if [ ! -d xitari ]; then
    git clone https://github.com/deepmind/xitari.git
fi


%build
cd xitari
rm -rf build
mkdir build
cd build
cmake .. 
make


%install
# The install seems to be broken, so we'll do it by hand for now
cd xitari
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}
mkdir -p %{buildroot}%{_includedir}/xitari
cp -a build/ale %{buildroot}%{_bindir}/
cp -a build/libxitar* %{buildroot}%{_libdir}/
cp -a ale_interface.hpp %{buildroot}%{_includedir}/xitari/


%files
%{_bindir}/*
%{_libdir}/*
%{_includedir}/xitari/

%changelog

