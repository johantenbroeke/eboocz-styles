import os
import zipfile

def zip(src, dst):
    zf = zipfile.ZipFile("%s.ebczstyle" % (dst), "w", zipfile.ZIP_DEFLATED)
    abs_src = os.path.abspath(src)
    for dirname, subdirs, files in os.walk(src):
        for filename in files:
            absname = os.path.abspath(os.path.join(dirname, filename))
            arcname = absname[len(abs_src) + 1:]
            print 'zipping %s as %s' % (os.path.join(dirname, filename),
                                        arcname)
            zf.write(absname, arcname)
    zf.close()

zip("style-1", "../styles/style-1")
zip("style-2", "../styles/style-2")
zip("style-3", "../styles/style-3")