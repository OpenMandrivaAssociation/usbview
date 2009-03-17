%define name 	usbview
%define version 1.0
%define release %mkrel 4

Name:		%name
Summary:	USB topology and device viewer
Version:	%version
Release:	%mkrel 10
Source:		%Url/%{name}-%{version}.tar.bz2
Source1:	%{name}-icons.tar.bz2
Source2:	usbview-1.0-man.tar.bz2
# Fix from David Paschal (http://hpoj.sf.net/): Hex numbers in
# /proc/bus/usb/devices were parsed as decimal numbers. Fixed.
Patch0:		usbview-1.0.patch.bz2
Patch1:		usbview-1.0-gtk_warning.patch.bz2
Patch2:		usbview-1.0-windows.patch.bz2
Group:		System/Kernel and hardware 
BuildRequires:	gtk+-devel
URL:		http://www.kroah.com/linux-usb/
BuildRoot:	%_tmppath/%{name}-buildroot
License:	GPL

%description
USBView is a GTK program that displays the topography of the devices that are
plugged into the USB bus on a Linux machine. It also displays information on
each of the devices. This can be useful to determine if a device is working
properly or not. 

%prep
%setup -q -a2
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

mkdir -p %buildroot/{%_iconsdir,%_mandir/man{7,8}}
for sec in 7 8; do
	install -m 644 usbview.$sec %buildroot/%_mandir/man$sec
done
bzcat %{SOURCE1}|tar xf - -C %buildroot/%{_iconsdir}

mkdir -p $RPM_BUILD_ROOT/%{_menudir}/
cat << EOF > $RPM_BUILD_ROOT/%{_menudir}/%{name}
?package(usbview): needs="X11"  \
icon="%{name}.png"  section="Configuration/Hardware"  \
title="UsbView" longtitle="USB viewer"  \
command="usbview"
EOF

%post
%{update_menus}

%postun
%{clean_menus}

%clean
rm -rf %buildroot

%files
%defattr(-,root,root,0755)
%doc AUTHORS COPYING* ChangeLog INSTALL NEWS README TODO
%_menudir/%name
%_bindir/*
%_iconsdir/*
%_mandir/*/*

