Name:		Nervana-imgworker
Version:	0.0.1
Release:	1%{?dist}
Summary:	Multithreaded decoding and transforms of jpg strings

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/imgworker

BuildRequires:	boost-devel
Requires:	boost

%description
Multithreaded decoding and transforms of jpg strings


%prep
%setup -D -c -T -n NervanaSystems
if [ ! -d imgworker ]; then
    git clone https://github.com/NervanaSystems/imgworker.git
fi
cd imgworker

git checkout master
git pull


%build
cd imgworker
python setup.py bdist


%install
cd imgworker/dist
tarDir=`pwd`

mkdir -p %{buildroot}
cd %{buildroot}
tar -xzf $tarDir/imgworker*tar.gz


%files
%{python_sitearch}/_ImgWorker.so
%{python_sitearch}/imgworker*


%changelog

