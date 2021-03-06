Name:		evopop-gtk-theme
Version:	2.1.2
Release:	1%{?dist}
Summary:	EvoPop GTK theme for Gnome
Group:		User Interface/Desktops

License:	GPLv3
URL:		https://github.com/solus-cold-storage/evopop-gtk-theme
Source0:	https://github.com/solus-cold-storage/%{name}/archive/%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildRequires:	automake

Requires:	gtk-murrine-engine >= 0.98.1.1
Requires:	gtk3 >= 3.18.5

BuildRequires:	git

BuildArch:	noarch

%description
EvoPop is the official GTK theme for Ozon OS.


%prep
%setup -q
chmod 644 AUTHORS README.md LICENSE

%build
autoreconf --force --install --symlink --warnings=all
%configure

%install
%{make_install}

find %{buildroot}%{_datadir}/themes/EvoPop -type f -exec chmod 644 {} \;
find %{buildroot}%{_datadir}/themes/EvoPop -type d -exec chmod 755 {} \;

%files
%defattr(-,root,root)
%doc AUTHORS README.md
%license LICENSE
%{_datadir}/themes/EvoPop

%changelog
* Tue Jun 27 2017 Arkady L. Shane <ashejn@russianfedora.ru> - 2.1.2-1
- update to 2.1.2

* Mon Jun 26 2017 Arkady L. Shane <ashejn@russianfedora.ru> - 2.1.1-1
- update to 2.1.1

* Thu Oct 27 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 2.0.4-1
- update to 2.0.4

* Mon Oct 17 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 2.0.1-1
- update to 2.0.1

* Mon Oct 17 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 2.0.0-1
- update to 2.0.0

* Tue Aug  2 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.7.3-1
- update to 1.7.3

* Wed Jul 20 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.7.2-1
- update to 1.7.2

* Mon Jul  4 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.7.0-1.R
- update to 1.7.0

* Tue Jun 28 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.6.1-1.R
- update to 1.6.1
- Fixed Raven black background.
- Improved tiled & maximized headerbars
- Gtk 3.18
  Total rewrite from Adwaita
  improved level / progressbars
  Improved scales
  Minor tweaks to Budgie theming
  Tweaked spinbuttons

* Mon Jun 20 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.5.0-1.R
- Total rewrite from Adwaita
- improved level / progressbars
- Improved scales
- Minor tweaks to Budgie theming
- Tweaked spinbuttons

* Thu Jun 16 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.4.2-1.R
- gtk 3.18/3.20 bugfix release

* Wed Jun 15 2016 Arkady L. Shane <ashejn@russianfedora.ru> - 1.4-1.R
- update to 1.4

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
