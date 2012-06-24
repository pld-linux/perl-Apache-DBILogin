%include	/usr/lib/rpm/macros.perl
%define	pdir	Apache
%define	pnam	DBILogin
Summary:	Apache::DBILogin - authenticates and authorizes via a DBI connection
Summary(pl):	Apache::DBILogin - uwierzytelnianie i autoryzacja poprzez po��czenie z DBI
Name:		perl-%{pdir}-%{pnam}
Version:	2.0
Release:	2
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1706789ce1f6ed733baae6448af59b4e
BuildRequires:	perl-devel >= 5
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Apache::DBILogin allows authentication and authorization against a
multi-user database.

It is intended to facilitate web-based transactions against a database
server as a particular database user.  If you wish authenticate against
a passwd table instead, please see Edmund Mergl's Apache::AuthDBI module.

%description -l pl
Apache::DBILogin udost�pnia mechanizmy uwierzytelniania i autoryzacji
przez wielou�ytkownikow� baz� danych.

Jest on zaprojektowany jako udogodnienie dla opartych na WWW
transakcji wykonywanych na serwerze bazy danych jako okre�lony
u�ytkownik. Uwierzytelnianie na podstawie tabeli hase� obs�uguje modu�
Apache::AuthDBI Edmunda Mergla.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{_mandir}/man3/*
