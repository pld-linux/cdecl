Summary:	Programs for encoding and decoding C and C++ function declarations
Summary(de.UTF-8):	Übersetzer von Deklarationen zwischen Englisch und C/C++
Summary(es.UTF-8):	Traductor inglés <--> declaraciones C/C++
Summary(fr.UTF-8):	Traducteur anglais <--> déclarations C/C++
Summary(pl.UTF-8):	Programy do kodowania i dekodowania deklaracji funkcji w C i C++
Summary(pt_BR.UTF-8):	Tradutor inglês <--> declarações C/C++
Summary(ru.UTF-8):	Транслятор English <--> декларации C/C++
Summary(tr.UTF-8):	İngilizceden C/C++ bildirimlerine çevirici
Summary(uk.UTF-8):	Транслятор English <--> декларації C/C++
Name:		cdecl
Version:	2.5
Release:	26
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

%description -l de.UTF-8
Dies ist ein Paket zum Übersetzen von Englisch in C/C++
Funktionsanweisungen und umgekehrt. Nützlich für Programmierer.

%description -l es.UTF-8
Este es un paquete para traducir inglés para declaraciones de
funciones C/C++ y viceversa. Útil para programadores.

%description -l fr.UTF-8
C'est un package pour traduire de l'anglais en déclarations de
fonctions C/C++ et vice-versa. Utile pour les programmeurs.

%description -l pl.UTF-8
Pakiet cdecl zawiera narzędzia cdecl oraz c++decl, których używa się
do tłumaczenia deklaracji funkcji C lub C++ na angielski i vice versa.

%description -l pt_BR.UTF-8
Este é um pacote para traduzir inglês para declarações de funções
C/C++ e vicer-versa. Útil para programadores.

%description -l ru.UTF-8
Используется для трансляции обычных описаний на английском языке в
декларации функций C/C++ и наоборот. Полезен для программистов.

%description -l tr.UTF-8
İngilizceden C/C++ bildirimlerine çeviri işlemini ve tersini
gerçekleştirmek için kullanılan bir pakettir. Programcılar için
kullanışlıdır.

%description -l uk.UTF-8
Використовується для перекладу описів англійською мовою в декларації
функцій C/C++ та навпаки. Корисний для програмістів.

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
