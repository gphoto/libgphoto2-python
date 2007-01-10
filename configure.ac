AC_PREREQ(2.59)
AC_INIT([libgphoto2 python bindings], [2.3.1.3.trunk], [gphoto-devel@lists.sourceforge.net], [libgphoto2-python])
AC_CONFIG_SRCDIR([gphoto2.pyx])
dnl AC_CONFIG_MACRO_DIR([auto-m4])
AC_CONFIG_AUX_DIR([auto-aux])
AM_INIT_AUTOMAKE([-Wall -Werror gnu 1.9 dist-bzip2 check-news])

GP_CHECK_SHELL_ENVIRONMENT

GP_PYTHON
GP_CHECK_LIBRARY([LIBGPHOTO2], [libgphoto2], [>= 2.3.1])


AC_CONFIG_FILES([
Makefile
m4m/Makefile
gp-setup.py
setup.py
])
AC_OUTPUT
