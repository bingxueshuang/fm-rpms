%define	pkgname	zellij
%define version 0.42.2
%define	summary A terminal workspace with batteries included
%define license MIT
%define urlpath https://zellij.dev

Name:		%{pkgname}
Version:	%{version}
Release:	%autorelease
Summary:	%{summary}
ExclusiveArch:	x86_64
License:	%{license}
URL:		%{urlpath}

BuildRequires:	curl

%description
This package contains a repackaged version of %{name}, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.

%prep
pushd %{_builddir}
curl -L https://github.com/zellij-org/zellij/releases/download/v%{version}/zellij-%{_arch}-unknown-linux-musl.tar.gz | tar -xzf-
popd

%build
# Nothing to do!

%install
PKG_BUILD="%{_builddir}"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
install -d $PKG_BIN
install -m 755 "$PKG_BUILD/$PKG_NAME" "$PKG_BIN/$PKG_NAME"

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} --help failed"
	exit $status
fi

%files
%{_bindir}/%{name}

%changelog
%autochangelog
