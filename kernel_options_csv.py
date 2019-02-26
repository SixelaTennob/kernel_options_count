#!/usr/bin/python3

import wget
import tarfile

CSV_FILE_PATH = "/home/sixelinux/kernel_options.csv"

if __name__ == "__main__":

    fichier = open(CSV_FILE_PATH, "w")
    fichier.write("Kernel_version, nb_options\n")
    for i in range(21):
        kernel_string = "4.{}.1".format(i)
        wget_string = "http://cdn.kernel.org/pub/linux/kernel/v4.x/linux-{}.tar.xz".format(kernel_string)
        print(wget_string)
        linux_tar = wget.download(wget_string)
        with tarfile.open(linux_tar) as f:
            f.extractall('.')
        fichier.write("{}, ".format(kernel_string))
