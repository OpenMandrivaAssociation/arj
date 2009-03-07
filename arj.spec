%define name arj
%define version 3.10.22
%define release %mkrel 5

Summary: File compression and packaging utility compatible with ARJ for MS-DOS
Name: %{name}
Version: %{version}
Release: %{release}
Source0: http://prdownloads.sourceforge.net/arj/%{name}-%{version}.tar.bz2
Patch: arj-3.10.21-debian-arches-align.patch
Patch1: arj-3.10.22-fix_format_string.patch
License: GPL
BuildRequires: automake
Group: Archiving/Compression
Url: http://arj.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
A portable version of the ARJ archiver, available for a growing number
of DOS-like and UNIX-like platforms on a variety of architectures.
This aims for compatibility with the original ARJ archiver by ARJ
Software, Inc.

%prep
%setup -q
%patch -p1
%patch1 -p0

cd gnu
# (misc) fix compile on x86_64, as the platform is otherwise not recognized
# by the current config.sub
cp /usr/share/automake-1.10/config.sub .
autoconf

%build
cd gnu
%configure
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

