#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-mdurl
Version  : 0.1.1
Release  : 6
URL      : https://files.pythonhosted.org/packages/d1/ff/2f02e94382daee347ca6cfd33fde421e891398d83c51d05f25941f7f93e9/mdurl-0.1.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/d1/ff/2f02e94382daee347ca6cfd33fde421e891398d83c51d05f25941f7f93e9/mdurl-0.1.1.tar.gz
Summary  : Markdown URL utilities
Group    : Development/Tools
License  : MIT
Requires: pypi-mdurl-license = %{version}-%{release}
Requires: pypi-mdurl-python = %{version}-%{release}
Requires: pypi-mdurl-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(flit_core)

%description
# mdurl
[![Build Status](https://github.com/executablebooks/mdurl/workflows/Tests/badge.svg?branch=master)](https://github.com/executablebooks/mdurl/actions?query=workflow%3ATests+branch%3Amaster+event%3Apush)
[![codecov.io](https://codecov.io/gh/executablebooks/mdurl/branch/master/graph/badge.svg)](https://codecov.io/gh/executablebooks/mdurl)
[![PyPI version](https://img.shields.io/pypi/v/mdurl)](https://pypi.org/project/mdurl)

%package license
Summary: license components for the pypi-mdurl package.
Group: Default

%description license
license components for the pypi-mdurl package.


%package python
Summary: python components for the pypi-mdurl package.
Group: Default
Requires: pypi-mdurl-python3 = %{version}-%{release}

%description python
python components for the pypi-mdurl package.


%package python3
Summary: python3 components for the pypi-mdurl package.
Group: Default
Requires: python3-core
Provides: pypi(mdurl)

%description python3
python3 components for the pypi-mdurl package.


%prep
%setup -q -n mdurl-0.1.1
cd %{_builddir}/mdurl-0.1.1
pushd ..
cp -a mdurl-0.1.1 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1653342919
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 -m build --wheel --skip-dependency-check --no-isolation
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -m build --wheel --skip-dependency-check --no-isolation

popd

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-mdurl
cp %{_builddir}/mdurl-0.1.1/LICENSE %{buildroot}/usr/share/package-licenses/pypi-mdurl/b87bd47e069fa27d2243d1638d435a9d5081ccff
pip install --root=%{buildroot} --no-deps --ignore-installed dist/*.whl
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
pip install --root=%{buildroot}-v3 --no-deps --ignore-installed dist/*.whl
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot}/usr/share/clear/optimized-elf/ %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-mdurl/b87bd47e069fa27d2243d1638d435a9d5081ccff

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
