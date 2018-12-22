from lxml import etree
import csv
import xml.dom.minidom

root = etree.Element("Interaction")

rdr = csv.reader(open("test.txt"))
header = rdr.next()
for row in rdr:
    eg = etree.SubElement(root, "Person")
    for h, v in zip(header, row):
        etree.SubElement(eg, h).text = v

f = open(r"test.xml", "w")
f.write(etree.tostring(root))
f.close()
xml = xml.dom.minidom.parse("test.xml")
pretty_xml_as_string = xml.toprettyxml()
g = open("prettytest.xml", "a")
g.write(pretty_xml_as_string)
g.close()
