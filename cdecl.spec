Summary:	Programs for encoding and decoding C and C++ function declarations
Summary(de):	�bersetzer von Deklarationen zwischen Englisch und C/C++
Summary(es):	Traductor ingl�s <--> declaraciones C/C++
Summary(fr):	Traducteur anglais <--> d�clarations C/C++
Summary(pl):	Programy do kodowania i dekodowania deklaracji funkcji w C i C++
Summary(pt_BR):	Tradutor ingl�s <--> declara��es C/C++
Summary(ru):	���������� English <--> ���������� C/C++
Summary(tr):	�ngilizceden C/C++ bildirimlerine �evirici
Summary(uk):	���������� English <--> �������æ� C/C++
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
Dies ist ein Paket zum �bersetzen von Englisch in C/C++
Funktionsanweisungen und umgekehrt. N�tzlich f�r Programmierer.

%description -l es
Este es un paquete para traducir ingl�s para declaraciones de
funciones C/C++ y viceversa. �til para programadores.

%description -l fr
C'est un package pour traduire de l'anglais en d�clarations de
fonctions C/C++ et vice-versa. Utile pour les programmeurs.

%description -l pl
Pakiet cdecl zawiera narz�dzia cdecl oraz c++decl, kt�rych u�ywa si�
do t�umaczenia deklaracji funkcji C lub C++ na angielski i vice versa.

%description -l pt_BR
Este � um pacote para traduzir ingl�s para declara��es de fun��es
C/C++ e vicer-versa. �til para programadores.

%description -l ru
������������ ��� ���������� ������� �������� �� ���������� ����� �
���������� ������� C/C++ � ��������. ������� ��� �������������.

%description -l tr
�ngilizceden C/C++ bildirimlerine �eviri i�lemini ve tersini
ger�ekle�tirmek i�in kullan�lan bir pakettir. Programc�lar i�in
kullan��l�d�r.

%description -l uk
����������դ���� ��� ��������� ���Ӧ� ���̦������ ����� � �������æ�
����æ� C/C++ �� �������. �������� ��� ������ͦ�Ԧ�.

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
