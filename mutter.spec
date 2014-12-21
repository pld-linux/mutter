Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		mutter
Version:	3.14.3
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mutter/3.14/%{name}-%{version}.tar.xz
# Source0-md5:	0f5b6beea5ae58c9ad1073ca8e47e19a
URL:		http://git.gnome.org/cgit/mutter
BuildRequires:	Mesa-libgbm-devel >= 10.3
BuildRequires:	autoconf >= 2.62
BuildRequires:	automake >= 1:1.11
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	clutter-devel >= 1.20.0
BuildRequires:	cogl-devel >= 1.18.0
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.26.0
BuildRequires:	gnome-common
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gsettings-desktop-schemas-devel >= 3.8.0
BuildRequires:	gtk+3-devel >= 3.10.0
BuildRequires:	gtk-doc >= 1.15
BuildRequires:	intltool >= 0.41.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libdrm-devel
BuildRequires:	libinput-devel
BuildRequires:	libtool >= 2:2.2.6
# xcb-randr
BuildRequires:	libxcb-devel
BuildRequires:	pango-devel >= 1:1.2.0
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	rpmbuild(macros) >= 1.98
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	systemd-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	wayland-devel >= 1.5.90
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
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libxkbcommon-devel
BuildRequires:	xorg-lib-libxkbcommon-x11-devel
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.26.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gsettings-desktop-schemas >= 3.8.0
Requires:	zenity
Provides:	gnome-wm
Obsoletes:	mutter-wayland < 3.14
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
Requires:	clutter >= 1.20.0
Requires:	cogl >= 1.18.0
Requires:	glib2 >= 1:2.26.0
Requires:	gnome-desktop >= 3.0
Requires:	gtk+3 >= 3.10.0
Requires:	libcanberra-gtk3 >= 0.26
Requires:	startup-notification >= 0.7
Requires:	upower-libs >= 0.99.0
Requires:	wayland >= 1.5.90
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
Requires:	clutter-devel >= 1.20.0
Requires:	cogl-devel >= 1.18.0
Requires:	glib2-devel >= 1:2.26.0
Requires:	gtk+3-devel >= 3.10.0
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

%package apidocs
Summary:	Mutter (Meta) API documentation
Summary(pl.UTF-8):	Dokumentacja API Mutter (Meta)
Group:		Documentation
Requires:	gtk-doc-common
Obsoletes:	mutter-wayland-apidocs < 3.14
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description apidocs
Mutter (Meta) API documentation.

%description apidocs -l pl.UTF-8
Dokumentacja API Mutter (Meta).

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
	--enable-compile-warnings=maximum \
	--disable-silent-rules \
	--disable-static \
	--with-html-dir=%{_gtkdocdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

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
%doc NEWS doc/*.txt
%attr(755,root,root) %{_bindir}/mutter
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
%attr(755,root,root) %{_libexecdir}/mutter-restart-helper
%{_desktopdir}/mutter.desktop
%{_desktopdir}/mutter-wayland.desktop
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
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter.so
%{_includedir}/mutter
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.gir
%{_pkgconfigdir}/libmutter.pc

%files apidocs
%defattr(644,root,root,755)
%{_gtkdocdir}/meta
