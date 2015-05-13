%global daterev	20150511gitf4cf8b

Name:		evopop-gtk-theme
Version:	0.27
Release:	0.1.%{?daterev}%{?dist}
Summary:	EvoPop GTK theme for Gnome
Group:		User Interface/Desktops

License:	GPLv3
URL:		https://github.com/solus-project
Source0:	%{name}-%{version}-%{?daterev}.tar.xz

BuildRequires:	automake

Requires:	gtk-murrine-engine >= 0.98.1.1
Requires:	gtk3 >= 3.14.0

BuildRequires:	git

BuildArch:	noarch

%description
EvoPop is the official GTK theme for Ozon OS.


%prep
%setup -q

%build
./autogen.sh

%install
%{make_install}
cp -f %{buildroot}%{_datadir}/themes/evopop-light-gtk-theme/gtk-2.0/gtkrc \
	%{buildroot}%{_datadir}/themes/evopop-gtk-theme/gtk-2.0/gtkrc


%files
%defattr(-,root,root)
%doc CREDITS README.md
%license LICENSE
%{_datadir}/themes/evopop*

%changelog
* Wed May 13 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.23-0.1.20150511gitf4cf8b.R
- update to last snapshot 20150511gitf4cf8b

* Sat Apr 11 2015 Arkady L. Shane <ashejn@russianfedora.ru> - 0.23-0.1.20150411git1af5e8.R
- initial build
