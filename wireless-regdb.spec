%global         _firmwarepath    /lib/firmware

Name:           wireless-regdb
Version:        2019.06.03
Release:        2
Summary:        Regulatory database for 802.11 wireless networking

License:        ISC
URL:            https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
BuildArch:      noarch

Requires:       udev, iw
Requires:       systemd

BuildRequires:  pkgconfig(systemd)

Provides:       crda = 3.18_2019.03.01-3
Obsoletes:      crda <= 3.18_2019.03.01-2
Obsoletes: 	%{name} = 20190301-1

Source0:        http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-%{version}.tar.xz
Source1:        setregdomain
Source2:        setregdomain.1
Source3:        85-regulatory.rules


%description
The wireless-regdb package provides the regulatory rules database
used by the kernels 802.11 networking stack in order to comply 
with radio frequency regulatory rules around the world.


%prep
%setup -q


%build
: # Package installs a firmware-like, prebuilt binary from upstream...


%install
make install DESTDIR=%{buildroot} MANDIR=%{_mandir} \
	FIRMWARE_PATH=%{_firmwarepath}

install -D -pm 0755 %SOURCE1 %{buildroot}%{_sbindir}/setregdomain
install -D -pm 0644 %SOURCE2 %{buildroot}%{_mandir}/man1/setregdomain.1
install -D -pm 0644 %SOURCE3 %{buildroot}%{_udevrulesdir}/85-regulatory.rules

rm -rf %{buildroot}/usr/lib/crda


%files
%{_sbindir}/setregdomain
%{_udevrulesdir}/85-regulatory.rules
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s
%{_mandir}/man1/setregdomain.1*
%{_mandir}/man5/regulatory.db.5*
%{_mandir}/man5/regulatory.bin.5*
%license LICENSE
%doc README
