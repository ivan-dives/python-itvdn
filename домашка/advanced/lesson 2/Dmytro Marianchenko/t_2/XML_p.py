import xml.etree.cElementTree as ET

root = ET.Element("body")
doc = ET.SubElement(root, "row")

ET.SubElement(doc, "field1", name="blah").text = "some value1"
ET.SubElement(doc, "field2", name="asdfasd").text = "some vlaue2"
tree = ET.ElementTree(root)

tree.write("my_file.xml")