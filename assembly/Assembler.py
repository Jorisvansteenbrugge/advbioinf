#!/usr/bin/env python

__author__ = "Joris van Steenbrugge"

from shutil import move
import subprocess as sp
import tempfile as tp
import os

class AssemblyTool(object):
    """Object to handle the assembly of reads with different tools

    Note: Currently only assembly with velvet is supported
    """
    toolIndex = {1: "Velvet",
                 2: "wgs-assembler",
                 3: "soapdenovo",
                 4: "abyss"
                 }

    def __init__(self, toolNum, readType, readFiles, outdir):
        self.tool = self.toolIndex[toolNum]
        self.readType = readType
        self.readFiles = readFiles
        self.workdir = tp.mkdtemp(suffix=self.tool)
        self.outdir = outdir
        
        #try:
        sp.call("mkdir {}".format(outdir), shell=True)
        #except FileExistsError:
         #   pass

    def getAssembleCommands(self, fileFormat="fastq"): 
        if self.tool == "Velvet":
            hash_length = 31
            self.inputs = "-short"
            if len(self.readFiles) > 1: 
                if self.readType == "paired":
                    self.inputs += "Paired"
                    self.inputs = "-separate {}".format(self.inputs) 
            self.inputs += " " + " ".join(self.readFiles)
            velveth = "velveth {} {} -{} {} ".format(self.workdir,
                                                hash_length,
                                                fileFormat,
                                                self.inputs)
            velvetg = "velvetg {}".format(self.workdir)  
            
            self.contigFile = self.workdir + "/contigs.fa"

            return [velveth, velvetg]
        elif self.tool == "soapdenovo":
            soapconfig = self.soapConfig()
            soap = "soapdenovo-63mer all -s {} -K 63 -R -o {}".format(soapconfig,
                                                                        "soapGraph")
            os.chdir(self.workdir)

            self.contigFile = self.workdir + "/soapGraph.contig"
            return [soap]
        else:
            raise NotImplementedError("The use of {} is not currently supported".format(self.tool))

    def soapConfig(self):
        soapconfig = self.workdir + "/soapconfig"
        with open("soapConfig") as inFile, open(soapconfig,"w") as outFile:
            for line in inFile:
                outFile.write(line)
            outFile.write("q1={}\n".format(self.readFiles[0]))
            outFile.write("q2={}".format(self.readFiles[1]))
        return soapconfig

    def assemble(self):
        commands = self.getAssembleCommands()
        for cmd in commands:
            print(cmd.strip())
            sp.call(cmd, shell=True)

        self.moveContigToOutdir()

    def moveContigToOutdir(self):
        sp.call("mv {} {}".format(self.contigFile, self.outdir+"/"), shell= True)
        

    def cleanUp(self):
        print(self.workdir)
#        sp.call("rm -rf {}".format(self.workdir), shell=True)

