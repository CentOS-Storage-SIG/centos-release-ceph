`centos-release-ceph-nautilus` provides the YUM repository file for packages of
the CentOS Storage SIG that are used with Ceph Nautilus (14.2.x).

This package needs to be built against the following targets so that the
packages land at the right tag for inclusion in CentOS Extras:

 - core7-extras-common-el7.centos (tag: core7-extras-common-candidate)


Building the package can be done like this:

    $ make srpm DISTRO=el7

    $ make build DISTRO=el7

We are working on el8 support at https://bugs.centos.org/view.php?id=17041
