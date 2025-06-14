%define	pkgname	k3s
%define version 1.33.1
%define	summary Lightweight Kubernetes.
%define license MIT
%define urlpath https://k3s.io

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
curl -LO https://github.com/k3s-io/k3s/releases/download/v%{version}%2Bk3s1/k3s
popd

%build
pushd %{_builddir}
chmod +x %{name}
./%{name} completion bash > completions.bash
./%{name} completion zsh > completions.zsh
popd

%define bashdir %{_datadir}/bash-completion/completions
%define zshdir	%{_datadir}/zsh/site-functions

%install
PKG_BUILD="%{_builddir}"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_BASH="%{buildroot}%{bashdir}"
PKG_ZSH="%{buildroot}%{zshdir}"
install -d $PKG_BIN $PKG_BASH $PKG_ZSH
install -m 755 "$PKG_BUILD/$PKG_NAME" "$PKG_BIN/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.bash" "$PKG_BASH/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.zsh" "$PKG_ZSH/_$PKG_NAME"

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} --help failed"
	exit $status
fi

%files
%{_bindir}/%{name}
%{bashdir}/%{name}
%{zshdir}/_%{name}

%changelog
%autochangelog
