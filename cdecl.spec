Summary:	Programs for encoding and decoding C and C++ function declarations
Summary(de):	�bersetzer von Deklarationen zwischen Englisch und C/C++
Summary(fr):	Traducteur anglais <--> d�clarations C/C++
Summary(tr):	�ngilizceden C/C++ bildirimlerine �evirici
Name:		cdecl
Version:	2.5
Release:	17
Copyright:	distributable
Group:		Development/Tools
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
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
Pakiet cdecl zawiera narz�dzia cdecl oraz c++decl, kt�rych u�ywa sie
do t�umaczenia deklaracji funkcji C lub C++ na angielski i vice versa.

%description -l de
Dies ist ein Paket zum �bersetzen von Englisch in C/C++
Funktionsanweisungen und umgekehrt. N�tzlich f�r Programmierer.

%description -l fr
C'est un package pour traduire de l'anglais en d�clarations de
fonctions C/C++ et vice-versa. Utile pour les programmeurs.

%description -l tr
�ngilizceden C/C++ bildirimlerine �eviri i�lemini ve tersini
ger�ekle�tirmek i�in kullan�lan bir pakettir. Programc�lar i�in
kullan��l�d�r.

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
