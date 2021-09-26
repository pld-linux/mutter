#
# Conditional build
%bcond_with	eglstream	# Wayland EGLStream support
%bcond_without	pipewire	# remote desktop via pipewire
%bcond_with	sysprof		# build with tracing support
%bcond_with	tests		# run tests (causes infinite loop on builders)

Summary:	Window and compositing manager based on Clutter
Summary(pl.UTF-8):	Zarządca okien i składania oparty na bibliotece Clutter
Name:		mutter
Version:	41.0
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	https://download.gnome.org/sources/mutter/41/%{name}-%{version}.tar.xz
# Source0-md5:	3eb959a4c8a192b3b535ee1b63941877
Patch0:		%{name}-deps.patch
URL:		https://gitlab.gnome.org/GNOME/mutter
BuildRequires:	EGL-devel
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	Mesa-libgbm-devel >= 17.3
BuildRequires:	atk-devel >= 1:2.6
BuildRequires:	cairo-devel >= 1.10.0
BuildRequires:	cairo-gobject-devel >= 1.14.0
BuildRequires:	dbus-devel
%{?with_eglstream:BuildRequires:	egl-wayland-devel}
BuildRequires:	fribidi-devel >= 1.0.0
BuildRequires:	gdk-pixbuf2-devel >= 2.0
BuildRequires:	gettext-tools >= 0.19.6
BuildRequires:	glib2-devel >= 1:2.69.0
BuildRequires:	gnome-desktop-devel >= 3.0
BuildRequires:	gnome-settings-daemon-devel
BuildRequires:	gobject-introspection-devel >= 1.40.0
BuildRequires:	graphene-devel >= 1.10.2
BuildRequires:	gsettings-desktop-schemas-devel >= 40
BuildRequires:	gtk+3-devel >= 3.20.0
BuildRequires:	json-glib-devel >= 0.12.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libdrm-devel
BuildRequires:	libgudev-devel >= 232
BuildRequires:	libinput-devel >= 1.18.0
BuildRequires:	libwacom-devel >= 0.13
# xcb-randr, xcb-res
BuildRequires:	libxcb-devel
BuildRequires:	meson >= 0.53.0
BuildRequires:	ninja >= 1.5
BuildRequires:	pango-devel >= 1:1.46.0
%{?with_pipewire:BuildRequires:	pipewire-devel >= 0.3.21}
BuildRequires:	pkgconfig >= 1:0.21
BuildRequires:	rpmbuild(macros) >= 1.736
BuildRequires:	startup-notification-devel >= 0.7
%{?with_sysprof:BuildRequires:	sysprof-devel >= 3.37.2}
# or elogind-devel
BuildRequires:	systemd-devel >= 1:209
BuildRequires:	tar >= 1:1.22
BuildRequires:	udev-devel >= 1:228
BuildRequires:	upower-devel >= 0.99.0
BuildRequires:	wayland-devel >= 1.18
BuildRequires:	wayland-egl-devel
BuildRequires:	wayland-protocols >= 1.21
BuildRequires:	xkeyboard-config
BuildRequires:	xorg-lib-libICE-devel
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXau-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.4
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXfixes-devel >= 3
BuildRequires:	xorg-lib-libXi-devel >= 1.7.4
BuildRequires:	xorg-lib-libXinerama-devel
BuildRequires:	xorg-lib-libXrandr-devel >= 1.5.0
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	xorg-lib-libXtst-devel
BuildRequires:	xorg-lib-libxkbcommon-devel >= 0.4.3
BuildRequires:	xorg-lib-libxkbcommon-x11-devel >= 0.4.3
BuildRequires:	xorg-lib-libxkbfile-devel
BuildRequires:	xorg-xserver-Xwayland-devel >= 21.1
# /usr/bin/cvt
BuildRequires:	xorg-xserver-server-tools
BuildRequires:	xz
Requires(post,postun):	glib2 >= 1:2.69.0
Requires:	%{name}-libs = %{version}-%{release}
Requires:	gsettings-desktop-schemas >= 40
Requires:	zenity
Provides:	gnome-wm
Obsoletes:	mutter-apidocs < 3.18
Obsoletes:	mutter-wayland < 3.14
Obsoletes:	mutter-wayland-apidocs < 3.14
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		apiver		9

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
Requires:	Mesa-libgbm >= 17.3
Requires:	atk >= 1:2.6
Requires:	cairo >= 1.10.0
Requires:	cairo-gobject >= 1.14.0
Requires:	fribidi >= 1.0.0
Requires:	glib2 >= 1:2.69.0
Requires:	gnome-desktop >= 3.0
Requires:	graphene >= 1.10.2
Requires:	gtk+3 >= 3.20.0
Requires:	json-glib >= 0.12.0
Requires:	libcanberra-gtk3 >= 0.26
Requires:	libinput >= 1.18.0
Requires:	libwacom >= 0.13
Requires:	pango >= 1:1.46.0
%{?with_pipewire:Requires:	pipewire-libs >= 0.3.21}
Requires:	startup-notification >= 0.7
Requires:	libgudev >= 232
Requires:	udev-libs >= 1:228
Requires:	upower-libs >= 0.99.0
Requires:	wayland >= 1.18
Requires:	xorg-lib-libXcomposite >= 0.4
Requires:	xorg-lib-libXfixes >= 3
Requires:	xorg-lib-libXi >= 1.7.4
Requires:	xorg-lib-libXrandr >= 1.5.0
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
Requires:	EGL-devel
Requires:	Mesa-libgbm-devel >= 17.3
Requires:	cairo-devel >= 1.10.0
Requires:	cairo-gobject-devel >= 1.14.0
Requires:	gdk-pixbuf2-devel >= 2.0
Requires:	glib2-devel >= 1:2.69.0
Requires:	graphene-devel >= 1.10.2
Requires:	gtk+3-devel >= 3.20.0
Requires:	libcanberra-gtk3-devel >= 0.26
Requires:	libdrm-devel
Requires:	startup-notification-devel >= 0.7
Requires:	wayland-devel >= 1.8
Requires:	wayland-egl-devel
Requires:	xorg-lib-libX11-devel
Requires:	xorg-lib-libXau-devel
Requires:	xorg-lib-libXcomposite-devel >= 0.4
Requires:	xorg-lib-libXcursor-devel
Requires:	xorg-lib-libXdamage-devel
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXfixes-devel >= 3
Requires:	xorg-lib-libXi-devel >= 1.7.4
Requires:	xorg-lib-libXrandr-devel >= 1.5.0
Requires:	xorg-lib-libXrender-devel
Requires:	xorg-lib-libXtst-devel
Requires:	xorg-lib-libxkbcommon-devel >= 0.4.3
Obsoletes:	mutter-wayland-devel < 3.14

