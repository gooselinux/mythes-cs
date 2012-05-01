Name: mythes-cs
Summary: Czech thesaurus
%define upstreamid 20070926
Version: 0.%{upstreamid}
Release: 3.1%{?dist}
Source: http://ftp.services.openoffice.org/pub/OpenOffice.org/contrib/dictionaries/thes_cs_CZ_v2.zip
Group: Applications/Text
URL: http://wiki.services.openoffice.org/wiki/Dictionaries
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: python, perl
License: BSD
BuildArch: noarch

%description
Czech thesaurus.

%prep
%setup -q -c

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_cs_CZ_v2.* $RPM_BUILD_ROOT/%{_datadir}/mythes

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc th_cs_CZ_license.txt
%dir %{_datadir}/mythes
%{_datadir}/mythes/*

%changelog
* Mon Nov 30 2009 Dennis Gregorovic <dgregor@redhat.com> - 0.20070926-3.1
- Rebuilt for RHEL 6

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20070926-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20070926-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Wed Nov 28 2007 Caolan McNamara <caolanm@redhat.com> - 0.20070926-1
- initial version
