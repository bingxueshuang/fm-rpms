%define	pkgname	miniserve
%define version 0.29.0
%define	summary 🌟 For when you really just want to serve some files over HTTP right now!
%define license MIT
%define urlpath https://github.com/svenstaro/miniserve

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
pushd %{_builddir}
curl -L -o %{name} https://github.com/svenstaro/miniserve/releases/download/v%{version}/miniserve-%{version}-%{_arch}-unknown-linux-gnu
popd

%build
pushd %{_builddir}
chmod +x %{name}
./%{name} --print-completions bash > completions.bash
./%{name} --print-completions fish > completions.fish
./%{name} --print-completions zsh > completions.zsh
./%{name} --print-manpage > manpage.1
popd

%define bashdir %{_datadir}/bash-completion/completions
%define fishdir %{_datadir}/fish/vendor_completions.d
%define zshdir	%{_datadir}/zsh/site-functions
%define mandir	%{_datadir}/man/man1

%install
PKG_BUILD="%{_builddir}"
PKG_NAME="%{name}"
PKG_BIN="%{buildroot}%{_bindir}"
PKG_BASH="%{buildroot}%{bashdir}"
PKG_FISH="%{buildroot}%{fishdir}"
PKG_ZSH="%{buildroot}%{zshdir}"
PKG_MAN="%{buildroot}%{mandir}"
install -d $PKG_BIN $PKG_BASH $PKG_FISH $PKG_ZSH $PKG_MAN
install -m 755 "$PKG_BUILD/$PKG_NAME" "$PKG_BIN/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.bash" "$PKG_BASH/$PKG_NAME"
install -m 644 "$PKG_BUILD/completions.fish" "$PKG_FISH/$PKG_NAME.fish"
install -m 644 "$PKG_BUILD/completions.zsh" "$PKG_ZSH/_$PKG_NAME"
install -m 644 "$PKG_BUILD/manpage.1" "$PKG_MAN/$PKG_NAME.1"

%check
# Nothing to do!

%files
%{_bindir}/%{name}
%{bashdir}/%{name}
%{fishdir}/%{name}.fish
%{zshdir}/_%{name}
# GOTCHA: rpm auto-gzip man pages before this section
%{mandir}/%{name}.1.gz

%changelog
%autochangelog
