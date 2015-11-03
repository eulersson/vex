import hou
otl_file = 'D:/houdini_projects/vex/superformula.otl'
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



