Summary:	Window and compositing manager based on Clutter
Name:		mutter
Version:	2.28.0
Release:	1
License:	GPL v2+
Group:		X11/Window Managers
URL:		http://git.gnome.org/cgit/mutter
Source0:	http://download.gnome.org/sources/mutter/2.28/%{name}-%{version}.tar.bz2
# Source0-md5:	3926895782024cff7af7ca480df46b4f
BuildRequires:	GConf2-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	clutter-devel >= 1.0.0
BuildRequires:	desktop-file-utils
BuildRequires:	gettext
BuildRequires:	gir-repository-devel
BuildRequires:	gnome-common
BuildRequires:	gnome-doc-utils
BuildRequires:	gobject-introspection-devel
BuildRequires:	gtk+2-devel
BuildRequires:	intltool
BuildRequires:	libtool
BuildRequires:	pango-devel
BuildRequires:	pkgconfig
BuildRequires:	startup-notification-devel
BuildRequires:	xorg-lib-libX11-devel
BuildRequires:	xorg-lib-libXcursor-devel
BuildRequires:	xorg-lib-libXdamage-devel
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXrandr-devel
BuildRequires:	xorg-lib-libXrender-devel
BuildRequires:	zenity
Requires:	GConf2
Requires:	dbus
Requires:	startup-notification
Requires:	zenity
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A window manager based on metacity and clutter

%package devel
Summary:	Development package for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	gtk-doc
Requires:	pkgconfig

%description devel
Files for development with %{name}.

%prep
%setup -q
rm po/ca@valencia.po
rm po/la.po
sed -i 's/^ca@valencia$//;s/^la$//' po/LINGUAS

%build
%{__intltoolize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--disable-schemas-install \
	--disable-static
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_datadir}/gir-1.0,%{_libdir}/girepository-1.0}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT/%{_libdir}/*.la
mv $RPM_BUILD_ROOT%{_libdir}/mutter/*.gir $RPM_BUILD_ROOT%{_datadir}/gir-1.0
mv $RPM_BUILD_ROOT%{_libdir}/mutter/*.typelib $RPM_BUILD_ROOT%{_libdir}/girepository-1.0

%find_lang %{name} --with-gnome --all-name

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
%doc README AUTHORS COPYING NEWS HACKING doc/theme-format.txt rationales.txt
%{_mandir}/man1/mutter.1*
%{_mandir}/man1/mutter-message.1*
%attr(755,root,root) %{_bindir}/mutter
%attr(755,root,root) %{_bindir}/mutter-message
%{_desktopdir}/*.desktop
%{_datadir}/gnome/wm-properties/mutter-wm.desktop
%{_sysconfdir}/gconf/schemas/mutter.schemas
%{_datadir}/mutter
%attr(755,root,root) %{_libdir}/libmutter-private.so.*.*
%attr(755,root,root) %ghost %{_libdir}/libmutter-private.so.0
%dir %{_libdir}/mutter
%dir %{_libdir}/mutter/plugins
%attr(755,root,root) %{_libdir}/mutter/plugins/default.so
%{_libdir}/girepository-1.0/*.typelib

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/mutter-theme-viewer
%attr(755,root,root) %{_bindir}/mutter-window-demo
%{_includedir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%{_pkgconfigdir}/*
%{_mandir}/man1/mutter-theme-viewer.1*
%{_mandir}/man1/mutter-window-demo.1*
%{_datadir}/gir-1.0/*.gir
