class Person(object):

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def get_name(self):
        return '%s %s' % (self.firstname, self.lastname)
        
class Parent(object): #define parent class
  def __init__(self, firstname, lastname):
    self.name=Person(firstname, lastname)
    self.child=[]
    
  def new_child(self, firstname, lastname): #adding new child
    c=Children(firstname, lastname, self.name.get_name) #initiate child
    self.child.append(c.name.get_name) #append child's name into list
  
  def get_child(self):
    return self.child
    
class Children(object): #define children class
  def __init__(self, firstname, lastname, parent):
    self.name = Person(firstname, lastname)
    self.parent = parent #set parent of the child
    
  def get_parent(self): #returns parent's name
    return self.parent.name.get_name
