%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Query-Simple
Summary:	Text::Query::Simple perl module
Summary(pl):	Modu³ perla Text::Query::Simple
Name:		perl-Text-Query-Simple
Version:	0.03
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text::Query::Simple - matches text against simple query expression.

%description -l pl
Text::Query::Simple - wyszukuje tekst przy pomocy prostych wyra¿eñ
regularnych.

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
%doc Changes readme
%{perl_vendorlib}/Text/Query/Simple.pm
%{_mandir}/man3/*
