Name:		python-fuse
Summary:	Python 2.x/3.x bindings for libfuse 2.x
URL:		https://github.com/libfuse/python-fuse
Source0:	https://github.com/libfuse/python-fuse/archive/v%{version}/%{name}-%{version}.tar.gz
License:	LGPL
BuildRoot:	%{_tmppath}/%{name}-%{version}-root
Group:		System/Libraries
BuildRequires:	python-devel
BuildRequires:  python2-devel
BuildRequires:  pkgconfig(fuse)
Requires:	fuse
Version:	1.0.0
Release:	1

%description
Python 2.x/3.x binding for Fuse 2.x (Filesystem in Userspace).

%prep
%setup -q

%build
%{__python} setup.py build
%{__python2} setup.py build

%install
%{__rm} -Rf $RPM_BUILD_ROOT
%{__python} setup.py install --root $RPM_BUILD_ROOT
%{__python2} setup.py install --root $RPM_BUILD_ROOT

%clean
%{__rm} -Rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc AUTHORS COPYING README.1st README.new_fusepy_api FAQ
%py_platsitedir/*

%changelog
* Tue Sep 15 2009 Thierry Vignaud <tv@mandriva.org> 2.5-5mdv2010.0
+ Revision: 442114
- rebuild

* Sun Dec 28 2008 Funda Wang <fwang@mandriva.org> 2.5-4mdv2009.1
+ Revision: 320160
- rebuild for new python

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 2.5-3mdv2009.0
+ Revision: 242410
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Thu Jul 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 2.5-1mdv2008.0
+ Revision: 55847
- update to new version 2.5

* Wed May 09 2007 Nicolas Vigier <nvigier@mandriva.com> 0.20070509-1mdv2008.0
+ Revision: 25760
- Import python-fuse

