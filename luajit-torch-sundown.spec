#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-sundown
Version:	0.0.1
Release:	1%{?dist}
Summary:	an interface to the Markdown implementation of the Sundown library

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/sundown-ffi

BuildRequires:	git, luajit-devel, gcc
Requires:	luajit

%description
an interface to the Markdown implementation of the Sundown library


%prep
%setup -D -c -T -n torch
if [ ! -d sundown-ffi ]; then
    git clone https://github.com/torch/sundown-ffi.git
fi


%build
cd sundown-ffi
cat >Makefile <<EOF

TARGET = libsundown.so

OBJECTS = src/autolink.o
OBJECTS += src/buffer.o
OBJECTS += src/markdown.o
OBJECTS += src/stack.o
OBJECTS += html/houdini_href_e.o
OBJECTS += html/houdini_html_e.o
OBJECTS += html/html.o
OBJECTS += html/html_smartypants.o

CFLAGS = -I src -I html -fPIC

\$(TARGET): \$(OBJECTS)
	gcc -shared -fPIC -o \$@ \$(OBJECTS)

.PHONY: clean
clean:
	rm -f \$(OBJECTS)
	rm -f \$(TARGET)
EOF

make clean
make


%install
cd sundown-ffi

mkdir -p %{buildroot}%{lua_dir}/sundown
mkdir -p %{buildroot}%{_libdir}/lua/5.1/

cp -a *.lua %{buildroot}%{lua_dir}/sundown/
cp libsundown.so %{buildroot}%{_libdir}/lua/5.1/


%files
%{_libdir}/lua/5.1/libsundown.so
%{lua_dir}/sundown


%changelog

