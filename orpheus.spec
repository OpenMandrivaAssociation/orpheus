%define name orpheus
%define version 1.5
%define release %mkrel 2

%define Summary A text-mode player for CDs and MP3 files
%define title	Orpheus

Summary: 	%Summary
Name: 		%name
Version: 	%version
Release: 	%release
License: 	GPL
Group:		Sound
URL: 		http://thekonst.net/orpheus/

Source: 	http://thekonst.net/download/%{name}-%{version}.tar.bz2

Patch0:		orpheus-mixerctl.patch
Patch1:		orpheus-uitext.patch
Patch2:		orpheus-oggtrack.patch
BuildRoot: 	%_tmppath/%{name}-%{version}-%{release}-buildroot

BuildRequires:	libghttp-devel, libvorbis-devel, libncurses-devel
Requires:	mpg123, vorbis-tools

%description
Orpheus is a text-mode player for CDs and files of MP3 format. It can
retrieve CDDB information for compact-discs, and save and load
playlists. Nice interface to modify MP3 ID tags is provided.

%prep
%setup -q

%patch0 -p0 -b .mixerctl
%patch1 -p0 -b .uitext
%patch2 -p0 -b .oggtrack

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
%{_datadir}/locale/*

