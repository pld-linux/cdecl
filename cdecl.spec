Summary:	Programs for encoding and decoding C and C++ function declarations
Summary(de):	эbersetzer von Deklarationen zwischen Englisch und C/C++
Summary(es):	Traductor inglИs <--> declaraciones C/C++
Summary(fr):	Traducteur anglais <--> dИclarations C/C++
Summary(pl):	Programy do kodowania i dekodowania deklaracji funkcji w C i C++
Summary(pt_BR):	Tradutor inglЙs <--> declaraГУes C/C++
Summary(ru):	Транслятор English <--> декларации C/C++
Summary(tr):	щngilizceden C/C++ bildirimlerine Гevirici
Summary(uk):	Транслятор English <--> декларац╕╖ C/C++
Name:		cdecl
Version:	2.5
Release:	25
License:	distributable
Group:		Development/Tools
Source0:	ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
# Source0-md5:	29895dab52e85b2474a59449e07b7996
Patch0:		%{name}-misc.patch
BuildRequires:	bison
BuildRequires:	flex
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

%description -l de
Dies ist ein Paket zum эbersetzen von Englisch in C/C++
Funktionsanweisungen und umgekehrt. NЭtzlich fЭr Programmierer.

%description -l es
Este es un paquete para traducir inglИs para declaraciones de
funciones C/C++ y viceversa. зtil para programadores.

%description -l fr
C'est un package pour traduire de l'anglais en dИclarations de
fonctions C/C++ et vice-versa. Utile pour les programmeurs.

%description -l pl
Pakiet cdecl zawiera narzЙdzia cdecl oraz c++decl, ktСrych u©ywa siЙ
do tЁumaczenia deklaracji funkcji C lub C++ na angielski i vice versa.

%description -l pt_BR
Este И um pacote para traduzir inglЙs para declaraГУes de funГУes
C/C++ e vicer-versa. зtil para programadores.

%description -l ru
Используется для трансляции обычных описаний на английском языке в
декларации функций C/C++ и наоборот. Полезен для программистов.

%description -l tr
щngilizceden C/C++ bildirimlerine Гeviri iЧlemini ve tersini
gerГekleЧtirmek iГin kullanЩlan bir pakettir. ProgramcЩlar iГin
kullanЩЧlЩdЩr.

%description -l uk
Використову╓ться для перекладу опис╕в англ╕йською мовою в декларац╕╖
функц╕й C/C++ та навпаки. Корисний для програм╕ст╕в.

%prep
%setup -q
%patch0 -p1

%build
bison -y cdgram.y && mv -f y.tab.c cdgram.c
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} %{rpmldflags} -DUSE_READLINE" \
	LIBS="-lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1}

%{__make} install \
	BINDIR=$RPM_BUILD_ROOT%{_bindir} \
	MANDIR=$RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
