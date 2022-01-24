#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-libarchive_c
Version  : 4.0
Release  : 50
URL      : https://files.pythonhosted.org/packages/93/c4/d8fa5dfcfef8aa3144ce4cfe4a87a7428b9f78989d65e9b4aa0f0beda5a8/libarchive-c-4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/93/c4/d8fa5dfcfef8aa3144ce4cfe4a87a7428b9f78989d65e9b4aa0f0beda5a8/libarchive-c-4.0.tar.gz
Summary  : Python interface to libarchive
Group    : Development/Tools
License  : CC0-1.0
Requires: pypi-libarchive_c-python = %{version}-%{release}
Requires: pypi-libarchive_c-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : libarchive-dev
BuildRequires : pypi(py)
BuildRequires : pypi-pluggy
BuildRequires : pypi-pytest
BuildRequires : pypi-tox
BuildRequires : pypi-virtualenv

%description
A Python interface to libarchive. It uses the standard ctypes_ module to
dynamically load and access the C library.

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
%setup -q -n libarchive-c-4.0
cd %{_builddir}/libarchive-c-4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1643042533
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
