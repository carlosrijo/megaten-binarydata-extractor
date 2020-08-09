import os
import re
from config import comp_decrypt_tool_path, comp_bdpatch_tool_path
class COMP_utils(object):

    __optionExtMap = {
        "load" : "xml",
        "flatten" : "tsv"
    }

    @staticmethod
    def decryptSBIN(filename, baseInputDirPath, baseOutputDirPath):
        fullInputFilePath = COMP_utils.buildPath(baseInputDirPath, filename)
        fullOutputFilePath = COMP_utils.buildPath(baseOutputDirPath, filename.replace("sbin", "bin"))
        cmd = "\"{tool}\" \"{input}\" \"{output}\"".format(tool=comp_decrypt_tool_path, input=fullInputFilePath, output=fullOutputFilePath)
        cmd = COMP_utils.buildMsCommand(cmd)
        print(cmd)
        os.system(cmd)

    @staticmethod
    def bdPatch(filename, format, baseInputDirPath, baseOutputDirPath, option="load"):
        fullInputFilePath = COMP_utils.buildPath(baseInputDirPath, filename)
        outputFileName = re.sub(r'\..*','',filename) + "." + COMP_utils.getFileExtensionFromExtractionOption(option)
        fullOutputFilePath = COMP_utils.buildPath(baseOutputDirPath, outputFileName)
        cmd = "\"{tool}\" {option} {format} \"{input}\" \"{output}\"".format(tool=comp_bdpatch_tool_path, option=option, format=format, input=fullInputFilePath, output=fullOutputFilePath)
        cmd = COMP_utils.buildMsCommand(cmd)
        print(cmd)
        os.system(cmd)
        
    @staticmethod
    def getFileExtensionFromExtractionOption(option):
        return COMP_utils.__optionExtMap[option]

    @staticmethod
    def buildPath(baseDir, filename):
        return "{baseDir}/{filename}".format(baseDir=baseDir, filename=filename)
    
    @staticmethod
    def buildMsCommand(cmd):
        return "cmd /c \"{command}\"".format(command=cmd)