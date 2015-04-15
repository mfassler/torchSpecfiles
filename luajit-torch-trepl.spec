#%define lua_dir /usr/share/luajit-2.0.3/
%define lua_dir /usr/share/lua/5.1/

Name:		luajit-torch-trepl
Version:	0.0.1
Release:	1%{?dist}
Summary:	Improved REPL for luajit+torch

Group:		Development/Languages
License:	BSD
URL:		https://github.com/torch/trepl

BuildRequires:	git, luajit-devel, readline-devel
Requires:	luajit, readline

%description
Improved REPL for luajit+torch


%prep
%setup -D -c -T -n torch
if [ ! -d trepl ]; then
    git clone https://github.com/torch/trepl.git
fi


%build
cd trepl
cat >Makefile <<EOF
TARGET = readline.so

OBJECTS = readline.o

CFLAGS = -I /usr/include/luajit-2.0 -fPIC

\$(TARGET): \$(OBJECTS)
	gcc -shared -fPIC -l readline -o \$@ \$(OBJECTS)

.PHONY: clean
clean:
	rm -f \$(OBJECTS)
	rm -f \$(TARGET)
EOF
make clean
make

%install
cd trepl
rm -rf %{buildroot}
mkdir -p %{buildroot}%{lua_dir}/trepl
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/lua/5.1

cp -a  *.lua %{buildroot}%{lua_dir}/trepl
cp -a th %{buildroot}%{_bindir}
chmod +xxx %{buildroot}%{_bindir}/th
cp readline.so %{buildroot}%{_libdir}/lua/5.1/

%files
#%{lua_dir}/trepl/README.md
%{lua_dir}/trepl/init.lua
%{lua_dir}/trepl/colors.lua
%{lua_dir}/trepl/colorize.lua
%{_bindir}/*
%{_libdir}/lua/5.1/*

%changelog

