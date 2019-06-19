Summary: Ceph Nautilus packages from the CentOS Storage SIG repository
Name: centos-release-ceph-nautilus
Version: 1.2
Release: 2%{?dist}
License: GPLv2
URL: http://wiki.centos.org/SpecialInterestGroup/Storage
Source0: CentOS-Ceph-Nautilus.repo

BuildArch: noarch

# $contentdir for altarch support was added with CentOS-7.5
Requires: centos-release >= 7-5.1804.el7.centos.2
# This provides the public key to verify the RPMs
Requires: centos-release-storage-common
Requires: centos-release-nfs-ganesha28

# Users can install centos-release-ceph to get the latest
Provides: centos-release-ceph = 14.0
Conflicts: centos-release-ceph < 14.0
Obsoletes: centos-release-ceph < 14.0

%description
yum configuration for Ceph Nautilus as delivered via the CentOS Storage SIG.

%install
install -D -m 644 %{SOURCE0} %{buildroot}%{_sysconfdir}/yum.repos.d/CentOS-Ceph-Nautilus.repo

%files
%config(noreplace) %{_sysconfdir}/yum.repos.d/CentOS-Ceph-Nautilus.repo

%changelog
* Wed Jun 19 2019 Giulio Fidente <gfidente@redhat.com> - 1.2-2
* Update changelog as necessary to document changes in 1.2-1

* Tue Jun 18 2019 Giulio Fidente <gfidente@redhat.com> - 1.2-1
- Add centos-release-nfs-ganesha28 to the RPM Requires

* Mon Dec 17 2018 Ken Dreyer <kdreyer@redhat.com> - 1.1-6
- Use HTTPS for buildlogs.centos.org
- Enable GPG-checking for centos-ceph-nautilus-source

* Wed Dec 05 2018 Anssi Johansson <avij@centosproject.org> - 1.1-5
- Use mirrorlist.c.o instead of mirror.c.o

* Tue Dec 04 2018 Ken Dreyer <kdreyer@redhat.com> - 1.1-4
- Fix some stray Luminous references

* Tue Dec 04 2018 Ken Dreyer <kdreyer@redhat.com> - 1.1-3
- Bumping for Nautilus

* Tue Jul 31 2018 Niels de Vos <ndevos@redhat.com> - 1.1-2
- Require centos-release that contains the $contentdir YUM variable

* Fri Jul 06 2018 Brian Stinson <brian@bstinson.com> - 1.1-1
- Update to use the $contentdir variable to point at centos for x86_64 and
  altarch for the other arches

* Wed Sep 20 2017 Giulio Fidente <gfidente@fedoraproject.org> - 1.0-1
- Initial version based on Jewel.
