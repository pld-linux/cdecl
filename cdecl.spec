Summary:	Programs for encoding and decoding C and C++ function declarations
Summary(de):	�bersetzer von Deklarationen zwischen Englisch und C/C++
Summary(fr):	Traducteur anglais <--> d�clarations C/C++
Summary(pl):	Programy do kodowania i dekodowania deklaracji funkcji w C i C++
Summary(tr):	�ngilizceden C/C++ bildirimlerine �evirici
Name:		cdecl
Version:	2.5
Release:	21
License:	distributable
Group:		Development/Tools
Group(de):	Entwicklung/Werkzeuge
Group(fr):	Development/Outils
Group(pl):	Programowanie/Narz�dzia
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Patch0:		%{name}-misc.patch
Patch1:		%{name}-glibc.patch
BuildRequires:	flex
BuildRequires:	bison
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

%description -l pl
Pakiet cdecl zawiera narz�dzia cdecl oraz c++decl, kt�rych u�ywa si�
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
%patch0 -p1
%patch1 -p1

%build
bison -y cdgram.y && mv -f y.tab.c cdgram.c
%{__make} CFLAGS="%{rpmcflags} %{rpmldflags} -DUSE_READLINE" \
	LIBS="-lreadline -ltinfo"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1 \

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
