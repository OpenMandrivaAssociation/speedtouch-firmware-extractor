%define name speedtouch-firmware-extractor
%define distname firmware-extractor
%define version 0.1
%define release %mkrel 2

Summary: Speedtouch firmware extractor
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{distname}.tar.bz2
License: GPL
Group: System/Kernel and hardware
Url: http://www.linux-usb.org/SpeedTouch/firmware/index.html

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
