%global daterev	20151120gitdc603c

Name:		evopop-gtk-theme
Version:	1.4
Release:	1%{?dist}
Summary:	EvoPop GTK theme for Gnome
Group:		User Interface/Desktops

License:	GPLv3
URL:		https://github.com/fdinardo/evopop-gtk-theme
Source0:	https://github.com/solus-cold-storage/evopop-gtk-theme/archive/%{version}.tar.gz

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
./autogen.sh

%install
%{make_install}

%if 0%{?fedora} > 23
rm -rf %{buildroot}%{_datadir}/themes/EvoPop/gtk-3.0
mv %{buildroot}%{_datadir}/themes/EvoPop/gtk-3.20 \
    %{buildroot}%{_datadir}/themes/EvoPop/gtk-3.0
%endif

%if 0%{?fedora} < 24
rm -rf %{buildroot}%{_datadir}/themes/EvoPop/gtk-3.20
%endif

find %{buildroot}%{_datadir}/themes/EvoPop -type f -exec chmod 644 {} \;
find %{buildroot}%{_datadir}/themes/EvoPop -type d -exec chmod 755 {} \;

%files
%defattr(-,root,root)
%doc AUTHORS README.md
%license LICENSE
%{_datadir}/themes/EvoPop

%changelog
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
