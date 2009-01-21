%define _verdate 2009-01-15
%define _version %(echo %_verdate | sed 's/-//g')

Name:		wireless-regdb
Version:	%{_version}
Release:	%mkrel 1
Summary:	The wireless regulatory database
License:	ISC
Group:		System/Kernel and hardware
URL:		http://linuxwireless.org/en/developers/Regulatory#Theregulatorydatabase
Source:		http://wireless.kernel.org/download/wireless-regdb/wireless-regdb-%{_verdate}.tar.bz2
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Database with wireless regulatory information, used by crda or which can
be used by another user space helpers to communicate wireless regulatory
data to linux kernel.

%prep
%setup -q -n %{name}-%{_verdate}

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_prefix}/lib/crda
cp regulatory.bin %{buildroot}%{_prefix}/lib/crda

%files
%defattr(0644,root,root,0644)
%doc LICENSE
%{_prefix}/lib/crda/regulatory.bin
