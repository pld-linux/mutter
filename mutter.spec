Summary:	Window and compositing manager based on Clutter
Name:		mutter
Version:	2.31.5
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
Source0:	http://download.gnome.org/sources/mutter/2.31/%{name}-%{version}.tar.bz2
# Source0-md5:	0bec58091d4a3b1df6d5d6c05a1dd7cd
URL:		http://git.gnome.org/cgit/mutter
BuildRequires:	GConf2-devel
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake
BuildRequires:	clutter-devel >= 1.2.0
BuildRequires:	gettext-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel >= 2:2.19.0
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libcanberra-gtk-devel
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel >= 0.7
BuildRequires:	xorg-lib-libSM-devel
BuildRequires:	xorg-lib-libXcomposite-devel >= 0.2
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	zenity
Requires(post,preun):	GConf2
Requires:	zenity
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
Requires:	gtk+2-devel >= 2:2.19.0

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

mv $RPM_BUILD_ROOT%{_prefix}/{lib,share}/locale

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
%{_mandir}/man1/mutter.1*
%{_mandir}/man1/mutter-message.1*
%attr(755,root,root) %{_bindir}/mutter
%attr(755,root,root) %{_bindir}/mutter-message
%attr(755,root,root) %{_libdir}/libmutter-private.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmutter-private.so.0
%dir %{_libdir}/mutter
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.typelib
%{_desktopdir}/mutter.desktop
%{_datadir}/gnome/wm-properties/mutter-wm.desktop
%{_sysconfdir}/gconf/schemas/mutter.schemas
%{_datadir}/mutter

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mutter-theme-viewer
%attr(755,root,root) %{_bindir}/mutter-window-demo
%{_includedir}/mutter
%attr(755,root,root) %{_libdir}/libmutter-private.so
%{_libdir}/libmutter-private.la
# intentionally installed in package-private dir
%{_libdir}/mutter/Meta-*.gir
%{_pkgconfigdir}/libmutter-private.pc
%{_pkgconfigdir}/mutter-plugins.pc
%{_mandir}/man1/mutter-theme-viewer.1*
%{_mandir}/man1/mutter-window-demo.1*
