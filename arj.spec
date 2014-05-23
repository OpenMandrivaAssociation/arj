%define name arj
%define version 3.10.22

Summary:	File compression and packaging utility compatible with ARJ for MS-DOS
Name:		arj
Version:	3.10.22
Release:	13
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
* Tue Jan 07 2014 Tomasz Paweł Gajc <tpgxyz@gmail.com> 3.10.22-13
+ Revision: 80677ad
- rebuild


