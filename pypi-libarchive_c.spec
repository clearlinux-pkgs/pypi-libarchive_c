#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-libarchive_c
Version  : 3.2
Release  : 49
URL      : https://files.pythonhosted.org/packages/0c/91/bf5e8861ab011752fd9f2680ffd9a130cd3990badc722f0e020da2646c28/libarchive-c-3.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/0c/91/bf5e8861ab011752fd9f2680ffd9a130cd3990badc722f0e020da2646c28/libarchive-c-3.2.tar.gz
Summary  : Python interface to libarchive
Group    : Development/Tools
License  : CC0-1.0
Requires: pypi-libarchive_c-python = %{version}-%{release}
Requires: pypi-libarchive_c-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: libarchive-c
Provides: libarchive-c-python
Provides: libarchive-c-python3
BuildRequires : libarchive-dev

%description
.. image:: https://travis-ci.org/Changaco/python-libarchive-c.svg
:target: https://travis-ci.org/Changaco/python-libarchive-c

%package python
Summary: python components for the pypi-libarchive_c package.
Group: Default
Requires: pypi-libarchive_c-python3 = %{version}-%{release}

%description python
python components for the pypi-libarchive_c package.


%package python3
Summary: python3 components for the pypi-libarchive_c package.
Group: Default
Requires: python3-core
Provides: pypi(libarchive_c)

%description python3
python3 components for the pypi-libarchive_c package.


%prep
%setup -q -n libarchive-c-3.2
cd %{_builddir}/libarchive-c-3.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641453284
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
