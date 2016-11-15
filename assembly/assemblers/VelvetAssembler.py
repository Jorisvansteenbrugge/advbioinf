#..!/usr/bin/env python

import subprocess as sp

class VelvetAssembler(object):

    def __init__(self, workdir):
        self.workdir = workdir
        self.contigFile = self.workdir + "/contigs.fa"


    def assemble(self, readType, readFiles, fileFormat = "fastq",
                                            hash_length = 31):

        self.inputs = "-short"
        if len(readFiles) > 1:
            if readType == "paired":
                self.inputs += "Paired"
                self.inputs = "-separate {}".format(self.inputs)
        self.inputs += " " + " ".join(readFiles)
        velveth = "velveth {} {} -{} {} ".format(self.workdir,
                                                hash_length,
                                                fileFormat,
                                                self.inputs)
        velvetg = "velvetg {}".format(self.workdir)
        


        sp.call(velveth, shell = True)
        sp.call(velvetg, shell = True)

    def getContigFile(self):
        return self.contigFile
