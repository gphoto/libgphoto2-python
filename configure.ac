AC_PREREQ(2.59)
AC_INIT([libgphoto2 python bindings], [2.3.1.4.trunk], [gphoto-devel@lists.sourceforge.net], [libgphoto2-python])
AC_CONFIG_SRCDIR([gphoto2.pyx])
AC_CONFIG_MACRO_DIR([m4])
AC_CONFIG_AUX_DIR([auto-aux])
dnl Note: Our *_PYTHON variable usage requires at least automake 1.8
AM_INIT_AUTOMAKE([-Wall -Werror gnu 1.9 dist-bzip2 check-news])

m4_ifdef([AM_PROG_AR], [AM_PROG_AR])
AM_PROG_LIBTOOL

dnl FIXME: What are our real Python version requirements?
AM_PATH_PYTHON([2.2],, [:])
AM_CONDITIONAL([HAVE_PYTHON], [ test "$PYTHON" != ":" ])
dnl FIXME: Shouldn't this include dir for Python.h be defined by AM_PATH_PYTHON?
AC_SUBST([GP_PYTHON_CPPFLAGS], ["-I/usr/include/python\$(PYTHON_VERSION)"])

GP_CHECK_SHELL_ENVIRONMENT
GP_REFERENCES

GP_CHECK_LIBRARY([LIBGPHOTO2], [libgphoto2], [>= 2.3.1])

dnl FIXME: Check that pyrexc actually works.
AC_ARG_VAR([PYREXC], [Pyrex compiler])
if test "x$PYREXC" = "x"; then
   AC_PATH_PROG([PYREXC],[pyrexc])
fi
AC_SUBST([PYREXC])
AC_MSG_CHECKING([for pyrexc executable])
AC_MSG_RESULT([${PYREXC}])
if test "x$PYREXC" = "x"; then
   AC_MSG_ERROR([Fatal: pyrexc not found.

Get Pyrex from
  * your system's packages (recommended)
  * upstream at http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/
])
fi
AM_CONDITIONAL([HAVE_PYREXC], [test "x$PYREXC" != "x"])


AC_CONFIG_FILES([
Makefile
gphoto-m4/Makefile
gp-setup.py
setup.py
],[
dnl This relies on this code being called for each of the above files
dnl with ac_file set to the filename.
	if echo "$ac_file" | grep '.py$' > /dev/null; then
		if test -f "$ac_file"; then
			chmod +x "$ac_file"
		fi
	fi
])
AC_OUTPUT
