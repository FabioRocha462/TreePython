
def down(List,index = 1):
  if List[index * 2] != -1 and List[(index * 2) + 1] != -1:  
    index = index + 1  
    return down(List,index)
  return index

def insert(List,value):
  if List[1] == -1:
    List[1] = value
  else:
    index = down(List)
    if List[index *2 ] != -1:
      if List[index * 2] > value:
        aux = List[index * 2]
        List[(index * 2)+ 1] = aux
        List[index * 2] = value
      else:
        List[(index * 2)+ 1] = value
    else:
      List[index *2 ] = value
          
def print_Tree(List):
  for i in List:
    if i != -1:
      print(i)

def cont_values(List):
  cont = 0
  for i in List:
    if i != -1:
      cont = cont + 1
  return cont

def cont_nivel(List,index,cont = 0):
  if index >= 1:
    index = index // 2
    cont = cont + 1
    return cont_nivel(List, index,cont) 
  return cont - 1
    
  
def searchInTree(List,value,index = 1):
  if index < cont_values(List) // 2 + 1:
    if List[1] == value:
      return index
    else:
      if List[index * 2] == value or List[(index * 2) + 1] == value:
        return List.index(value)
      else:
        return searchInTree(List,value,index + 1)
  return 0
      
def leafs(List):
  values_number = cont_values(List)
  nivel = cont_nivel(List,values_number)
  pot = 2 ** nivel
  return values_number - (pot - 1)
def downRemove(List,index):
  if List[index * 2] != -1:
    List[index] = List[index * 2]
    if List[index] > List[index + 1]:
      aux = List[index + 1]
      List[index + 1] = List[index]
      List[index] = aux
      index = index * 2
      return downRemove(List,index)
  return index
    
    
def remove(List,value):
  index = searchInTree(List,value)
  if index == 0:
    return "not found"
  else:
    if List[index * 2] == -1 and List[(index * 2) + 1] == -1:
      List[index] = -1
    if List[index * 2] == -1 and List[(index * 2) + 1] != -1:
      List[index] = List[(index * 2) + 1]
      List[(index * 2) + 1] = -1
    if List[index * 2 ]!= -1 and List[(index * 2) + 1] != -1:
      index = downRemove(List,index)
      List[index * 2 ] = -1
      
      
    
      
    
    
        
    
  
  
  
  
  

  
      
    