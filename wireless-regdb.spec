%global _firmwarepath /lib/firmware
%define oldver %(echo %version | sed 's/\\.//g')

Summary:	Regulatory database for 802.11 wireless networking
Name:		wireless-regdb
Version:	2022.04.08
Release:	1
License:	ISC
URL:		https://wireless.wiki.kernel.org/en/developers/regulatory/wireless-regdb
Source0:	http://www.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-%{version}.tar.xz
Source1:	setregdomain
Source2:	setregdomain.1
Source3:	85-regulatory.rules
BuildArch:	noarch
BuildRequires:	systemd-rpm-macros
Requires:	iw
Requires:	systemd
Provides:	crda = 3.18-7
Obsoletes:	crda < 3.18-7
Obsoletes:	crda-devel < 3.18-7
Obsoletes:	wireless-regdb < 20190301-2
Provides:	wireless-regdb = 20190301-2
Provides:	wireless-regdb = %{oldver}-%{release}
Obsoletes:	wireless-regdb < %{oldver}-%{release}

%description
The wireless-regdb package provides the regulatory rules database
used by the kernels 802.11 networking stack in order to comply 
with radio frequency regulatory rules around the world.

%prep
%autosetup -p1

%build
# Package installs a firmware-like, prebuilt binary from upstream...

%install
%make_install DESTDIR=%{buildroot} MANDIR=%{_mandir} FIRMWARE_PATH=%{_firmwarepath}

install -D -pm 0755 %{SOURCE1} %{buildroot}%{_sbindir}/setregdomain
install -D -pm 0644 %{SOURCE2} %{buildroot}%{_mandir}/man1/setregdomain.1
install -D -pm 0644 %{SOURCE3} %{buildroot}%{_udevrulesdir}/85-regulatory.rules

rm -rf %{buildroot}/usr/lib/crda

%files
%license LICENSE
%doc README
%{_sbindir}/setregdomain
%{_udevrulesdir}/85-regulatory.rules
%{_firmwarepath}/regulatory.db
%{_firmwarepath}/regulatory.db.p7s
%doc %{_mandir}/man1/setregdomain.1*
%doc %{_mandir}/man5/regulatory.db.5*
%doc %{_mandir}/man5/regulatory.bin.5*
