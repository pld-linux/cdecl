Summary:	Programs for encoding and decoding C and C++ function declarations
Summary(de):	Übersetzer von Deklarationen zwischen Englisch und C/C++
Summary(fr):	Traducteur anglais <--> déclarations C/C++
Summary(tr):	Ýngilizceden C/C++ bildirimlerine çevirici
Name:		cdecl
Version:	2.5
Release:	17
Copyright:	distributable
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narzêdzia
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Patch0:		cdecl-misc.patch
BuildRequires:	byacc
BuildRequires:	ncurses-devel >= 5.0
BuildRequires:	readline-devel >= 4.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

%description -l pl
Pakiet cdecl zawiera narzêdzia cdecl oraz c++decl, których u¿ywa sie
do t³umaczenia deklaracji funkcji C lub C++ na angielski i vice versa.

%description -l de
Dies ist ein Paket zum Übersetzen von Englisch in C/C++
Funktionsanweisungen und umgekehrt. Nützlich für Programmierer.

%description -l fr
C'est un package pour traduire de l'anglais en déclarations de
fonctions C/C++ et vice-versa. Utile pour les programmeurs.

%description -l tr
Ýngilizceden C/C++ bildirimlerine çeviri iþlemini ve tersini
gerçekleþtirmek için kullanýlan bir pakettir. Programcýlar için
kullanýþlýdýr.

%prep
%setup -q
%patch -p1

%build
%{__make} CFLAGS="$RPM_OPT_FLAGS -DUSE_READLINE -s" \
	LIBS="-lreadline -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
