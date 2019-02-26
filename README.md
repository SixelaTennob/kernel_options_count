git clone https://github.com/ulfalizer/Kconfiglib.git

pip3 install kconfiglib

Download a Linux kernel and patch the makefile in kernel/scripts/kconfig with this command : 

patch -p1 <  Kconfiglib/makefile.patch

In the kernel folder :

make scriptconfig SCRIPT=Kanalyser2/count_options.py
