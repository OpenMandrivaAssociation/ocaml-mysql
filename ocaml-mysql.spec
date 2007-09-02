%define name	ocaml-mysql
%define version	1.0.4
%define release	%mkrel 5

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
BuildRequires:  findlib
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
%make

%install
rm -rf %{buildroot}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}
install -d -m 755 %{buildroot}/%{ocaml_sitelib}/stublibs
make install OCAMLFIND_INSTFLAGS="-destdir %{buildroot}/%{ocaml_sitelib}"
rm -f %{buildroot}/%{ocaml_sitelib}/stublibs/*.owner

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc CHANGES COPYING README VERSION
%dir %{ocaml_sitelib}/mysql
%{ocaml_sitelib}/mysql/*.cmi
%{ocaml_sitelib}/stublibs/dllmysql_stubs.so

%files devel
%defattr(-,root,root)
%{ocaml_sitelib}/mysql/*
%exclude %{ocaml_sitelib}/mysql/*.cmi
