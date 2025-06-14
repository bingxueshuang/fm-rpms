Name:		chezmoi
Version:	2.62.6
Release:	%autorelease
Summary:	Manage your dotfiles across multiple diverse machines, securely.
ExclusiveArch:	x86_64
License:	MIT
URL:		https://www.chezmoi.io
BuildRequires:	rpm-build curl
Requires:	git

%description
This package contains a repackaged version of chezmoi, downloaded directly
from its GitHub Releases page. It provides the same functionality as the
upstream distribution.

%prep
pushd %{_builddir}
curl -L -o chezmoi.rpm https://github.com/twpayne/chezmoi/releases/download/v%{version}/chezmoi-%{version}-%{_arch}.rpm
rpm2cpio ./chezmoi.rpm | cpio -idmv
popd

%build
# Nothing to do!

%install
cp -r %{_builddir}/usr %{buildroot}

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
%autochangelog
