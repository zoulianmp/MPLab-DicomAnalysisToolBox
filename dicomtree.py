# dicomtree.py
"""Show a dicom file using a hierarchical tree in a graphical window"""
# Copyright (c) 2008-2012 Darcy Mason
# This file is part of pydicom, relased under an MIT license.
#    See the file license.txt included with this distribution, also
#    available at http://pydicom.googlecode.com

usage = "Usage: python dicomtree.py dicom_filename"
from dicom.valuerep import PersonNameUnicode

import Tix

def RunTree(w, filename):
    top = Tix.Frame(w, relief=Tix.RAISED, bd=1)
    tree = Tix.Tree(top, options="hlist.columns 2")
    tree.pack(expand=1, fill=Tix.BOTH, padx=10, pady=10, side=Tix.LEFT)
    # print tree.hlist.keys()   # use to see the available configure() options
    tree.hlist.configure(bg='white', font='Courier 10', indent=30)
    tree.hlist.configure(selectbackground='light yellow', gap=150)
    
    box = Tix.ButtonBox(w, orientation=Tix.HORIZONTAL)
    # box.add('ok', text='Ok', underline=0, command=w.destroy, width=6)
    box.add('exit', text='Exit', underline=0, command=w.destroy, width=6)
    box.pack(side=Tix.BOTTOM, fill=Tix.X)
    top.pack(side=Tix.TOP, fill=Tix.BOTH, expand=1)

    show_file(filename, tree)

def show_file(filename, tree):
    tree.hlist.add("root", text=filename)
    ds = dicom.read_file(filename,force= True)
    ds.decode()  # change strings to unicode
    recurse_tree(tree, ds, "root", False)
    tree.autosetmode()

def recurse_tree(tree, dataset, parent, hide=False):
    # order the dicom tags
    for data_element in dataset:
        node_id = parent + "." + hex(id(data_element))
        if isinstance(data_element.value, unicode):
            tree.hlist.add(node_id, text=unicode(data_element))
        else:
            tree.hlist.add(node_id, text=str(data_element))
        if hide:
            tree.hlist.hide_entry(node_id)
        if data_element.VR == "SQ":   # a sequence
            for i, dataset in enumerate(data_element.value):
                item_id = node_id + "." + str(i+1)
                sq_item_description = data_element.name.replace(" Sequence", "") # XXX not i18n
                item_text = "%s %d" % (sq_item_description, i+1)
                tree.hlist.add(item_id, text=item_text)
                tree.hlist.hide_entry(item_id)
                recurse_tree(tree, dataset, item_id, hide=True)

if __name__ == '__main__':
    import sys
    import dicom
    
    
    
    
    
    
    
    
    
    
    
    
    

    if len(sys.argv) == 2:
             
        root = Tix.Tk()
        root.geometry("%dx%d%+d%+d" % (800, 600, 0, 0))
        
        RunTree(root, sys.argv[1])
        root.mainloop()
        
    
    else:
        
        root = Tix.Tk()
        root.geometry("%dx%d%+d%+d" % (800, 600, 0, 0))
        
        folder = "C:\\Users\\zoulian\\Desktop\\magicalphantomtest"
        
        filename = "\\templatedataset.dcm"
        
        path1 = folder + filename
        
        dataset = dicom.read_file(path1,force=True)
        
        print dataset
        
        
        
        
        
        
        
        
        
        
        
        path = folder + filename
    
        RunTree(root, path)
        root.mainloop()


        root1 = Tix.Tk()
        root1.geometry("%dx%d%+d%+d" % (800, 600, 0, 0))
        
        folder1 = "C:\\Users\\zoulian\\Desktop\\magicalphantomtest"
        
        filename1 = "\\CTI.201407070501.0010814101700004.96.Zhou_li_rong"
        
        path1 = folder + filename
    
        RunTree(root1, path1)
        root1.mainloop()