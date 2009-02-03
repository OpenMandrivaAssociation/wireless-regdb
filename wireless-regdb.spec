%define _verdate 2009.01.30
%define _version %(echo %_verdate | sed 's/\\.//g')

Name:		wireless-regdb
Version:	%{_version}
Release:	%mkrel 1
Summary:	The wireless regulatory database
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory#Theregulatorydatabase
Source:		http://wireless.kernel.org/download/wireless-regdb/wireless-regdb-%{_verdate}.tar.bz2
Patch:		wireless-regdb-2009.01.30-allow-install-without-root.patch
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Database with wireless regulatory information, used by crda or which can
be used by another user space helpers to communicate wireless regulatory
data to linux kernel.

%prep
%setup -q -n %{name}-%{_verdate}
%patch -p1 -b .allow-install-without-root

%build

%install
rm -rf %{buildroot}
%makeinstall_std

%files
%defattr(0644,root,root,0755)
%doc LICENSE
%{_mandir}/man5/regulatory.bin.5*
%{_prefix}/lib/crda/regulatory.bin
