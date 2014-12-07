%define _verdate 2014.10.07
%define _version %(echo %_verdate | sed 's/\\.//g')

Name:		wireless-regdb
Version:	%{_version}
Release:	2
Summary:	The wireless regulatory database
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory#Theregulatorydatabase
Source0:	http://wireless.kernel.org/download/wireless-regdb/wireless-regdb-%{_verdate}.tar.xz
BuildArch:	noarch

%description
Database with wireless regulatory information, used by crda or which can
be used by another user space helpers to communicate wireless regulatory
data to linux kernel.

%prep
%setup -q -n %{name}-%{_verdate}

%build

%install
%makeinstall_std

%files
%defattr(0644,root,root,0755)
%doc LICENSE
%{_mandir}/man5/regulatory.bin.5*
%{_prefix}/lib/crda/regulatory.bin
%{_prefix}/lib/crda/pubkeys/linville.key.pub.pem

