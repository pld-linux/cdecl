Summary:	Programs for encoding and decoding C and C++ function declarations.
Name:		cdecl
Version:	2.5
Release:	10
Copyright:	distributable
Group:		Development/Tools
Source:		ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/%{name}-%{version}.tar.gz
Patch:		cdecl-misc.patch
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
install -d $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	install

gzip -9nf $RPM_BUILD_ROOT/usr/man/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) /usr/bin/*
/usr/man/man1/*

%changelog
* Thu Apr 15 1999 Tomasz K³oczko <kloczek@rudy.mif.pg.gda.pl>
  [2.5-10]
- added passing $RPM_OPT_FLAGS on compile time,
- added gzipping man pages,
- compile against ncurses.

* Sun Mar 21 1999 Cristian Gafton <gafton@redhat.com> 
- auto rebuild in the new build environment (release 9)

* Wed Dec 30 1998 Cristian Gafton <gafton@redhat.com>
- built for glibc 2.1

* Sat Aug 15 1998 Jeff Johnson <jbj@redhat.com>
- build root

* Tue May 05 1998 Prospector System <bugs@redhat.com>
- translations modified for de, fr, tr

* Fri Oct 10 1997 Erik Troan <ewt@redhat.com>
- built against readline lib w/ proper soname

* Thu Jul 10 1997 Erik Troan <ewt@redhat.com>
- built against glibc
