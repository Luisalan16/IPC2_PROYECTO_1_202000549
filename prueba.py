import xml.etree.ElementTree as ET

tree = ET.parse('ejemplo1.xml')
root = tree.getroot()

dato = root.findall('dato')

for senales in root:
    print("Nombre de la prueba: ", senales.attrib.get('nombre'))
    tiempo = int(senales.attrib.get('t'))
    amplitud = int(senales.attrib.get('A'))
    data = int(senales.text)
    print(f'[t= {tiempo}], [A= {amplitud}], {data}')