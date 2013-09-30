SUBDIRS = gphoto-m4

ACLOCAL_AMFLAGS = -I m4 -I gphoto-m4

EXTRA_DIST = \
	gp-setup.py.in \
	setup.py.in setup.py \
	gphoto2.pyx \
	gptest.py \
	test-gp.py \
	TODO

if HAVE_PYTHON

BUILT_SOURCES = gphoto2.c

pyexec_LTLIBRARIES = gphoto2.la
gphoto2_la_CPPFLAGS = $(AM_CPPFLAGS) $(GP_PYTHON_CPPFLAGS) $(CPPFLAGS)
gphoto2_la_CFLAGS = $(AM_CFLAGS) $(LIBGPHOTO2_CFLAGS) $(CPPFLAGS)
gphoto2_la_SOURCES = gphoto2.c
gphoto2_la_LDFLAGS = -avoid-version -module
gphoto2_la_LIBADD = $(LIBGPHOTO2_LIBS)

if HAVE_PYREXC
gphoto2.c: gphoto2.pyx
	$(PYREXC) \
		$(LIBGPHOTO2_CFLAGS) \
		-o $@ \
		$<
endif

clean-local:
	rm -rf test-install build
	rm -f $(BUILT_SOURCES)

INSTALL_TESTS_ENVIRONMENT = env \
	PYTHONPATH="$(DESTDIR)/$(pyexecdir)" \
	LD_LIBRARY_PATH="$(DESTDIR)/$(libdir):$(LD_LIBRARY_PATH)"

INSTALL_TESTS = test-gp.py
INSTALLCHECK_DEPS = $(PYTHON_LIB)

# Breaks "make distdir" due to automake expecting all install dirs to
# depend on $prefix :-(
# So we use those local install hooks.
# python_sitearch_DATA = test-install$(python_sitearchdir)/gphoto2.so

endif

include $(top_srcdir)/installcheck.mk
