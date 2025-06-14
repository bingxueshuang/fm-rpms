%define	pkgname	sd
%define version 1.0.0
%define	summary Intuitive find & replace CLI (sed alternative).
%define license MIT
%define urlpath https://github.com/chmln/sd

Name:		%{pkgname}
Version:	%{version}
Release:	%autorelease
Summary:	%{summary}
ExclusiveArch:	x86_64
License:	%{license}
URL:		%{urlpath}

BuildRequires:	curl

%description
This package contains a repackaged version of miniserve, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.

%prep
PKG_GHDL="https://github.com/chmln/sd/releases/download/v%{version}"
PKG_FULL_NAME="sd-v%{version}-%{_arch}-unknown-linux-gnu"
pushd %{_builddir}
curl -L "$PKG_GHDL/$PKG_FULL_NAME.tar.gz" | tar -xzf-
mv "$PKG_FULL_NAME" %{name}
pushd %{name}/completions
mv sd.bash sd
popd
popd

%build
# Nothing to do!

%define bashdir %{_datadir}/bash-completion/completions
%define fishdir %{_datadir}/fish/vendor_completions.d
%define zshdir	%{_datadir}/zsh/site-functions
%define mandir	%{_datadir}/man/man1
%define docdir  %{_datadir}/doc/sd
%define licdir  %{_datadir}/licenses/sd

%install
PKG_BUILD="%{_builddir}/%{name}"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_BASH="%{buildroot}%{bashdir}"
PKG_FISH="%{buildroot}%{fishdir}"
PKG_ZSH="%{buildroot}%{zshdir}"
PKG_MAN="%{buildroot}%{mandir}"
PKG_DOC="%{buildroot}%{docdir}"
PKG_LIC="%{buildroot}%{licdir}"
install -d $PKG_BIN $PKG_BASH $PKG_FISH $PKG_ZSH $PKG_MAN $PKG_DOC $PKG_LIC
install -m 755 -t "$PKG_BIN" "$PKG_BUILD/$PKG_NAME"
install -m 644 -t "$PKG_BASH" "$PKG_BUILD/completions/$PKG_NAME"
install -m 644 -t "$PKG_FISH" "$PKG_BUILD/completions/$PKG_NAME.fish"
install -m 644 -t "$PKG_ZSH" "$PKG_BUILD/completions/_$PKG_NAME"
install -m 644 -t "$PKG_MAN" "$PKG_BUILD/$PKG_NAME.1"
install -m 644 -t "$PKG_LIC" "$PKG_BUILD/LICENSE"
install -m 644 -t "$PKG_DOC" $PKG_BUILD/*.md

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} --help failed"
fi

%files
%{_bindir}/%{name}
%{bashdir}/%{name}
%{fishdir}/%{name}.fish
%{zshdir}/_%{name}
%{mandir}/%{name}.1.gz
%{licdir}/LICENSE
%{docdir}/README.md
%{docdir}/CHANGELOG.md

%changelog
%autochangelog
