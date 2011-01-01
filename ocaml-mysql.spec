%define name	ocaml-mysql
%define version	1.0.4
%define release	%mkrel 17

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
