import re
import zipfile
import io
from lxml import etree as ET
import os

# 获取当前文件所在目录
current_dir = os.path.dirname(os.path.abspath(__file__))
input_docx = os.path.join(current_dir, "docs", "input.docx")
output_docx = os.path.join(current_dir, "docs", "output.docx")

# 检查输入文件是否存在
if not os.path.exists(input_docx):
    print(f"❌ 错误：输入文件不存在: {input_docx}")
    print("请确保在以下位置放置一个Word文档：")
    print(f"  {input_docx}")
    print("文档中应包含类似格式的文本：")
    print('  "天地玄黄（tiān dì xuán huáng）"')
    exit(1)

print(f"📄 正在处理文件: {input_docx}")

# Word 命名空间
ns = {'w': 'http://schemas.openxmlformats.org/wordprocessingml/2006/main'}

# 正则：匹配 "天地玄黄（tiān dì xuán huáng）"
pattern = re.compile(r'([\u4e00-\u9fff]+)（([a-zāáǎàēéěèīíǐìōóǒòūúǔùüǖǘǚǜ\s]+)）')

def create_ruby(hanzi, pinyin):
    ruby = ET.Element(f"{{{ns['w']}}}ruby")

    rubyPr = ET.SubElement(ruby, f"{{{ns['w']}}}rubyPr")
    ET.SubElement(rubyPr, f"{{{ns['w']}}}rubyAlign", {f"{{{ns['w']}}}val": "center"})
    ET.SubElement(rubyPr, f"{{{ns['w']}}}hps", {f"{{{ns['w']}}}val": "14"})
    ET.SubElement(rubyPr, f"{{{ns['w']}}}hpsRaise", {f"{{{ns['w']}}}val": "14"})
    ET.SubElement(rubyPr, f"{{{ns['w']}}}hpsBaseText", {f"{{{ns['w']}}}val": "28"})

    rt = ET.SubElement(ruby, f"{{{ns['w']}}}rt")
    rt_r = ET.SubElement(rt, f"{{{ns['w']}}}r")
    rt_t = ET.SubElement(rt_r, f"{{{ns['w']}}}t")
    rt_t.text = pinyin

    rb = ET.SubElement(ruby, f"{{{ns['w']}}}rb")
    rb_r = ET.SubElement(rb, f"{{{ns['w']}}}r")
    rb_t = ET.SubElement(rb_r, f"{{{ns['w']}}}t")
    rb_t.text = hanzi

    return ruby

# 1. 读取 docx 内的 document.xml
with zipfile.ZipFile(input_docx, 'r') as zin:
    xml_content = zin.read("word/document.xml")

parser = ET.XMLParser(remove_blank_text=True)
tree = ET.parse(io.BytesIO(xml_content), parser)
root = tree.getroot()

# 2. 查找所有 w:t 节点
found_matches = 0
for t_node in root.findall('.//w:t', ns):
    text = t_node.text
    if not text:
        continue
    match = pattern.search(text)
    if match:
        found_matches += 1
        hanzi = match.group(1)
        pinyins = match.group(2).strip().split()
        print(f"✓ 找到匹配：{hanzi}（{' '.join(pinyins)}）")
        if len(hanzi) != len(pinyins):
            print(f"⚠️ 警告：汉字和拼音数量不匹配，已跳过")
            continue

        # 找到 <w:r> 父节点
        r_node = t_node.getparent()
        p_node = r_node.getparent()
        idx = list(p_node).index(r_node)

        # 插入 ruby
        for i in range(len(hanzi)):
            ruby_elem = create_ruby(hanzi[i], pinyins[i])
            p_node.insert(idx + i, ruby_elem)

        # 删除原 <w:r>
        p_node.remove(r_node)

# 3. 把修改后的 XML 写回 docx
with io.BytesIO() as xml_buffer:
    tree.write(xml_buffer, encoding="utf-8", xml_declaration=True)
    new_xml = xml_buffer.getvalue()

with zipfile.ZipFile(input_docx, 'r') as zin:
    with zipfile.ZipFile(output_docx, 'w') as zout:
        for item in zin.infolist():
            if item.filename != "word/document.xml":
                zout.writestr(item, zin.read(item.filename))
            else:
                zout.writestr("word/document.xml", new_xml)

if found_matches == 0:
    print("⚠️ 警告：未找到任何匹配的文本")
    print("请确保文档中包含类似格式的文本：")
    print('  "天地玄黄（tiān dì xuán huáng）"')
else:
    print(f"✅ 处理完成，共找到 {found_matches} 处匹配")
    print(f"📝 输出文件：{output_docx}")
