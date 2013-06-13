Name:           linux-firmware
Version:        20121007
Release:        1
Summary:        Firmware for various devices

License:        Redistributable, no modification permitted
Url:            ftp://ftp.kernel.org//pub/linux/kernel/people/dwmw2/firmware/
Group:          System/Kernel
Source0:        ftp://ftp.kernel.org//pub/linux/kernel/people/dwmw2/firmware/linux-firmware-%{version}.tar.bz2
BuildRequires:  fdupes
BuildArch:      noarch

%description
This package contains the firmware required by various devices

%package ivi
Summary:	Firmware files for Tizen IVI platform drivers

%description ivi
Firmware files for Tizen IVI platform drivers

%prep
%setup -q
find . -type f -exec chmod 0644 {} ';'

%build
# Nothing to build


%install
mkdir -p %{buildroot}/lib/firmware
cp -a * %{buildroot}/lib/firmware/

%fdupes %{buildroot}/lib/firmware

%files
%defattr(-,root,root,-)
/lib/firmware/*

%files ivi
# NOTE: make sure all the firmware we use in this RPM is documented in
# the 'ivi-firmware.txt' file.
/lib/firmware/iwlwifi-6000g2b-6.ucode
/lib/firmware/LICENCE.iwlwifi_firmware