NAME = centos-release-ceph-nautilus

ifndef DISTRO
  $(error DISTRO is undefined, set to "el7" or "el8")
endif


OS_VERSION = $(subst el,,${DISTRO})

DIST := ".${DISTRO}.centos"

VERSION := $(shell rpmspec \
             --define "dist ${DIST}" \
             -q --srpm --qf "%{version}\n" ${NAME}.spec)

RELEASE := $(shell rpmspec \
             --define "dist ${DIST}" \
             -q --srpm --qf "%{release}\n" ${NAME}.spec)

NVR := ${NAME}-${VERSION}-${RELEASE}
SRPM := ${NVR}.src.rpm

all: srpm

srpm: $(SRPM)

$(SRPM):
	rpmbuild -bs \
		--define "_sourcedir ." --define "_srcrpmdir ." \
		--define "dist $(DIST)" \
		$(NAME).spec

build: $(SRPM)
	# el8 currently fails to build because the CBS admins have not yet set
	# up the tags and target. https://bugs.centos.org/view.php?id=17041
	echo cbs build core$(OS_VERSION)-extras-common-$(DISTRO).centos $(SRPM) && \
	echo cbs tag-build core$(OS_VERSION)-extras-common-testing $(NVR)

.PHONY: all build srpm
