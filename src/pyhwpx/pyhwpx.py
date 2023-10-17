import zipfile
import xmltodict
import json
file_name = "[별표] 유독물질(제3조 관련)(유독물질의 지정고시).hwpx"
hwpx_file = zipfile.ZipFile(file_name)

section0 = hwpx_file.read("Contents/section0.xml")

section0 = xmltodict.parse(section0)
print(json.dumps(section0, indent=4))
