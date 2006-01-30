#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	HTTP
%define	pnam	Request-AsCGI
Summary:	HTTP::Request::AsCGI - Setup a CGI enviroment from a HTTP::Request
Summary(pl):	HTTP::Request::AsCGI - ustawianie �rodowiska CGI z HTTP::Request
Name:		perl-HTTP-Request-AsCGI
Version:	0.5
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e1f5d332969d072a19d9649ed7d77f59
URL:		http://search.cpan.org/dist/HTTP-Request-AsCGI/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Class-Accessor
BuildRequires:	perl-libwww >= 5.805
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides a convinient way of setting up an CGI enviroment from a
HTTP::Request.

%description -l pl
Ten modu� udost�pnia �atw� metod� ustawiania �rodowiska CGI z
HTTP::Request.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
cp -a examples $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/HTTP/Request/*.pm
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
