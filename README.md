`centos-release-ceph-nautilus` provides the YUM repository file for packages of
the CentOS Storage SIG that are used with Ceph Nautilus (14.2.x).

This package needs to get built against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)


Building the package can be done like this:

    $ make srpm DISTRO=el7

    $ make build DISTRO=el7
