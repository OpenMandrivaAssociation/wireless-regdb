%define _verdate 2013.01.11
%define _version %(echo %_verdate | sed 's/\\.//g')

Name:		wireless-regdb
Version:	%{_version}
Release:	1
Summary:	The wireless regulatory database
License:	ISC
Group:		System/Configuration/Hardware
URL:		http://linuxwireless.org/en/developers/Regulatory#Theregulatorydatabase
Source0:	http://wireless.kernel.org/download/wireless-regdb/wireless-regdb-%{_verdate}.tar.bz2
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



%changelog
* Fri May 06 2011 Oden Eriksson <oeriksson@mandriva.com> 20101124-2mdv2011.0
+ Revision: 670809
- mass rebuild

* Fri Nov 26 2010 Thomas Backlund <tmb@mandriva.org> 20101124-1mdv2011.0
+ Revision: 601466
- update to 2010-11-24 database

* Tue Nov 23 2010 Thomas Backlund <tmb@mandriva.org> 20101122-1mdv2011.0
+ Revision: 599880
- update to 2010-11-22 release

* Sat Mar 20 2010 Emmanuel Andry <eandry@mandriva.org> 20091125-1mdv2010.1
+ Revision: 525463
- Updated to 20091125

* Thu Nov 12 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 20091110-1mdv2010.1
+ Revision: 465442
- Updated to 20091110

* Wed Sep 09 2009 Thomas Backlund <tmb@mandriva.org> 20090908-1mdv2010.0
+ Revision: 434748
- update to 2009.09.08

* Sat Aug 29 2009 Thomas Backlund <tmb@mandriva.org> 20090817-1mdv2010.0
+ Revision: 422200
- update to 2009-08-17

* Fri Aug 07 2009 Thomas Backlund <tmb@mandriva.org> 20090805-1mdv2010.0
+ Revision: 411495
- update to 2009-08-05

* Tue Jul 14 2009 Thomas Backlund <tmb@mandriva.org> 20090417-1mdv2010.0
+ Revision: 395979
- update to 2009.04.17

* Wed Mar 18 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 20090309-1mdv2009.1
+ Revision: 357373
- Updated to 2009.03.09 release.

* Tue Feb 03 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 20090130-1mdv2009.1
+ Revision: 336871
- Updated to 2009.01.30 release.

* Wed Jan 21 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 20090115-2mdv2009.1
+ Revision: 332313
- Change rpm group to System/Configuration/Hardware
- import wireless-regdb


