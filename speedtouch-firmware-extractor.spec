%define debug_package %{nil}
%define name speedtouch-firmware-extractor
%define distname firmware-extractor
%define version 0.1

Summary: Speedtouch firmware extractor
Name: %{name}
Version: %{version}
Release: 14
Source0: %{distname}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.linux-usb.org/SpeedTouch/firmware/index.html
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This is a small application to prepare and install the firmware for a
SpeedTouch USB modem so that a 2.6.10 kernel (or later) can load the
firmware without the assistance of modem_run.

The firmware extractor splits the firmware file (old mgmt.o) in
smaller firmware files (stage1 and stage2) that are meant to be used
with hotplug firmware loading.

%prep
%setup -q -n %{distname}

%build
gcc -o %{distname} firmware.c

%install
rm -rf $RPM_BUILD_ROOT
install -D -m755 %{distname} $RPM_BUILD_ROOT%{_sbindir}/%{distname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/%{distname}


%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 0.1-8mdv2011.0
+ Revision: 670007
- mass rebuild

* Fri Dec 03 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-7mdv2011.0
+ Revision: 607554
- rebuild

* Wed Mar 17 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1-6mdv2010.1
+ Revision: 524118
- rebuilt for 2010.1

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 0.1-5mdv2010.0
+ Revision: 427206
- rebuild

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 0.1-4mdv2009.0
+ Revision: 225470
- rebuild

* Wed Mar 05 2008 Oden Eriksson <oeriksson@mandriva.com> 0.1-3mdv2008.1
+ Revision: 179516
- rebuild

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Thu Jun 14 2007 Adam Williamson <awilliamson@mandriva.org> 0.1-2mdv2008.0
+ Revision: 39260
- rebuild for new era
- Import speedtouch-firmware-extractor



* Mon May 15 2006 Olivier Blin <oblin@mandriva.com> 0.1-1mdk
- initial Mandriva release
