Summary:	Process markdown into manpages
Name:		go-md2man
Version:	1.0.10
Release:	1
License:	MIT
Group:		Development/Tools
Source0:	https://github.com/cpuguy83/go-md2man/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	2f2ab80cbee456548790449a26cc2edc
URL:		https://github.com/cpuguy83/go-md2man
BuildRequires:	golang
BuildRequires:	golang-github-russross-blackfriday-devel
ExclusiveArch:	%{ix86} %{x8664} %{arm} aarch64 mips64 mips64le ppc64 ppc64le s390x

%define		_enable_debug_packages 0
%define		gobuild(o:) go build -mod=vendor -ldflags "${LDFLAGS:-} -B 0x$(head -c20 /dev/urandom|od -An -tx1|tr -d ' \\n')" -a -v -x %{?**};

%description
go-md2man is a golang tool using blackfriday to process markdown into
manpages.

%prep
%setup -q

mkdir -p src/github.com/cpuguy83
ln -s ../../../ src/github.com/cpuguy83/go-md2man

%build
export GOCACHE=$(pwd)/.go-cache

%gobuild -o bin/go-md2man github.com/cpuguy83/go-md2man

bin/go-md2man -in=go-md2man.1.md -out=go-md2man.1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}
cp -p bin/go-md2man $RPM_BUILD_ROOT%{_bindir}
install -p go-md2man.1 $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE.md
%attr(755,root,root) %{_bindir}/go-md2man
%{_mandir}/man1/*.1*
