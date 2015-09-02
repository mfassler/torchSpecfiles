
Name:		Nervana-maxas
Version:	1.03
Release:	1%{?dist}
Summary:	Assembler for NVIDIA Maxwell GPUs

Group:		Development/Languages
License:	MIT
URL:		https://github.com/NervanaSystems/maxas
#Source0:	

BuildRequires:	perl-ExtUtils-MakeMaker
#Requires:	

%description
Assembler for NVIDIA Maxwell GPUs


%prep
%setup -D -c -T -n NervanaSystems
if [ ! -d maxas ]; then
	git clone https://github.com/NervanaSystems/maxas.git
fi
cd maxas
git checkout master
git pull

# Version 1.03:
git checkout 38d5d9ea4d56931


%build
cd maxas
perl Makefile.PL PREFIX=/usr
make %{?_smp_mflags}


%install
cd maxas
make install DESTDIR=%{buildroot}


%files
#%doc
%{_bindir}/maxas.pl
/usr/lib64/perl5/auto/MaxAs
/usr/lib64/perl5/perllocal.pod
%{_mandir}/man*/MaxAs*
/usr/share/perl5/MaxAs


%changelog