%description devel
Header files for developing Mutter plugins.

%description devel -l pl.UTF-8
Pliki nagłówkowe do tworzenia wtyczek zarządcy okien i składania
Mutter.

%prep
%setup -q
%patch0 -p1

%build
%meson build \
	%{?with_eglstream:-Degl_device=true} \
	%{?with_eglstream:-Dwayland_eglstream=true} \
	-Dgles2_libname=libGLESv2.so.2 \
	-Dinstalled_tests=false \
	-Dprofiler=%{__true_false sysprof} \
	%{!?with_pipewire:-Dremote_desktop=false} \
	-Dtests=%{__true_false tests} \
	-Dxwayland_path=/usr/bin/Xwayland

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

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
%dir %{_libdir}/mutter-%{apiver}/plugins
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/plugins/libdefault.so
%attr(755,root,root) %{_libexecdir}/mutter-restart-helper
/lib/udev/rules.d/61-mutter.rules
%{_desktopdir}/mutter.desktop
%{_datadir}/GConf/gsettings/mutter-schemas.convert
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.gschema.xml
%{_datadir}/glib-2.0/schemas/org.gnome.mutter.wayland.gschema.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-wayland.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-windows.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-navigation.xml
%{_datadir}/gnome-control-center/keybindings/50-mutter-system.xml
%{_mandir}/man1/mutter.1*

%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter-%{apiver}.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmutter-%{apiver}.so.0
%dir %{_libdir}/mutter-%{apiver}
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-clutter-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-clutter-%{apiver}.so.0
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-cogl-pango-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-cogl-pango-%{apiver}.so.0
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-cogl-%{apiver}.so.*.*.*
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-cogl-%{apiver}.so.0
# intentionally installed in package-private dir
%{_libdir}/mutter-%{apiver}/Cally-%{apiver}.typelib
%{_libdir}/mutter-%{apiver}/Clutter-%{apiver}.typelib
%{_libdir}/mutter-%{apiver}/Cogl-%{apiver}.typelib
%{_libdir}/mutter-%{apiver}/CoglPango-%{apiver}.typelib
%{_libdir}/mutter-%{apiver}/Meta-%{apiver}.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libmutter-%{apiver}.so
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-clutter-%{apiver}.so
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-cogl-pango-%{apiver}.so
%attr(755,root,root) %{_libdir}/mutter-%{apiver}/libmutter-cogl-%{apiver}.so
%{_includedir}/mutter-%{apiver}
# intentionally installed in package-private dir
%{_libdir}/mutter-%{apiver}/Cally-%{apiver}.gir
%{_libdir}/mutter-%{apiver}/Clutter-%{apiver}.gir
%{_libdir}/mutter-%{apiver}/Cogl-%{apiver}.gir
%{_libdir}/mutter-%{apiver}/CoglPango-%{apiver}.gir
%{_libdir}/mutter-%{apiver}/Meta-%{apiver}.gir
%{_pkgconfigdir}/libmutter-%{apiver}.pc
%{_pkgconfigdir}/mutter-clutter-%{apiver}.pc
%{_pkgconfigdir}/mutter-cogl-%{apiver}.pc
%{_pkgconfigdir}/mutter-cogl-pango-%{apiver}.pc
