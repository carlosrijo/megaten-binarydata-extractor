import sys, re
from extractor import Extractor
from FormatsAndFiles import formatsFiles as faf
from config import base_input_directory_sbin, base_output_directory_xml_or_tsv

extractor = Extractor(base_input_directory_sbin, base_output_directory_xml_or_tsv)

option = sys.argv[1] if len(sys.argv) > 1 else "load"

for format in faf:
    extractor.extract(format, faf[format], option)

