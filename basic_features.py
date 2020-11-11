import os
import json
from extractor import Extractor
from xmlparser import XmlParser
from config import base_client_binary_data_directory, base_output_directory_xml_or_tsv
from utils import COMP_utils, FlagParser, PyUtils

class BasicFeaturesManager:

  def __init__(self):
    self.inputBinaryFileName = 'ItemData.sbin'
    self.outputXmlFileName = 'ItemData.xml'
    self.outputFilePath = os.path.join(base_output_directory_xml_or_tsv, self.outputXmlFileName)
    self.basicFeaturesMap = {}

  def generateBasicFeatureXmlSchema(self, outputFilename):
    XmlParser.printXmlSchemaFromXmlFile(self.outputFilePath, outputFilename)

  def getBasicFeaturesMap(self, reloadMap = False, objForSingleElems = False):
    if not self.basicFeaturesMap: reloadMap = True
    if reloadMap: self.__loadBasicFeaturesMap(objForSingleElems)
    return self.basicFeaturesMap

  def __loadBasicFeaturesMap(self, objForSingleElems = False):
    # Extract XML data from client file
    doesOutputFileExist = os.path.exists(COMP_utils.buildPath(base_output_directory_xml_or_tsv, self.outputXmlFileName))
    if doesOutputFileExist == False:
      extractor = Extractor(base_client_binary_data_directory, base_output_directory_xml_or_tsv)
      extractor.extract('item', self.inputBinaryFileName)
    # Parse XML file
    objs = XmlParser.parseXmlObjectFromFile(self.outputFilePath, objForSingleElems)
    for obj in objs:
      lenOfStuff = len(obj['MiItemData'][0]['common'][0]['MiSkillItemStatusCommonData'])
      if lenOfStuff > 0:
        if not(obj['MiItemData'][0]['common'][0]['MiSkillItemStatusCommonData'][lenOfStuff-1]['correctTbl'] is None):
          if (len(obj['MiItemData'][0]['common'][0]['MiSkillItemStatusCommonData'][lenOfStuff-1]['correctTbl']) > 0):
            objId = next(PyUtils.getValueFromNestedDictionary('id', obj))
            self.basicFeaturesMap[objId] = self.__falttenObject(obj)

  def __falttenObject(self, obj):
    res = {}

    res = {
      'id': next(PyUtils.getValueFromNestedDictionary('id', obj)),
      'mainCategory': next(PyUtils.getValueFromNestedDictionary('mainCategory',obj)),
      'subCategory': next(PyUtils.getValueFromNestedDictionary('subCategory',obj)),
      'affinity': next(PyUtils.getValueFromNestedDictionary('affinity',obj)),
      'correctTbl': [],
      'buyPrice': next(PyUtils.getValueFromNestedDictionary('buyPrice',obj)),
      'sellPrice': next(PyUtils.getValueFromNestedDictionary('sellPrice',obj)),
      'repairPrice': next(PyUtils.getValueFromNestedDictionary('repairPrice',obj)),
      'appearanceID': next(PyUtils.getValueFromNestedDictionary('appearanceID',obj)),
      'weaponType': next(PyUtils.getValueFromNestedDictionary('weaponType',obj)),
      'equipType': next(PyUtils.getValueFromNestedDictionary('equipType',obj)),
      'flags': next(PyUtils.getValueFromNestedDictionary('flags',obj)),
      'durability': next(PyUtils.getValueFromNestedDictionary('durability',obj)),
      'stackSize': next(PyUtils.getValueFromNestedDictionary('stackSize',obj)),
      'useSkill': next(PyUtils.getValueFromNestedDictionary('useSkill',obj)),
      'gender': next(PyUtils.getValueFromNestedDictionary('gender',obj)),
      'level': next(PyUtils.getValueFromNestedDictionary('level',obj)),
      'alignment': next(PyUtils.getValueFromNestedDictionary('alignment',obj)),
      'modSlots': next(PyUtils.getValueFromNestedDictionary('modSlots',obj)),
      'stock': next(PyUtils.getValueFromNestedDictionary('stock', obj)),
      'gpRequirement': next(PyUtils.getValueFromNestedDictionary('GPRequirement',obj)),
      'rental': next(PyUtils.getValueFromNestedDictionary('rental',obj))
    }

    for tbl in PyUtils.getValueFromNestedDictionary('MiCorrectTbl',obj):
      res['correctTbl'].append(tbl)

    return res
    