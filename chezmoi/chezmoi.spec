Name:		chezmoi
Version:	2.62.6
Release:	2%{?dist}
Summary:	Manage your dotfiles across multiple diverse machines, securely.
ExclusiveArch:	x86_64

License:	MIT
URL:		https://www.chezmoi.io
Source0:	https://github.com/twpayne/chezmoi/releases/download/v%{version}/chezmoi-%{version}-%{_arch}.rpm

BuildRequires:	rpm-build
Requires:	git

%description
This package contains a repackaged version of chezmoi, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.


%prep
mkdir -p %{_builddir}/%{name}-%{version}
cd %{_builddir}/%{name}-%{version}
rpm2cpio ${SOURCE0} | cpio -idmv
rpmextract -v %{SOURCE0}

%build
# Nothing to do

%install
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/usr/share
cp -a ./* %{buildroot}/

%check
%{buildroot}%{_bindir}/chezmoi --help > /dev/null 2>&1
if [$? -ne 0]; then
	echo "ERROR: chezmoi --help failed"
	exit 1
fi

%files
/usr/bin/chezmoi
/usr/share/bash-completion/completions/chezmoi
/usr/share/fish/vendor_completions.d/chezmoi.fish
/usr/share/zsh/site-functions/_chezmoi

%changelog
* Fri Jun 13 2025 Manojna - 2.62.6-2
- Re-package chezmoi from upstream.
