#!/usr/bin/env python

from assemblers.VelvetAssembler import VelvetAssembler
from subprocess import call

import tempfile as tp

class BaseAssembler(object):
    
    import subprocess as sp

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
        self.outdir = outdir
        
        call("mkdir {}".format(outdir), shell = True)

    def moveContigFile(self):
        call("mv {} {}".format(self.assembler.getContigFile() , self.outdir+"/"), shell = True)


    def assemble(self):
        self.assembler = None
        if self.tool == "Velvet":
            self.assembler = VelvetAssembler(self.workdir)
        
        self.assembler.assemble(self.readType, self.readFiles)
        
        self.moveContigFile()

    def cleanUp(self):
        print("Removing: {}".format(self.workdir))
        call("rm -rf {}".format(self.workdir), shell = True)
