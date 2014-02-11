Summary:	File compression and packaging utility compatible with ARJ for MS-DOS
Name:		arj
Version:	3.10.22
Release:	11
License:	GPLv2+
Group:		Archiving/Compression
Url:		http://arj.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/arj/%{name}-%{version}.tar.bz2
Patch:		arj-3.10.21-debian-arches-align.patch
Patch1:		arj-3.10.22-fix_format_string.patch
Patch2:		arj-3.10.2-fix_strnlen_redefinition.patch
Patch3:		arj-3.10.22-quotes.patch
BuildRequires:	automake

%description
A portable version of the ARJ archiver, available for a growing number
of DOS-like and UNIX-like platforms on a variety of architectures.
This aims for compatibility with the original ARJ archiver by ARJ
Software, Inc.

%files
%doc doc/*
%{_bindir}/arj
%{_bindir}/arj-register
%{_bindir}/arjdisp
%{_bindir}/rearj
%dir %{_libdir}/arj/
%{_libdir}/arj/arjcrypt.so
%{_mandir}/man1/*.1*

#----------------------------------------------------------------------------

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
%configure2_5x
cd ..
make prepare
#disable binary strippings
#gw strange errors from the postproc command
make ADD_LDFLAGS="" || make || make || make

%install
%makeinstall_std


