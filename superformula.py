import sys
import subprocess
sys.path.append('/opt/hfs15.0.244.16/houdini/python2.7libs')

import hou
hou.hipFile.save(file_name='/home/ramon/hello.hipnc')


hou.hipFile.load(file_name='/home/ramon/hello.hipnc')
otl_file = '/home/ramon/dev/vex/superformula.otl'
hou.hda.installFile(otl_file)

sf_vex  = hou.node('/shop').createNode('superformula')
sf_geo  = hou.node('/obj').createNode('geo')
sf_geo.children()[0].destroy()
sf_null = sf_geo.createNode('null')
sf_attribvop = sf_geo.createNode('attribvop')
sf_attribvop.setFirstInput(sf_null)
sf_attribvop.parm('bindclass').set('detail')
sf_attribvop.parm('vexsrc').set('shop')
sf_attribvop.parm('shoppath').set('/shop/superformula1')
sf_attribvop.setDisplayFlag(True)


hou.hipFile.save(file_name='/home/ramon/hello.hipnc')
subprocess.Popen(['houdinifx', '/home/ramon/hello.hipnc'])

