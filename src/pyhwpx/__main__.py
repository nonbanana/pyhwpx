import zipfile
import xmltodict
import json
import xml.etree.ElementTree as ET

file_name = "[별표] 유독물질(제3조 관련)(유독물질의 지정고시).hwpx"
hwpx_file = zipfile.ZipFile(file_name)

section0 = hwpx_file.read("Contents/section0.xml").decode()
import io
# section0 = xmltodict.parse(section0)
print(section0)
# tree = ET.ElementTree()
root = ET.fromstring(section0)
print(root.tag)

for table in root.iterfind('tbl'):
    print(table)
    for row in table.findall("hp:tr"):
        for column in row.findall("hp:tc"):
            sub_list = column.find("hp:subList")
            p = sub_list.find("hp:p")
            run = p.find("hp:run")
            text = run.find("hp:t").text
            print(text.encode())

# print(json.dumps(section0, indent=4))
# with open("section0.json", 'w') as fp:
#     json.dump(section0,fp, indent=4)