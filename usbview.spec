Summary:	USB topology and device viewer
Name:		usbview
Version:	1.1
Release:	%mkrel 1
Group:		System/Kernel and hardware
License:	GPLv2+
URL:		http://www.kroah.com/linux-usb/
Source:		http://www.kroah.com/linux-usb//%{name}-%{version}.tar.bz2
BuildRequires:	gtk+2-devel imagemagick
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
USBView is a GTK program that displays the topography of the devices that are
plugged into the USB bus on a Linux machine. It also displays information on
each of the devices. This can be useful to determine if a device is working
properly or not.

%prep
%setup -q

%build
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

for i in 16x16 32x32 48x48; do
mkdir -p %{buildroot}%{_iconsdir}/hicolor/$i/apps
convert -resize $i %{name}_logo.xpm %{buildroot}%{_iconsdir}/hicolor/$i/apps/%{name}.png;
done

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/%{name}.desktop <<EOF
[Desktop Entry]
Name=%{name}
Comment=%{summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=GTK;System;
EOF

%if %mdkversion < 200900
%post
%{update_menus}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%clean_icon_cache hicolor
%endif

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc AUTHORS ChangeLog NEWS README TODO
%{_bindir}/*
%{_datadir}/applications/%{name}.desktop
%{_iconsdir}/*
%{_mandir}/*/*
