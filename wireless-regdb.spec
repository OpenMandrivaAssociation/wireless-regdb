Name:		wireless-regdb
Version:	2019.06.03
Release:	1
Summary:	The wireless regulatory database
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory#Theregulatorydatabase
Source0:	https://mirrors.edge.kernel.org/pub/software/network/wireless-regdb/wireless-regdb-%{version}.tar.xz
BuildArch:	noarch

%description
Database with wireless regulatory information, used by crda or which can
be used by another user space helpers to communicate wireless regulatory
data to linux kernel.

%prep
%autosetup -p1

%build

%install
%make_install

%files
%defattr(0644,root,root,0755)
%doc LICENSE
%{_mandir}/man5/regulatory.*.5*
%{_prefix}/lib/crda/regulatory.bin
%{_prefix}/lib/crda/pubkeys/*.key.pub.pem
/lib/firmware/regulatory.db*
