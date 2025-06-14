%define	pkgname	eza
%define version 0.21.4
%define	summary A modern alternative to ls.
%define license MIT AND EUPL-1.2 AND CC-BY-4.0
%define urlpath https://eza.rocks/

Name:		%{pkgname}
Version:	%{version}
Release:	%autorelease
Summary:	%{summary}
ExclusiveArch:	x86_64
License:	%{license}
URL:		%{urlpath}

BuildRequires:	curl

%description
This package contains a repackaged version of ${name}, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.

%prep
PKG_GHDL="https://github.com/eza-community/eza/releases/download/v%{version}"
pushd %{_builddir}
curl -L "$PKG_GHDL/%{name}_%{_arch}-unknown-linux-gnu.tar.gz" | tar -xzf-
curl -L "$PKG_GHDL/completions-%{version}.tar.gz" | tar -xzf-
curl -L "$PKG_GHDL/man-%{version}.tar.gz" | tar -xzf-
popd

%build
# Nothing to do!

%define bashdir %{_datadir}/bash-completion/completions
%define fishdir %{_datadir}/fish/vendor_completions.d
%define zshdir	%{_datadir}/zsh/site-functions
%define mandir	%{_datadir}/man/man1
%define man5dir %{_datadir}/man/man5

%install
PKG_BUILD="%{_builddir}"
PKG_NAME="%{name}"
PKG_VERSION="%{version}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_BASH="%{buildroot}%{bashdir}"
PKG_FISH="%{buildroot}%{fishdir}"
PKG_ZSH="%{buildroot}%{zshdir}"
PKG_MAN="%{buildroot}%{mandir}"
PKG_MAN5="%{buildroot}%{man5dir}"
PKG_COMPLETIONS="$PKG_BUILD/target/completions-$PKG_VERSION"
PKG_TARGET_MAN="$PKG_BUILD/target/man-$PKG_VERSION"
install -d $PKG_BIN $PKG_BASH $PKG_FISH $PKG_ZSH $PKG_MAN $PKG_MAN5
install -m 755 -t "$PKG_BIN" "$PKG_BUILD/$PKG_NAME"
install -m 644 -t "$PKG_BASH" "$PKG_COMPLETIONS/$PKG_NAME"
install -m 644 -t "$PKG_FISH" "$PKG_COMPLETIONS/$PKG_NAME.fish"
install -m 644 -t "$PKG_ZSH" "$PKG_COMPLETIONS/_$PKG_NAME"
install -m 644 -t "$PKG_MAN" "$PKG_TARGET_MAN/$PKG_NAME.1"
install -m 644 -t "$PKG_MAN5" $PKG_TARGET_MAN/*.5

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} --help failed"
	exit $status
fi

%files
%{_bindir}/%{name}
%{_datadir}/bash-completion/completions/%{name}
%{_datadir}/fish/vendor_completions.d/%{name}.fish
%{_datadir}/man/man1/%{name}.1.gz
%{_datadir}/man/man5/%{name}_colors-explanation.5.gz
%{_datadir}/man/man5/%{name}_colors.5.gz
%{_datadir}/zsh/site-functions/_%{name}

%changelog
%autochangelog
