%define name python-fuse
%define cvsversion 20070509
%define version 2.5
%define release %mkrel 1

Name:		%name
Summary:	Python binding for Fuse (Filesystem in Userspace)
URL:		http://fuse.sourceforge.net/wiki/index.php/FusePython
Source0:	%{name}-cvs%{cvsversion}.tar.bz2
License:	LGPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Group:		System/Libraries
BuildRequires:	python-devel, fuse-devel
Requires:	fuse
Version:	%version
Release:	%release

%description
Python binding for Fuse (Filesystem in Userspace).

%prep
%setup -q -n %{name}-cvs%{cvsversion}

%build
%{__python} setup.py build

%install
%{__rm} -Rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT

%clean
%{__rm} -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.1st README.new_fusepy_api FAQ
%py_platsitedir/*

