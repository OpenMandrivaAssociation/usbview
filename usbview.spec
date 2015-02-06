Summary:	USB topology and device viewer
Name:		usbview
Version:	1.1
Release:	3
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


%changelog
* Wed Dec 08 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-2mdv2011.0
+ Revision: 615382
- the mass rebuild of 2010.1 packages

* Thu Dec 03 2009 Thierry Vignaud <tv@mandriva.org> 1.1-1mdv2010.1
+ Revision: 473017
- BR imagemagick

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - welcome back usbview
    - update to new version 1.1
    - bump buildrequires to gtk2
    - drop all patches
    - import usbview


* Mon Dec  19 2005 Erwan Velu <erwan@seanodes.com> 1.0-10mdk
- Rebuild

* Thu Oct  2 2003 Gwenole Beauchesne <gbeauchesne@mandrakesoft.com> 1.0-9mdk
- lib64 fixes

* Thu Jul 24 2003 Per Øyvind Karlsen <peroyvind@sintrax.net> 1.0-8mdk
- rebuild
- use %%make macro
- rm -rf $RPM_BUILD_ROOT in %%install, not %%prep

* Wed Jan 21 2003 Pablo Saratxaga <pablo@mandrakesoft.com> 1.0-7mdk
- English proofreading of menu entries (by Stew Benedicts)

* Thu Jan 02 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-6mdk
- build release

* Mon Oct 28 2002 Thierry Vignaud <tvignaud@mandrakesoft.com> 1.0-5mdk
- source 2 : add usbview.7 and usbview.8 man pages
- patch 1 : fix gtk warning when opening about and configure dialogs 
- patch 2 : make about & configure buttons looking as in other apps
- rpmlint fixes

* Mon Aug 19 2002 Till Kamppeter <till@mandrakesoft.com> 1.0-4mdk
- Applied fix from David Paschal (http://hpoj.sf.net/): Hex numbers in
  /proc/bus/usb/devices were parsed as decimal numbers.

* Sat Mar 09 2002 Yves Duret <yduret@mandrakesoft.com> 1.0-3mdk
- spec clean up: macros, s/Copyright/License, globbing
- png icons

* Wed Jul 11 2001 Stefan van der Eijk <stefan@eijk.nu> 1.0-2mdk
- BuildRequires:	gtk+-devel
- Removed BuildRequires:	XFree86-devel

* Thu Dec  7 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 1.0-1mdk
- 1.0.

* Sat Dec  2 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.0-2mdk
- Add icons.

* Sun Sep 24 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.9.0-1mdk
- 0.9.0

* Mon Aug 07 2000 Frederic Lepied <flepied@mandrakesoft.com> 0.8.1-3mdk
- automatically added BuildRequires

* Fri Jul 21 2000 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.8.1-2mdk
- BM
- more macros

* Fri Jun 30 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.1-1mdk
- macros everywhere.
- 0.8.1.

* Fri Jun 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.0-2mdk
- Add menu.

* Fri Jun 23 2000 Chmouel Boudjnah <chmouel@mandrakesoft.com> 0.8.0-1mdk
- 0.8.0.
- Clean up specs.

* Sat Mar 25 2000 Daouda Lo <daouda@mandrakesoft.com> 0.5.0-3mdk
- ready for 7.1

* Wed Dec  8 1999 Chmouel Boudjnah <chmouel@mandrakesoft.com>
- small specs tweaks.

* Tue Dec 07 1999 Lenny Cartier <lenny@mandrakesoft.com>
- new in contribs
- first specfile
