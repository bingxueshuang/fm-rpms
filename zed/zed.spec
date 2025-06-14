%define	pkgname	zed
%define version 0.190.6
%define	summary Code at the speed of thought – Zed is a high-performance, multiplayer code editor from the creators of Atom and Tree-sitter.
%define license AGPL-3.0-only AND Apache-2.0 AND GPL-3.0-only
%define urlpath https://zed.dev

Name:		%{pkgname}
Version:	%{version}
Release:	%autorelease
Summary:	%{summary}
ExclusiveArch:	x86_64
License:	%{license}
URL:		%{urlpath}

BuildRequires:	curl
Requires:	desktop-file-utils

%description
This package contains a repackaged version of %{name}, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.

%prep
pushd %{_builddir}
curl -L https://github.com/zed-industries/zed/releases/download/v%{version}/zed-linux-%{_arch}.tar.gz | tar -xzf-
popd

%build
# Nothing to do!

%define docdir %{_datadir}/doc/%{name}

%install
PKG_BUILD="%{_builddir}/zed.app"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_LIB="%{buildroot}%{_libdir}"
PKG_LIBEXEC="%{buildroot}%{_libexecdir}"
PKG_APPS="%{buildroot}%{_datadir}/applications"
PKG_ICONS="%{buildroot}%{_datadir}/icons"
PKG_DOCS="%{buildroot}%{docdir}"
install -d $PKG_BIN $PKG_LIB $PKG_LIBEXEC $PKG_APPS $PKG_DOCS $PKG_ICONS
install -m 755 -t "$PKG_BIN" $PKG_BUILD/bin/*
install -m 755 -t "$PKG_LIBEXEC" $PKG_BUILD/libexec/*
install -m 644 -t "$PKG_LIB" $PKG_BUILD/lib/*
install -m 644 -t "$PKG_APPS" $PKG_BUILD/share/applications/*
install -m 644 -t "$PKG_DOCS" $PKG_BUILD/licenses.md
cp -a $PKG_BUILD/share/icons/* $PKG_ICONS

%post
# Update desktop database so the application shows up in menus
desktop-file-install %{_datadir}/applications/%{name}.desktop || :
# Update icon cache
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
	gtk-update-icon-cache %{_datadir}/icons/hicolor || :
fi

%postun
# Clean up desktop database entry on uninstall
desktop-file-install %{_datadir}/applications/%{name}.desktop --remove || :
# Update icon cache on uninstall
if command -v gtk-update-icon-cache >/dev/null 2>&1; then
	gtk-update-icon-cache %{_datadir}/icons/hicolor || :
fi

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} --help failed"
	exit $status
fi

%files
%{_bindir}/zed
%{_libexecdir}/zed-editor
%{_libdir}/libbsd.so.0
%{_libdir}/libxkbcommon-x11.so.0
%{_libdir}/libX11.so.6
%{_libdir}/libX11-xcb.so.1
%{_libdir}/libutil.so.1
%{_libdir}/libxcb-xkb.so.1
%{_libdir}/libz.so.1
%{_libdir}/libxkbcommon.so.0
%{_libdir}/libXau.so.6
%{_libdir}/libXdmcp.so.6
%{_libdir}/libxcb.so.1
%{_datadir}/applications/zed.desktop
%{docdir}/licenses.md
%{_datadir}/icons/hicolor/512x512/apps/zed.png
%{_datadir}/icons/hicolor/1024x1024/apps/zed.png

%changelog
%autochangelog
