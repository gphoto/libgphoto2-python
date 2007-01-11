AC_PREREQ(2.59)
AC_INIT([libgphoto2 python bindings], [2.3.1.3.trunk], [gphoto-devel@lists.sourceforge.net], [libgphoto2-python])
AC_CONFIG_SRCDIR([gphoto2.pyx])
dnl AC_CONFIG_MACRO_DIR([auto-m4])
AC_CONFIG_AUX_DIR([auto-aux])
AM_INIT_AUTOMAKE([-Wall -Werror gnu 1.9 dist-bzip2 check-news])

GP_CHECK_SHELL_ENVIRONMENT
GP_REFERENCES

GP_PYTHON
GP_CHECK_LIBRARY([LIBGPHOTO2], [libgphoto2], [>= 2.3.1.3.trunk])

AC_ARG_VAR([PYREXC], [Pyrex compiler])
if test "x$PYREXC" = "x"; then
   AC_PATH_PROG([PYREXC],[pyrexc])
fi
AC_SUBST([PYREXC])


AC_CONFIG_FILES([
Makefile
m4m/Makefile
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
