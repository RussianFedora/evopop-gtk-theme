%global daterev	20151120gitdc603c

Name:		evopop-gtk-theme
Version:	0.29
Release:	0.4.%{?daterev}%{?dist}
Summary:	EvoPop GTK theme for Gnome
Group:		User Interface/Desktops

License:	GPLv3
URL:		https://github.com/fdinardo/evopop-gtk-theme
Source0:	%{name}-%{version}-%{?daterev}.tar.xz
Patch0:		%{name}-0.29-more-padding.patch

BuildRequires:	automake

Requires:	gtk-murrine-engine >= 0.98.1.1
Requires:	gtk3 >= 3.18.5

BuildRequires:	git

BuildArch:	noarch

%description
EvoPop is the official GTK theme for Ozon OS.


%prep
%setup -q
%patch0 -p1 -b .more-padding

%build
./autogen.sh

%install
%{make_install}

rm -rf %{buildroot}%{_datadir}/themes/evopop-light-gtk-theme


%files
%defattr(-,root,root)
%doc CREDITS README.md
%license LICENSE
%{_datadir}/themes/evopop*

%changelog
* Tue Nov 24 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29 0.4.20151120gitdc603c.R
- update to last snapshot

* Tue Nov 17 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29 0.3.20151028git8d0f4d.R
- update to last snapshot
- increase padding in Nautilus

* Fri Nov 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29 0.2.20151028git248234.R
- do not use gtkrc from light theme

* Fri Oct 30 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.29 0.1.20151028git248234.R
- rebase on https://github.com/fdinardo/evopop-gtk-theme git
- drop light theme

* Wed Sep  2 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.27-0.3.20150604git9767c3.R
- adjust black theme to Chrome browser

* Wed Jul 15 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.27-0.2.20150604git9767c3.R
- update to last snapshot

* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.23-0.1.20150511gitf4cf8b.R
- update to last snapshot 20150511gitf4cf8b

* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.23-0.1.20150411git1af5e8.R
- initial build
