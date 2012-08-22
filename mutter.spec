#
# Conditional build:
%bcond_with	gnome2		# build with support for GNOME2 wm-properties
#
Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		mutter
Version:	3.5.90
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mutter/3.5/%{name}-%{version}.tar.xz
# Source0-md5:	31a127c43e2e3b15739feb05df354767
URL:		http://git.gnome.org/cgit/mutter
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	clutter-devel >= 1.9.10
BuildRequires:	cogl-devel >= 1.9.6
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.3.0
BuildRequires:	gtk+3-devel >= 3.3.7
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	pkgconfig
# only in configure.in
BuildRequires:	python >= 1:2.5
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	tar >= 1:1.22
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.2
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gsettings-desktop-schemas >= 3.3.0
Requires:	zenity
Provides:	gnome-wm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display
engine using the Clutter toolkit with solid window-management logic
inherited from the Metacity window manager.

%description -l pl.UTF-8
Mutter to zarządca okien i składania wyświetlający pulpit i
zarządzający nim poprzez OpenGL. Łączy wyszukany silnik wyświetlania
wykorzystujący toolkit Clutter z solidną logiką zarządcy okien
odziedziczoną z zarządcy okien Metacity.

%package libs
Summary:	Mutter shared library
Summary(pl.UTF-8):	Biblioteka współdzielona zarządcy okien Mutter
Group:		Libraries
Requires:	cairo >= 1.10
Requires:	clutter >= 1.9.10
Requires:	cogl >= 1.9.6
Requires:	glib2 >= 1:2.26.0
Requires:	gtk+3 >= 3.3.7
Requires:	libcanberra-gtk3 >= 0.26
Requires:	startup-notification >= 0.7
Requires:	xorg-lib-libXcomposite >= 0.2
Conflicts:	mutter < 3.4.0-2

%description libs
Mutter shared library.

%description libs -l pl.UTF-8
Biblioteka współdzielona zarządcy okien i składania Mutter.

%package devel
Summary:	Development package for Mutter
Summary(pl.UTF-8):	Pakiet programistyczny do wtyczek zarządcy okien Mutter
Group:		X11/Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	cairo-devel >= 1.10
Requires:	clutter-devel >= 1.9.10
Requires:	cogl-devel >= 1.9.6
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+3-devel >= 3.3.7
Requires:	libcanberra-gtk3-devel >= 0.26
Requires:	startup-notification-devel >= 0.7
Requires:	xorg-lib-libXcomposite-devel >= 0.2
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrender-devel

%description devel
Header files for developing Mutter plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek zarządcy okien i składania
Mutter.

%prep
%setup -q

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ZENITY=/usr/bin/zenity \
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_gnome2:%{__rm} $RPM_BUILD_ROOT%{_datadir}/gnome/wm-properties/mutter-wm.desktop}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%glib_compile_schemas

%postun
%glib_compile_schemas

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS HACKING doc/theme-format.txt rationales.txt
%attr(755,root,root) %{_bindir}/mutter
%attr(755,root,root) %{_bindir}/mutter-message
%attr(755,root,root) %{_bindir}/mutter-theme-viewer
%attr(755,root,root) %{_bindir}/mutter-window-demo
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
%{_desktopdir}/mutter.desktop
%{?with_gnome2:%{_datadir}/gnome/wm-properties/mutter-wm.desktop}
%{_datadir}/mutter
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-windows.xml
%{_mandir}/man1/mutter.1*
%{_mandir}/man1/mutter-message.1*
%{_mandir}/man1/mutter-theme-viewer.1*
%{_mandir}/man1/mutter-window-demo.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmutter.so.0
%dir %{_libdir}/mutter
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter.so
%{_includedir}/mutter
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.gir
%{_pkgconfigdir}/libmutter.pc
%{_pkgconfigdir}/mutter-plugins.pc
