#
# Conditional build:
%bcond_with	gnome2		# build with support for GNOME2 wm-properties
#
Summary:	Window and compositing manager based on Clutter
Name:		mutter
Version:	3.0.2.1
Release:	2
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://ftp.gnome.org/pub/GNOME/sources/mutter/3.0/%{name}-%{version}.tar.bz2
# Source0-md5:	52212e032309fff6307f9083171fcb1a
URL:		http://git.gnome.org/cgit/mutter
BuildRequires:	GConf2-devel >= 1.2.0
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	cairo-devel >= 1.10
BuildRequires:	clutter-devel >= 1.6.0
BuildRequires:	gdk-pixbuf2-devel
BuildRequires:	gettext-devel
BuildRequires:	glib2-devel >= 1:2.28.0
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils >= 0.8.0
BuildRequires:	gobject-introspection-devel >= 0.10.0
BuildRequires:	gtk+3-devel >= 3.0.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk3-devel >= 0.26
BuildRequires:	libtool
BuildRequires:	pango-devel >= 1.2.0
BuildRequires:	pkgconfig
# only in configure.in
BuildRequires:	python >= 2.5
BuildRequires:	startup-notification-devel >= 0.7
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
BuildRequires:	zenity
Requires(post,preun):	GConf2
Requires:	zenity
Provides:	gnome-wm
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Mutter is a window and compositing manager that displays and manages
your desktop via OpenGL. Mutter combines a sophisticated display
engine using the Clutter toolkit with solid window-management logic
inherited from the Metacity window manager.

%package devel
Summary:	Development package for Mutter
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	clutter-devel >= 1.2.0
Requires:	gtk+3-devel >= 3.0.0

%description devel
Header files and libraries for developing Mutter plugins.

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
	--disable-schemas-install \
	--disable-silent-rules \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{!?with_gnome2:%{__rm} %{_datadir}/gnome/wm-properties/mutter-wm.desktop}

%{__rm} $RPM_BUILD_ROOT%{_libdir}/*.la

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%gconf_schema_install mutter.schemas
/sbin/ldconfig

%preun
%gconf_schema_uninstall mutter.schemas

%postun -p /sbin/ldconfig

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README AUTHORS NEWS HACKING doc/theme-format.txt rationales.txt
%attr(755,root,root) %{_bindir}/mutter
%attr(755,root,root) %{_bindir}/mutter-message
%attr(755,root,root) %{_bindir}/mutter-theme-viewer
%attr(755,root,root) %{_bindir}/mutter-window-demo
%attr(755,root,root) %{_libdir}/libmutter.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libmutter.so.0
%dir %{_libdir}/mutter
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.typelib
%{_desktopdir}/mutter.desktop
%{?with_gnome2:%{_datadir}/gnome/wm-properties/mutter-wm.desktop}
%{_sysconfdir}/gconf/schemas/mutter.schemas
%{_datadir}/mutter
%{_mandir}/man1/mutter.1*
%{_mandir}/man1/mutter-message.1*
%{_mandir}/man1/mutter-theme-viewer.1*
%{_mandir}/man1/mutter-window-demo.1*

%files devel
%defattr(644,root,root,755)
%{_includedir}/mutter
%attr(755,root,root) %{_libdir}/libmutter.so
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.gir
%{_pkgconfigdir}/libmutter.pc
%{_pkgconfigdir}/mutter-plugins.pc
