#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libpsl
Version  : 0.21.1
Release  : 10
URL      : https://github.com/rockdaboot/libpsl/releases/download/0.21.1/libpsl-0.21.1.tar.gz
Source0  : https://github.com/rockdaboot/libpsl/releases/download/0.21.1/libpsl-0.21.1.tar.gz
Summary  : Public Suffix List C library.
Group    : Development/Tools
License  : BSD-3-Clause MIT
Requires: libpsl-bin = %{version}-%{release}
Requires: libpsl-filemap = %{version}-%{release}
Requires: libpsl-lib = %{version}-%{release}
Requires: libpsl-license = %{version}-%{release}
Requires: libpsl-man = %{version}-%{release}
BuildRequires : buildreq-meson
BuildRequires : docbook-xml
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : gtk-doc
BuildRequires : gtk-doc-dev
BuildRequires : libxslt-bin
BuildRequires : pkg-config
BuildRequires : pkgconfig(32icu-uc)
BuildRequires : pkgconfig(32libidn)
BuildRequires : pkgconfig(icu-uc)
BuildRequires : pkgconfig(libidn)

%description


%package bin
Summary: bin components for the libpsl package.
Group: Binaries
Requires: libpsl-license = %{version}-%{release}
Requires: libpsl-filemap = %{version}-%{release}

%description bin
bin components for the libpsl package.


%package dev
Summary: dev components for the libpsl package.
Group: Development
Requires: libpsl-lib = %{version}-%{release}
Requires: libpsl-bin = %{version}-%{release}
Provides: libpsl-devel = %{version}-%{release}
Requires: libpsl = %{version}-%{release}

%description dev
dev components for the libpsl package.


%package dev32
Summary: dev32 components for the libpsl package.
Group: Default
Requires: libpsl-lib32 = %{version}-%{release}
Requires: libpsl-bin = %{version}-%{release}
Requires: libpsl-dev = %{version}-%{release}

%description dev32
dev32 components for the libpsl package.


%package filemap
Summary: filemap components for the libpsl package.
Group: Default

%description filemap
filemap components for the libpsl package.


%package lib
Summary: lib components for the libpsl package.
Group: Libraries
Requires: libpsl-license = %{version}-%{release}
Requires: libpsl-filemap = %{version}-%{release}

%description lib
lib components for the libpsl package.


%package lib32
Summary: lib32 components for the libpsl package.
Group: Default
Requires: libpsl-license = %{version}-%{release}

%description lib32
lib32 components for the libpsl package.


%package license
Summary: license components for the libpsl package.
Group: Default

%description license
license components for the libpsl package.


%package man
Summary: man components for the libpsl package.
Group: Default

%description man
man components for the libpsl package.


%prep
%setup -q -n libpsl-0.21.1
cd %{_builddir}/libpsl-0.21.1
pushd ..
cp -a libpsl-0.21.1 build32
popd
pushd ..
cp -a libpsl-0.21.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1656131731
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%configure --disable-static
make  %{?_smp_mflags}

pushd ../build32/
export PKG_CONFIG_PATH="/usr/lib32/pkgconfig:/usr/share/pkgconfig"
export ASFLAGS="${ASFLAGS}${ASFLAGS:+ }--32"
export CFLAGS="${CFLAGS}${CFLAGS:+ }-m32 -mstackrealign"
export CXXFLAGS="${CXXFLAGS}${CXXFLAGS:+ }-m32 -mstackrealign"
export LDFLAGS="${LDFLAGS}${LDFLAGS:+ }-m32 -mstackrealign"
%configure --disable-static    --libdir=/usr/lib32 --build=i686-generic-linux-gnu --host=i686-generic-linux-gnu --target=i686-clr-linux-gnu
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check
cd ../build32;
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || :

%install
export SOURCE_DATE_EPOCH=1656131731
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libpsl
cp %{_builddir}/libpsl-0.21.1/COPYING %{buildroot}/usr/share/package-licenses/libpsl/11688b6f9d81a04ed799175031d1edfe9aa6a0cf
cp %{_builddir}/libpsl-0.21.1/LICENSE %{buildroot}/usr/share/package-licenses/libpsl/5c185b7842aea33889989ac88bfd4ebae70c7dc9
cp %{_builddir}/libpsl-0.21.1/src/LICENSE.chromium %{buildroot}/usr/share/package-licenses/libpsl/73187e456b0901438d4982e4fcb4391a0e7dadef
pushd ../build32/
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
if [ -d %{buildroot}/usr/share/pkgconfig ]
then
pushd %{buildroot}/usr/share/pkgconfig
for i in *.pc ; do ln -s $i 32$i ; done
popd
fi
popd
pushd ../buildavx2/
%make_install_v3
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/psl
/usr/share/clear/optimized-elf/bin*

%files dev
%defattr(-,root,root,-)
/usr/include/libpsl.h
/usr/lib64/libpsl.so
/usr/lib64/pkgconfig/libpsl.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/libpsl.so
/usr/lib32/pkgconfig/32libpsl.pc
/usr/lib32/pkgconfig/libpsl.pc

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-libpsl

%files lib
%defattr(-,root,root,-)
/usr/lib64/glibc-hwcaps/x86-64-v3/libpsl.so
/usr/lib64/glibc-hwcaps/x86-64-v3/libpsl.so.5
/usr/lib64/glibc-hwcaps/x86-64-v3/libpsl.so.5.3.3
/usr/lib64/libpsl.so.5
/usr/lib64/libpsl.so.5.3.3

%files lib32
%defattr(-,root,root,-)
/usr/lib32/libpsl.so.5
/usr/lib32/libpsl.so.5.3.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libpsl/11688b6f9d81a04ed799175031d1edfe9aa6a0cf
/usr/share/package-licenses/libpsl/5c185b7842aea33889989ac88bfd4ebae70c7dc9
/usr/share/package-licenses/libpsl/73187e456b0901438d4982e4fcb4391a0e7dadef

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/psl-make-dafsa.1
/usr/share/man/man1/psl.1
