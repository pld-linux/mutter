Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		mutter
Version:	3.22.0
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mutter/3.22/%{name}-%{version}.tar.xz
# Source0-md5:	e448039015b355e7e2b9f86087e2f399
URL:		http://git.gnome.org/cgit/mutter
BuildRequires:	Mesa-libgbm-devel >= 10.3
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-tools
BuildRequires:	glib2-devel >= 1:2.50.0
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.22.0
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	json-glib-devel
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libdrm-devel
BuildRequires:	libinput-devel
BuildRequires:	libtool >= 2:2.2.6
BuildRequires:	libwacom-devel >= 0.13
# xcb-randr
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel >= 1:1.2.0
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-glib-devel
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	wayland-devel >= 1.6.90
BuildRequires:	wayland-protocols >= 1.7
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.2
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel
BuildRequires:	xorg-lib-libXi-devel >= 1.7
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.3
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.35.1
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gsettings-desktop-schemas >= 3.22.0
Requires:	zenity
Provides:	gnome-wm
Obsoletes:	mutter-apidocs < 3.18
Obsoletes:	mutter-wayland < 3.14
Obsoletes:	mutter-wayland-apidocs < 3.14
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
Requires:	Mesa-libgbm >= 10.3
Requires:	cairo >= 1.10.0
Requires:	glib2 >= 1:2.50.0
Requires:	gnome-desktop >= 3.0
Requires:	gtk+3 >= 3.20.0
Requires:	libcanberra-gtk3 >= 0.26
Requires:	startup-notification >= 0.7
Requires:	upower-libs >= 0.99.0
Requires:	wayland >= 1.6.90
Requires:	xorg-lib-libXcomposite >= 0.2
Requires:	xorg-lib-libXi >= 1.7
Obsoletes:	mutter-wayland-libs < 3.14
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
Requires:	cairo-devel >= 1.10.0
Requires:	glib2-devel >= 1:2.50.0
Requires:	gtk+3-devel >= 3.20.0
Requires:	libcanberra-gtk3-devel >= 0.26
Requires:	startup-notification-devel >= 0.7
Requires:	xorg-lib-libXcomposite-devel >= 0.2
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXfixes-devel
Requires:	xorg-lib-libXrender-devel
Obsoletes:	mutter-wayland-devel < 3.14

%description devel
Header files for developing Mutter plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek zarządcy okien i składania
Mutter.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	ZENITY=/usr/bin/zenity \
	--enable-compile-warnings=maximum \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la
%{__rm} $RPM_BUILD_ROOT%{_libdir}/mutter/*.la

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
%doc NEWS doc/*.txt
%attr(755,root,root) %{_bindir}/mutter
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
%attr(755,root,root) %{_libexecdir}/mutter-restart-helper
%{_desktopdir}/mutter.desktop
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-windows.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-navigation.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-system.xml
%{_mandir}/man1/mutter.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmutter.so.0
%dir %{_libdir}/mutter
%attr(755,root,root) %{_libdir}/mutter/libmutter-clutter-1.0.so
%attr(755,root,root) %{_libdir}/mutter/libmutter-cogl-pango.so
%attr(755,root,root) %{_libdir}/mutter/libmutter-cogl-path.so
%attr(755,root,root) %{_libdir}/mutter/libmutter-cogl.so
# intentionally installed in package-private dir
%{_libdir}/mutter/Cally-*.typelib
%{_libdir}/mutter/Clutter-*.typelib
%{_libdir}/mutter/ClutterX11-*.typelib
%{_libdir}/mutter/Cogl-*.typelib
%{_libdir}/mutter/CoglPango-*.typelib
%{_libdir}/mutter/Meta-*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter.so
%{_includedir}/mutter
# intentionally installed in package-private dir
%{_libdir}/mutter/Cally-*.gir
%{_libdir}/mutter/Clutter-*.gir
%{_libdir}/mutter/ClutterX11-*.gir
%{_libdir}/mutter/Cogl-*.gir
%{_libdir}/mutter/CoglPango-*.gir
%{_libdir}/mutter/Meta-*.gir
%{_pkgconfigdir}/libmutter.pc
%{_pkgconfigdir}/mutter-clutter-1.0.pc
%{_pkgconfigdir}/mutter-clutter-x11-1.0.pc
%{_pkgconfigdir}/mutter-cogl-1.0.pc
%{_pkgconfigdir}/mutter-cogl-pango-1.0.pc
%{_pkgconfigdir}/mutter-cogl-path-1.0.pc

