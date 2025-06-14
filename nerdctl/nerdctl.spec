%define	pkgname	nerdctl
%define version 2.1.2
%define	summary contaiNERD CTL - Docker-compatible CLI for containerd.
%define license Apache-2.0
%define urlpath https://github.com/containerd/nerdctl

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
curl -L https://github.com/containerd/nerdctl/releases/download/v%{version}/nerdctl-%{version}-linux-amd64.tar.gz | tar -xzf-
popd

%build
pushd %{_builddir}
chmod +x %{name}
./%{name} completion bash > completions.bash
./%{name} completion fish > completions.fish
./%{name} completion zsh > completions.zsh
popd

%define bashdir %{_datadir}/bash-completion/completions
%define fishdir %{_datadir}/fish/vendor_completions.d
%define zshdir	%{_datadir}/zsh/site-functions
%define execdir %{_libexecdir}/nerdctl

%install
PKG_BUILD="%{_builddir}"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_LIBEXEC="%{buildroot}%{execdir}"
PKG_BASH="%{buildroot}%{bashdir}"
PKG_FISH="%{buildroot}%{fishdir}"
PKG_ZSH="%{buildroot}%{zshdir}"
install -d $PKG_BIN $PKG_LIBEXEC $PKG_BASH $PKG_FISH $PKG_ZSH
install -m 755 -t "$PKG_BIN" "$PKG_BUILD/$PKG_NAME"
install -m 755 -t "$PKG_LIBEXEC" $PKG_BUILD/*.sh
install -m 644 "$PKG_BUILD/completions.bash" "$PKG_BASH/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.fish" "$PKG_FISH/$PKG_NAME.fish"
install -m 644 "$PKG_BUILD/completions.zsh" "$PKG_ZSH/_$PKG_NAME"

%check
%{buildroot}%{_bindir}/%{name} --help
status=$?
if [$status -ne 0]; then
	echo "error: %{name} --help failed"
fi

%files
%{_bindir}/%{name}
%{execdir}/containerd-rootless.sh
%{execdir}/containerd-rootless-setuptool.sh
%{bashdir}/%{name}
%{fishdir}/%{name}.fish
%{zshdir}/_%{name}

%changelog
%autochangelog
