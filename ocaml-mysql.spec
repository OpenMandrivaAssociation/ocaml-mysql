%define name	ocaml-mysql
%define version	1.0.4
%define release	%mkrel 16

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Bindings for interacting with MySQL databases from ocaml
Source: 	http://raevnos.pennmush.org/code/ocaml-mysql/%{name}-%{version}.tar.bz2
URL:		http://raevnos.pennmush.org/code/ocaml-mysql/
License:	GPL
Group:		Development/Other
BuildRequires:	ocaml
BuildRequires:	camlp4
BuildRequires:	mysql-devel
BuildRequires:  ocaml-findlib
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module provides access to MySQL databases, roughly following the C API.

%package devel
Summary:	Development files for %{name}
Group:		Development/Other
Requires:   mysql-devel
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the development files needed to build applications
using %{name}.

%prep
%setup -q

%build
%configure2_5x
%make reallyall

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{_libdir}/ocaml/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{_libdir}/ocaml"
rm -f %{buildroot}/%{_libdir}/ocaml/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README VERSION
%dir %{_libdir}/ocaml/mysql
%{_libdir}/ocaml/mysql/*.cmi
%{_libdir}/ocaml/mysql/*.cma
%{_libdir}/ocaml/mysql/META
%{_libdir}/ocaml/stublibs/dllmysql_stubs.so

%files devel
%defattr(-,root,root)
%{_libdir}/ocaml/mysql/*.a
%{_libdir}/ocaml/mysql/*.cmx
%{_libdir}/ocaml/mysql/*.cmxa
%{_libdir}/ocaml/mysql/*.mli


%changelog
* Thu Dec 30 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-16mdv2011.0
+ Revision: 626552
- rebuilt against mysql-5.5.8 libs

* Thu Feb 18 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-14mdv2011.0
+ Revision: 507495
- rebuild

* Sat Jun 27 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-13mdv2010.0
+ Revision: 389924
- rebuild

* Wed Dec 24 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-12mdv2009.1
+ Revision: 318316
- site-lib hierarchy doesn't exists anymore

* Mon Dec 22 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-11mdv2009.1
+ Revision: 317643
- move non-devel files in main package

* Sat Dec 06 2008 Oden Eriksson <oeriksson@mandriva.com> 1.0.4-10mdv2009.1
+ Revision: 311341
- rebuilt against mysql-5.1.30 libs

* Wed Jul 30 2008 Thierry Vignaud <tv@mandriva.org> 1.0.4-9mdv2009.0
+ Revision: 254267
- rebuild

* Tue Mar 04 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-7mdv2008.1
+ Revision: 178368
- rebuild

* Wed Jan 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-6mdv2008.1
+ Revision: 153665
- build native interface too (Andre Nathan <andre@digirati.com.br>)

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-5mdv2008.0
+ Revision: 78234
- drop useless conflict, the files are identical

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-4mdv2008.0
+ Revision: 78167
- fix interdependency
  swap stub libs to non-devel package
  add conflicts to help upgrade

* Sat Sep 01 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-3mdv2008.0
+ Revision: 77542
- drop macro definition, now in rpm-mandriva-setup
  ship .cmi file in non-devel subpackage


* Tue Feb 20 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-2mdv2007.0
+ Revision: 123143
- requires corresponding native devel package

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2007.1
+ Revision: 122717
- fix build dependencies

* Mon Feb 19 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.4-1mdv2007.1
- first mdv release

