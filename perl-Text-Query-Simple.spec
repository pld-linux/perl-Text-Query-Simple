%include	/usr/lib/rpm/macros.perl
%define	pdir	Text
%define	pnam	Query-Simple
Summary:	Text-Query-Simple perl module
Summary(pl):	Modu� perla Text-Query-Simple
Name:		perl-Text-Query-Simple
Version:	0.03
Release:	8
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Query-Simple - matches text against simple query expression.

%description -l pl
Text-Query-Simple - wyszukuje tekst przy pomocy prostych wyra�e�
regularnych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf Changes readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Text/Query/Simple.pm
%{_mandir}/man3/*
