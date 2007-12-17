%define name arj
%define version 3.10.22
%define release %mkrel 2

Summary: File compression and packaging utility compatible with ARJ for MS-DOS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/arj/%{name}-%{version}.tar.bz2
Patch: arj-3.10.21-debian-arches-align.patch
License: GPL
Group: Archiving/Compression
Url: http://arj.sourceforge.net/

%description
A portable version of the ARJ archiver, available for a growing number
of DOS-like and UNIX-like platforms on a variety of architectures.
This aims for compatibility with the original ARJ archiver by ARJ
Software, Inc.

%prep
%setup -q
%patch -p1
cd gnu
autoconf

%build
cd gnu
%configure2_5x
cd ..
make prepare
#gw strange errors from the postproc command
make || make || make || make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

%clean
rm -rf $RPM_BUILD_ROOT

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

