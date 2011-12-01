%define name speedtouch-firmware-extractor
%define distname firmware-extractor
%define version 0.1

Summary: Speedtouch firmware extractor
Name: %{name}
Version: %{version}
Release: %mkrel 8
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
rm -rf %{buildroot}
install -D -m755 %{distname} %{buildroot}%{_sbindir}/%{distname}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{_sbindir}/%{distname}
