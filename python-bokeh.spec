Name:		python-bokeh
Version:	0.10.0dev1
Release:	1%{?dist}
Summary:	Interactive Web Plotting for Python 

Group:		Development/Languages
License:	BSD
URL:		http://bokeh.pydata.org/en/latest/

#BuildRequires:
#Requires:

%description
Bokeh is a Python interactive visualization library that targets modern web 
browsers for presentation.  


%prep
%setup -D -c -T -n bokeh
if [ ! -d bokeh ]; then
    git clone https://github.com/bokeh/bokeh.git
fi
cd bokeh

git checkout master
git pull

git checkout 0.10.0dev1


%build
cd bokeh

cd bokehjs
npm install

cd ..
python setup.py build --build_js


%install
cd bokeh
python setup.py install --install_js -O1 --skip-build --root %{buildroot}

%files
%{_bindir}/bokeh-server
%{_bindir}/websocket_worker.py
/usr/lib/python2.7/site-packages/bokeh*
#%{python_sitearch}/bokeh*


%changelog

