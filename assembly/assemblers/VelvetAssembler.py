#..!/usr/bin/env python

__author__ = "Joris van Steenbrugge"
__date__ = "November 2016"
__email__ = "joris.vansteenbrugge@wur.nl"

import subprocess as sp

class VelvetAssembler(object):
    """Object to execute a de novo assembly using Velvet"""

    def __init__(self, workdir):
        """Sets some local variables concerning directories
        
        Keyword arguments:
            workdir -- 
        """
        self.workdir = workdir
        self.contigFile = self.workdir + "/contigs.fa"
        self.logdir = self.workdir+ "/log/"

    def assemble(self, readType, readFiles, ksize,
                 fileFormat = "fastq",):

        self.inputs = "-short"
        if len(readFiles) > 1:
            if readType == "paired":
                self.inputs += "Paired"
                self.inputs = "-separate {}".format(self.inputs)
        self.inputs += " " + " ".join(readFiles)
        velveth = "velveth {0} {1} -{2} {3} > {4}/velvet.log 2> {4}/velvet.err".format(self.workdir,
                                                ksize,
                                                fileFormat,
                                                self.inputs,
                                                self.logdir)
        print(velveth)
        velvetg = "velvetg {}".format(self.workdir)
        


        sp.call(velveth, shell = True)
        sp.call(velvetg, shell = True)

    def getContigFile(self):
        return self.contigFile
