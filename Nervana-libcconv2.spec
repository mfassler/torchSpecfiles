Name:		Nervana-libcconv2
Version:	0.0.1
Release:	1%{?dist}
Summary:	Build/run convolutional neural networks on the GPU

Group:		Development/Languages
License:	Apache
URL:		https://github.com/NervanaSystems/cuda-convnet2

BuildRequires:	cmake, cuda, atlas-devel
#Requires:	

%description
Build/run convolutional neural networks on the GPU


%prep
%setup -D -c -T -n NervanaSystems
if [ ! -d cuda-convnet2 ]; then
	git clone https://github.com/NervanaSystems/cuda-convnet2.git

fi
cd cuda-convnet2

git checkout master
git pull


%build
cd cuda-convnet2
rm -rf build
mkdir build
cd build

## FIXME: there's probably a better way to do this:
# (plus, cuda has it's own blas library...)
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/lib64/atlas

cmake .. \
 -DCMAKE_INSTALL_PREFIX=/usr \
 -DCUDA_SDK_ROOT_DIR=/usr/local/cuda 

make %{?_smp_mflags}


%install
cd cuda-convnet2/build
make install DESTDIR=%{buildroot}
mv %{buildroot}/usr/lib %{buildroot}/usr/lib64


%files
%{_libdir}/libcconv*


%changelog

