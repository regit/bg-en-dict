import codecs
#from lxml import etree
import re

f = open('bg_en.dat', 'rb')
out = open('regit-bg-en.csv', 'wb')

dico = f.read()

word_list = dico.split('\0')

#root = etree.Element('dictionary')

for entry in word_list:
    definition = codecs.decode(entry, 'cp1251')
    entry_parts = definition.split('\n', 1)
    if len(entry_parts) == 2:
        print(entry_parts[0])
        out.write(entry_parts[0].encode('utf8'))
        out.write(u'\t')
        out.write(entry_parts[1].replace('\n','\\n').encode('utf8'))
        out.write(u'\n')
#        def_entry = etree.Element('entry')
#        def_key = etree.Element('key')
#        def_key.text = entry_parts[0]
#        def_entry.append(def_key)
#        def_def = etree.Element('def')
#        def_def.text = def_word
#        def_entry.append(def_def)
#        root.append(def_entry)
#
#s = etree.tostring(root, pretty_print=True, encoding='UTF-8')
#print s
