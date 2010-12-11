%define name orpheus
%define version 1.6
%define release %mkrel 7

%define Summary A text-mode player for CDs and MP3 files
%define title	Orpheus

Summary: 	%Summary
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPLv2+
Group:		Sound
URL: 		http://thekonst.net/orpheus/

Source: 	http://thekonst.net/download/%{name}-%{version}.tar.bz2

Patch0: 101_fix-buffer-overflow.diff
Patch1: patch.orpheus-1.5.add-start-stop-clear-1.diff
Patch2: patch.orpheus-1.5.fix-nexttrack-prevtrack-1.diff
Patch3: patch.orpheus-1.5.fix-play-n-1.diff
Patch4: improve-manpage.diff
Patch5: add-more-instructions.diff
Patch6: regenerate-configure-scripts.diff
Patch7: orpheus-1.6-fix_build_x86_64.diff
Patch8: orpheus-1.6-fix-gcc43.patch
BuildRoot: 	%_tmppath/%{name}-%{version}-%{release}-buildroot

# libghttp is now dead, do not build requires it
#BuildRequires:	libghttp-devel
BuildRequires:	libvorbis-devel, libncurses-devel
Requires:	mpg123, vorbis-tools

%description
Orpheus is a text-mode player for CDs and files of MP3 format. It can
retrieve CDDB information for compact-discs, and save and load
playlists. Nice interface to modify MP3 ID tags is provided.

%prep
%setup -q

%patch0 -p1 
%patch1 -p1 
%patch2 -p1 
%patch3 -p1 
%patch4 -p1 
%patch5 -p1 
%patch6 -p1 
%patch7 -p0 
%patch8 -p1 -b .gcc43

%build
%configure2_5x

%make WARM_CFLAGS=""

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(-, root, root)

%doc README COPYING INSTALL TODO ChangeLog

%{_bindir}/*
