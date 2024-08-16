import os
from lxml import etree

def remove_unregistered_from_svg(input_file, output_file):
    # Parse the SVG file
    parser = etree.XMLParser(remove_blank_text=True)
    tree = etree.parse(input_file, parser)
    root = tree.getroot()

    # Define the SVG namespace
    ns = {'svg': 'http://www.w3.org/2000/svg'}

    # Find all text elements in the SVG
    for text_element in root.xpath('//svg:text', namespaces=ns):
        # Check if the text is not None and contains "UNREGISTERED"
        if text_element.text and 'UNREGISTERED' in text_element.text:
            # Remove the text element
            parent = text_element.getparent()
            parent.remove(text_element)

    # Write the modified SVG to a new file
    tree.write(output_file, pretty_print=True, xml_declaration=True, encoding='UTF-8')

# Usage
input_svg = os.path.abspath('your_file.svg')  # Sử dụng đường dẫn tuyệt đối, để file svg cần xử lý và đây
output_svg = os.path.abspath('output.svg')
remove_unregistered_from_svg(input_svg, output_svg)
