%define module fuse
%define oname fuse_python
# disable test for abf
%bcond_with test

Name:		python-fuse
Version:	1.0.9
Release:	1
Summary:	Python 2.x/3.x bindings for libfuse 2.x
License:	LGPL-2.1-only
URL:		https://github.com/libfuse/python-fuse
Source0:	https://github.com/libfuse/python-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
Group:		System/Libraries
BuildSystem: python

BuildRequires:	python
BuildRequires:	pkgconfig(python3)
BuildRequires:  pkgconfig(fuse)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)
%if %{with test}
BuildRequires:	python%{pyver}dist(pytest)
%endif
Requires:	fuse
Suggests: %{name}-doc = %{version}-%{release}

%description
Python 2.x/3.x binding for Fuse 2.x (Filesystem in Userspace).

%package -n %{name}-doc
Summary:        Documentation files for %name
Group:          Documentation/Other
BuildArch: noarch

%description -n %{name}-doc
HTML Documentation and examples for %name.

%prep
%autosetup -n %{name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{oname}.egg-info

%build
export CFLAGS="%{optflags}"
%py3_build

%install
%py3_install

%if %{with test}
%check
pip install -e .[test]
pytest -v tests/
%endif

%files
%{python3_sitearch}/%{module}parts
%{python3_sitearch}/%{module}.py
%{python3_sitearch}/%{oname}-%{version}*.*-info
%license COPYING
%doc README.md

%files -n %{name}-doc
%doc README.*
%doc FAQ
%doc AUTHORS
%doc example
