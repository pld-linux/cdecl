Summary:	Programs for encoding and decoding C and C++ function declarations.
Name:		cdecl
Version:	2.5
Release:	11
Copyright:	distributable
Group:		Development/Tools
Group(pl):	Programowanie/Narzêdzia
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Patch:		cdecl-misc.patch
BuildRequires:	byacc
BuildRoot:	/tmp/%{name}-%{version}-root

%description
The cdecl package includes the cdecl and c++decl utilities, which are used
to translate English to C or C++ function declarations and vice versa.

You should install the cdecl package if you intend to do C and/or C++
programming.

%prep
%setup -q
%patch -p1

%build
make CFLAGS="$RPM_OPT_FLAGS -DUSE_READLINE -s" \
	LIBS="-lreadline -lncurses"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/usr/{bin,share/man/man1}

make BINDIR=$RPM_BUILD_ROOT%{_bindir} MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \
	install

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
