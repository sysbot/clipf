
ROOTDIR=
BINDIR=usr/bin
CONFDIR=etc
MANDIR=usr/share/man/man1

install:
	install -d $(ROOTDIR)/$(BINDIR)
	install -m 755 clipf $(ROOTDIR)/$(BINDIR)
	install -d $(ROOTDIR)/$(CONFDIR)
	install -m 644 clipf.conf $(ROOTDIR)/$(CONFDIR)
	install -d $(ROOTDIR)/$(MANDIR)
	install -m 644 man/clipf.1 $(ROOTDIR)/$(MANDIR)
