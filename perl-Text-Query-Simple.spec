%include	/usr/lib/rpm/macros.perl
Summary:	Text-Query-Simple perl module
Summary(pl):	Modu� perla Text-Query-Simple
Name:		perl-Text-Query-Simple
Version:	0.03
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Text/Text-Query-Simple-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Text-Query-Simple - matches text against simple query expression.

%description -l pl
Text-Query-Simple - wyszukuje tekst przy pomocy prostych wyra�e�
regularnych.

%prep
%setup -q -n Text-Query-Simple-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Text/Query/Simple
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes readme

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,readme}.gz

%{perl_sitelib}/Text/Query/Simple.pm
%{perl_sitearch}/auto/Text/Query/Simple

%{_mandir}/man3/*
