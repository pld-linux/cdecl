Summary: Programs for encoding and decoding C and C++ function declarations.
Name: cdecl
Version: 2.5
Release: 9
Copyright: distributable
Group: Development/Tools
Source: ftp://sunsite.unc.edu/pub/Linux/devel/lang/c/cdecl-2.5.tar.gz
Patch: cdecl-2.5.misc.patch
BuildRoot: /var/tmp/cdecl-root

%description
The cdecl package includes the cdecl and c++decl utilities, which are
used to translate English to C or C++ function declarations and vice
versa.

You should install the cdecl package if you intend to do C and/or C++
programming.

%prep
%setup -q
%patch -p1

%build
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/{bin,man/man1}

make BINDIR=$RPM_BUILD_ROOT/usr/bin MANDIR=$RPM_BUILD_ROOT/usr/man/man1 \
	install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
/usr/bin/cdecl
/usr/bin/c++decl
/usr/man/man1/cdecl.1
/usr/man/man1/c++decl.1

%changelog
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
