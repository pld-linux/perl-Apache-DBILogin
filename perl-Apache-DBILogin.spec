%include	/usr/lib/rpm/macros.perl
%define		pdir	Apache
%define		pnam	DBILogin
Summary:	Apache::DBILogin - authenticates and authorizes via a DBI connection
Summary(pl.UTF-8):   Apache::DBILogin - uwierzytelnianie i autoryzacja poprzez połączenie z DBI
Name:		perl-Apache-DBILogin
Version:	2.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	45844b1aba2318535070b5e9bf2bcb6f
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::DBILogin allows authentication and authorization against a
multi-user database.

It is intended to facilitate web-based transactions against a database
server as a particular database user. If you wish authenticate against
a passwd table instead, please see Edmund Mergl's Apache::AuthDBI
module.

%description -l pl.UTF-8
Apache::DBILogin udostępnia mechanizmy uwierzytelniania i autoryzacji
przez wieloużytkownikową bazę danych.

Jest on zaprojektowany jako udogodnienie dla opartych na WWW
transakcji wykonywanych na serwerze bazy danych jako określony
użytkownik. Uwierzytelnianie na podstawie tabeli haseł obsługuje moduł
Apache::AuthDBI Edmunda Mergla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
