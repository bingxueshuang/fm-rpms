%define	pkgname	usql
%define version 0.19.24
%define	summary Universal command-line interface for SQL databases
%define license MIT
%define urlpath https://github.com/xo/usql

Name:		%{pkgname}
Version:	%{version}
Release:	%autorelease
Summary:	%{summary}
ExclusiveArch:	x86_64
License:	%{license}
URL:		%{urlpath}

BuildRequires:	curl bzip2

%description
This package contains a repackaged version of %{name}, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.

%prep
pushd %{_builddir}
curl -L https://github.com/xo/usql/releases/download/v%{version}/usql-%{version}-linux-amd64.tar.bz2 | tar -xjf-
popd

%build
pushd %{_builddir}
./%{name} completion bash > completions.bash
./%{name} completion fish > completions.fish
./%{name} completion zsh > completions.zsh
popd

%define bashdir %{_datadir}/bash-completion/completions
%define fishdir %{_datadir}/fish/vendor_completions.d
%define zshdir	%{_datadir}/zsh/site-functions
%define licdir  %{_datadir}/licenses/usql

%install
PKG_BUILD="%{_builddir}"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_BASH="%{buildroot}%{bashdir}"
PKG_FISH="%{buildroot}%{fishdir}"
PKG_ZSH="%{buildroot}%{zshdir}"
PKG_LIC="%{buildroot}%{licdir}"
install -d $PKG_BIN $PKG_BASH $PKG_FISH $PKG_ZSH $PKG_LIC
install -m 755 "$PKG_BUILD/$PKG_NAME" "$PKG_BIN/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.bash" "$PKG_BASH/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.fish" "$PKG_FISH/$PKG_NAME.fish"
install -m 644 "$PKG_BUILD/completions.zsh" "$PKG_ZSH/_$PKG_NAME"
install -m 644 "$PKG_BUILD/LICENSE" "$PKG_LIC/LICENSE"

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} -help failed"
	exit $status
fi

%files
%{_bindir}/%{name}
%{bashdir}/%{name}
%{fishdir}/%{name}.fish
%{zshdir}/_%{name}
%{licdir}/LICENSE

%changelog
%autochangelog
