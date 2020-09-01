import sys, re
from extractor import Extractor
from MappingFormatsAndFiles import mapping_formats_and_files as faf
from config import base_client_binary_data_directory, base_output_directory_xml_or_tsv

extractor = Extractor(base_client_binary_data_directory, base_output_directory_xml_or_tsv)

option = sys.argv[1] if len(sys.argv) > 1 else "load"

for format in faf:
    extractor.extract(format, faf[format], option)

