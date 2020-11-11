import glob
import json
import math
import xml.etree.ElementTree as ET

class XmlParser(object):
  
  ##############################
  # Xml Schema
  ##############################

  @staticmethod
  def printXmlSchemaFromXmlFile(inputFilename, outputFileName):
    xmlTree = ET.parse(inputFilename)
    xmlSchema = XmlParser.__getXmlObjectSchema(xmlTree)
    XmlParser.__printXmlSchemaToFile(xmlSchema, outputFileName)
  
  @staticmethod
  def printXmlSchemaFromXmlFileList(inputFileList, outputFileName):
    masterXmlSchema = []
    for f in inputFileList:
      xmlTree = ET.parse(f)
      fileXmlSchema = XmlParser.__getXmlObjectSchema(xmlTree)
      masterXmlSchema = masterXmlSchema + fileXmlSchema
    XmlParser.__printXmlSchemaToFile(masterXmlSchema, outputFileName)

  @staticmethod
  def __processXmlObjSchema(elem, level, parentProperty, xmlSchema):
    schemaPropertyName = elem.attrib.get('name') or elem.tag
    schemaProperty = '{parent}.{name}'.format(parent=parentProperty, name=schemaPropertyName)
    xmlSchema.append(schemaProperty)
    for child in elem:
      XmlParser.__processXmlObjSchema(child, level + 1, schemaProperty, xmlSchema)

  @staticmethod
  def __getXmlObjectSchema(xmlObject):
    xmlSchema = []
    XmlParser.__processXmlObjSchema(xmlObject.getroot(), -1, '.', xmlSchema)
    return xmlSchema

  @staticmethod
  def __printXmlSchemaToFile(xmlSchema, outputFileName):
    res = []
    for elem in sorted(list(dict.fromkeys(xmlSchema))):
      lastCharIndex = elem.rfind('.') + 1
      strToRemove = elem[0:lastCharIndex]
      newStr = ' ' * int(math.floor(len(strToRemove)/6))
      res.append(elem.replace(strToRemove, newStr))
    with open(outputFileName, 'w') as outputFile:
      for field in res:
        outputFile.write(field+"\n")

  ##############################
  # Xml Object Parsing
  ##############################

  @staticmethod
  def parseXmlObjectFromFiles(fileNamesList, objForSingleElems = False):
    objs = []
    for f in fileNamesList:
      objs = objs + XmlParser.parseXmlObjectFromFile(f, objForSingleElems)
    return objs

  @staticmethod
  def parseXmlObjectFromFile(fileName, objForSingleElems = False):
    xmlTree = ET.parse(fileName)
    return XmlParser.parseXmlObject(xmlTree, objForSingleElems)

  @staticmethod
  def parseXmlObject(xmlObject, objForSingleElems = False):
    objs = []
    for child in xmlObject.getroot():
      xmlTmpObj = {}
      XmlParser.__depthTraversalOnXmlElem(child, -1, xmlTmpObj, objForSingleElems)
      objs.append(xmlTmpObj)
    return objs

  @staticmethod
  def __depthTraversalOnXmlElem(elem, level, parentNode, objForSingleElems=False):
    objKey = elem.attrib.get('name') or elem.tag
    numChildren = len(elem.getchildren())
    if numChildren == 0:
      if isinstance(parentNode, list): parentNode.append({ objKey: elem.text })
      if isinstance(parentNode, dict): parentNode[objKey] = elem.text
    else:
      newParentNode = None
      if numChildren == 1 and isinstance(parentNode, dict): 
        parentNode[objKey] = {}
        newParentNode = parentNode[objKey]
      elif numChildren > 1 and isinstance(parentNode, dict): 
        parentNode[objKey] = []
        newParentNode = parentNode[objKey]
      elif objForSingleElems and numChildren == 1 and isinstance(parentNode, list): 
        newObj = { objKey: {} }
        parentNode.append(newObj)
        newParentNode = newObj[objKey]
      elif numChildren >= 1 and isinstance(parentNode, list): 
        newObj = { objKey: [] }
        parentNode.append(newObj)
        newParentNode = newObj[objKey]
      for child in elem:  
        XmlParser.__depthTraversalOnXmlElem(child, level + 1, newParentNode)
