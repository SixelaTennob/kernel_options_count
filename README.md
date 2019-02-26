patch the makefile in kernel/scripts/kconfig

patch -p1 <  Kconfiglib/makefile.patch


In the kernel folder :

make scriptconfig SCRIPT=Kanalyser2/count_options.py