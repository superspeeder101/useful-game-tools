class Item(object):
  def __init__(self, name, raw_ingredient=False,requirements={}):
    assert isinstance(requirements,dict)
    self.name=  name
    self.raw = raw_ingredient
    if not self.raw:
      self.requirements = requirements
  
  def __repr__(self):
    return "<Item {}>".format(self.name)
    

def raw_rescources(itm, earlyout={}):
  output = earlyout
  if itm.raw:
    output = {itm:1}
    return output
  
  else:
    for item in itm.requirements.keys():
      if item.raw:
        if item in output.keys():
          output[item] = output[item] + itm.requirements[item]
        else:
          output[item] = itm.requirements[item]
        
        
        
  return output


