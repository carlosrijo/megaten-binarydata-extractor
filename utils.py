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
        #print(cmd)
        os.system(cmd)

    @staticmethod
    def bdPatch(filename, format, baseInputDirPath, baseOutputDirPath, option="load"):
        fullInputFilePath = COMP_utils.buildPath(baseInputDirPath, filename)
        outputFileName = re.sub(r'\..*','',filename) + "." + COMP_utils.getFileExtensionFromExtractionOption(option)
        fullOutputFilePath = COMP_utils.buildPath(baseOutputDirPath, outputFileName)
        cmd = "\"{tool}\" {option} {format} \"{input}\" \"{output}\"".format(tool=comp_bdpatch_tool_path, option=option, format=format, input=fullInputFilePath, output=fullOutputFilePath)
        cmd = COMP_utils.buildMsCommand(cmd)
        #print(cmd)
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

class FlagParser(object):
    '''
    Requirements:
        Crystal, SI, Special, Soul, Tarot, Repair, CP, Multiple, Store, Discard, Sell, Bazaar, Trade
    '''
    __requirementsMasks = [
        0b0000000000001, # 1    - Can Trade
        0b0000000000010, # 2    - Can Bazaar
        0b0000000000100, # 4    - Can Sell
        0b0000000001000, # 8    - Can Discard
        0b0000000010000, # 16   - Can Store
        0b0000000100000, # 32   - Can Multiple
        0b0000001000000, # 64   - Can CP
        0b0000010000000, # 128  - Can Repair
        0b0000100000000, # 256  - Can Tarot
        0b0001000000000, # 512  - Can Soul
        0b0010000000000, # 1024 - Can Special
        0b0100000000000, # 2048 - Can SI
        0b1000000000000  # 4096 - Can Crystal
    ]

    @staticmethod
    def canTrade(flag):
        return flag & FlagParser.__requirementsMasks[0] > 0

    @staticmethod
    def canBazaar(flag):
        return flag & FlagParser.__requirementsMasks[1] > 0

    @staticmethod
    def canSell(flag):
        return flag & FlagParser.__requirementsMasks[2] > 0

    @staticmethod
    def canDiscard(flag):
        return flag & FlagParser.__requirementsMasks[3] > 0

    @staticmethod
    def canStore(flag):
        return flag & FlagParser.__requirementsMasks[4] > 0

    @staticmethod
    def canMultiple(flag):
        return flag & FlagParser.__requirementsMasks[5] > 0

    @staticmethod
    def canCp(flag):
        return flag & FlagParser.__requirementsMasks[6] > 0

    @staticmethod
    def canRepair(flag):
        return flag & FlagParser.__requirementsMasks[7] > 0

    @staticmethod
    def canTarot(flag):
        return flag & FlagParser.__requirementsMasks[8] > 0

    @staticmethod
    def canSoul(flag):
        return flag & FlagParser.__requirementsMasks[9] > 0

    @staticmethod
    def canSpecial(flag):
        return flag & FlagParser.__requirementsMasks[10] > 0

    @staticmethod
    def canSI(flag):
        return flag & FlagParser.__requirementsMasks[11] > 0

    @staticmethod
    def canCrystal(flag):
        return flag & FlagParser.__requirementsMasks[12] > 0

class PyUtils(object):

  @staticmethod
  def getValueFromNestedDictionary(key, var):
    if hasattr(var,'iteritems'):
        for k, v in var.iteritems():
            if k == key:
                yield v
            if isinstance(v, dict):
                for result in PyUtils.getValueFromNestedDictionary(key, v):
                    yield result
            elif isinstance(v, list):
                for d in v:
                    for result in PyUtils.getValueFromNestedDictionary(key, d):
                        yield result
