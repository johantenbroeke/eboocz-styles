import os
import zipfile


TEMPLATE = """---
layout: default
title: Eboocz styles
---

##Eboocz styles


%(styles)s

"""

STYLE_TEMPLATE = """###%(style_name)s

![%(style_name)s](images/%(style_id)s.png "%(style_name)s")

[install](styles/%(style_id)s.ebczstyle)

----------

"""


class EbooczStyleBuilder:

    def __init__(self):
        self.styles = ""

    def zip(self,src, dst):
        zf = zipfile.ZipFile("%s.ebczstyle" % (dst), "w", zipfile.ZIP_DEFLATED)
        abs_src = os.path.abspath(src)
        for dirname, subdirs, files in os.walk(src):
            for filename in files:
                absname = os.path.abspath(os.path.join(dirname, filename))
                arcname = absname[len(abs_src) + 1:]
                print 'zipping %s as %s' % (os.path.join(dirname, filename),arcname)
                zf.write(absname, arcname)
        zf.close()
        self.styles += STYLE_TEMPLATE%{"style_name":src,"style_id":src}


    def writeMarkDown(self):
        markdown = TEMPLATE%{"styles":self.styles}
        f = open("../index.md","w")
        f.write(markdown)
        f.close()


if __name__ == "__main__":
    b = EbooczStyleBuilder()
    b.zip("style-1", "../styles/style-1")
    b.zip("style-2", "../styles/style-2")
    b.zip("style-3", "../styles/style-3")
    b.writeMarkDown()