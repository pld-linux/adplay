Summary:	AdLib music player for the command line
Summary(pl.UTF-8):	Odtwarzacz muzyki AdLib działający z linii poleceń
Name:		adplay
Version:	1.5
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	http://dl.sourceforge.net/adplug/%{name}-%{version}.tar.bz2
# Source0-md5:	18e1ac84b6f07d0388902a083f400da7
URL:		http://adplug.sourceforge.net/
BuildRequires:	adplug-devel >= 2.0
BuildRequires:	alsa-lib-devel >= 0.9.1
BuildRequires:	esound-devel
BuildRequires:	pkgconfig
Requires:	adplug >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
AdPlay/UNIX is AdPlug's UNIX console-based frontend. AdPlug is a free,
universal OPL2 audio playback library. AdPlay/UNIX supports the full
range of AdPlug's file format playback features. Despite this, at the
moment, only emulated OPL2 output is supported by AdPlay/UNIX, but
this on a wide range of output devices.

%description -l pl.UTF-8
AdPlay/UNIX to frontend AdPluga dla uniksowej konsoli. AdPlug to
wolnodostępna, uniwersalna biblioteka otwarzania dźwięku OPL2.
AdPlay/UNIX obsługuje cały zakres możliwości odtwarzania formatów
plików AdPluga. Niezależnie od tego przez AdPlay/UNIX aktualnie
obsługiwane jest tylko emulowane wyjście OPL2, ale za to na wielu
różnych urządzeniach wyjściowych.

%prep
%setup -q

%build
%configure \
	--disable-output-sdl \
	--disable-output-qsa
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/adplay
%{_mandir}/man1/adplay.1*
