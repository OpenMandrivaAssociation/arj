%define name arj
%define version 3.10.22
%define release 9

Summary:	File compression and packaging utility compatible with ARJ for MS-DOS
Name:		arj
Version:	3.10.22
Release:	11
Source0:	http://prdownloads.sourceforge.net/arj/%{name}-%{version}.tar.bz2
Patch:		arj-3.10.21-debian-arches-align.patch
Patch1:		arj-3.10.22-fix_format_string.patch
Patch2:		arj-3.10.2-fix_strnlen_redefinition.patch
Patch3:		arj-3.10.22-quotes.patch
License:	GPLv2
BuildRequires:	automake
Group:		Archiving/Compression
Url:		http://arj.sourceforge.net/


%description
A portable version of the ARJ archiver, available for a growing number
of DOS-like and UNIX-like platforms on a variety of architectures.
This aims for compatibility with the original ARJ archiver by ARJ
Software, Inc.

%prep
%setup -q
%patch -p1
%patch1 -p0
%patch2 -p0 
%patch3 -p1

cd gnu
# (misc) fix compile on x86_64, as the platform is otherwise not recognized
# by the current config.sub
cp /usr/share/automake-1.13/config.sub .
autoconf

%build
cd gnu
%configure
cd ..
make prepare
#disable binary strippings
#gw strange errors from the postproc command
make ADD_LDFLAGS="" || make || make || make

%install
%makeinstall

%files
%defattr(-,root,root)
%doc doc/*
%_bindir/arj
%_bindir/arj-register
%_bindir/arjdisp
%_bindir/rearj
%dir %_libdir/arj/
%_libdir/arj/arjcrypt.so
%_mandir/man1/*.1*



%changelog
* Fri Sep 09 2011 GÃ¶tz Waschk <waschk@mandriva.org> 3.10.22-7mdv2012.0
+ Revision: 699090
- rebuild

* Mon Sep 07 2009 Michael Scherer <misc@mandriva.org> 3.10.22-6mdv2011.0
+ Revision: 432473
- fix build ( patch 2 ), since newer glibc have strnlen
- fix the license, thanks to Andrey Bondrov
- adapt to build with newer automake

* Sat Mar 07 2009 Michael Scherer <misc@mandriva.org> 3.10.22-5mdv2009.1
+ Revision: 351512
- fix build on x86_64
- fix build, patch 1, correct format string error

  + Antoine Ginies <aginies@mandriva.com>
    - rebuild
    - rebuild

* Thu Jun 19 2008 Thierry Vignaud <tv@mandriva.org> 3.10.22-3mdv2009.0
+ Revision: 226169
- rebuild

* Thu Dec 20 2007 Olivier Blin <blino@mandriva.org> 3.10.22-2mdv2008.1
+ Revision: 135823
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request


* Sat Jun 24 2006 GÃ¶tz Waschk <waschk@mandriva.org> 3.10.22-2mdk
- Rebuild
- use mkrel

* Thu Jun 23 2005 Götz Waschk <waschk@mandriva.org> 3.10.22-1mdk
- New release 3.10.22

* Tue Apr 19 2005 Götz Waschk <waschk@mandriva.org> 3.10.21-1mdk
- initial package

