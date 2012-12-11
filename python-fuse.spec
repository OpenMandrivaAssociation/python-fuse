%define name python-fuse
%define cvsversion 20070509
%define version 2.5
%define release %mkrel 5

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

