NAME = centos-release-ceph-nautilus

ifndef DISTRO
  $(error DISTRO is undefined, set to "el7")
endif


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
	# XXX: remove hard-coded "7" here:
	cbs build core7-extras-common-$(DISTRO).centos $(SRPM) && \
	cbs tag-build core7-extras-common-testing $(NVR)

.PHONY: all build srpm
