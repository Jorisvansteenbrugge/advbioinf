#!/usr/bin/env python

from assemblers.SoapAssembler import SoapAssembler
from assemblers.VelvetAssembler import VelvetAssembler
from subprocess import call

import tempfile as tp
import subprocess as sp

class BaseAssembler(object):
 
    toolIndex = {1: "Velvet",
                 2: "wgs-assembler",
                 3: "soapdenovo",
                 4: "abyss"
                 }

    def __init__(self, toolNum, readType, readFiles, outdir):
        self.tool = self.toolIndex[toolNum]
        self.readType = readType
        self.readFiles = readFiles
        self.workdir = tp.mkdtemp(prefix=self.tool)
        self.logdir = self.workdir + "/log/"
        self.outdir = outdir
        
        try:
            call("mkdir {}".format(outdir), shell = True)
            call("mkdir {}".format(self.logdir), shell = True)
        except:
            print("Output exists")
            sys.exit(1)

    def moveContigFile(self):
        call("mv {} {}".format(self.assembler.getContigFile(),
                                self.outdir+"/"+self.tool+"_contigs_kmer{}.fa".format(str(self.ksize)))
                        , shell = True)
        call("mv {}/* {}".format(self.logdir, self.logdir)
                        , shell = True)


    def assemble(self, ksize = 23 ):
        self.ksize = ksize
        self.assembler = None
        if self.tool == "Velvet":
            self.assembler = VelvetAssembler(self.workdir)
        elif self.tool == "soapdenovo":
            self.assembler = SoapAssembler(self.workdir)

        self.assembler.assemble(self.readType, self.readFiles, ksize)
        
        self.moveContigFile()

    def cleanUp(self):
        print("Removing: {}".format(self.workdir))
        call("rm -rf {}".format(self.workdir), shell = True)
