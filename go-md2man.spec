Summary:	Process markdown into manpages
Summary(pl.UTF-8):	Przetwarzanie formatu markdown do stron man
Name:		go-md2man
Version:	2.0.3
Release:	1
License:	MIT
Group:		Development/Tools
#Source0Download: https://github.com/cpuguy83/go-md2man/releases
Source0:	https://github.com/cpuguy83/go-md2man/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	59716d2bf2400e109b3d9070197bc2c1
URL:		https://github.com/cpuguy83/go-md2man
BuildRequires:	golang >= 1.11
BuildRequires:	rpmbuild(macros) >= 2.009
ExclusiveArch:	%go_arches
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_enable_debug_packages 0
%define		gobuild(o:) %__go build -mod=vendor -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};

%description
go-md2man is a golang tool using blackfriday to process markdown into
manpages.

%description -l pl.UTF-8
go-md2man to napisane w języku Go narzędzie wykorzystujące blackfriday
do przetwarzania formatu markdown do stron man.

%prep
%setup -q

%build
%gobuild -o bin/go-md2man github.com/cpuguy83/go-md2man/v2

bin/go-md2man -in=go-md2man.1.md -out=go-md2man.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

install bin/go-md2man $RPM_BUILD_ROOT%{_bindir}
cp -p go-md2man.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%attr(755,root,root) %{_bindir}/go-md2man
%{_mandir}/man1/go-md2man.1*
