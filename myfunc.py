def f_vlanbuild():
  new_script=open('first.txt',"w")
  line='system-view\n'+'#\n'
  new_script.write(line)
  vlanchart=''
  while True:
      vlan=(input("Introduce la vlan a propagar\n"))
      vlanchart= vlanchart+' '+ vlan
      line='vlan'+' '+ vlan+'\n'
      new_script.write(line)
      desc=input("Introduce la descripcion\n")
      line='description'+' '+desc+'\n'+'#\n'
      new_script.write(line)
      #func.f_vlanbuild(vlan,desc)
      a=input("Agregar otra vlan (S/N):\n")
      if a == 'N' or a == 'n':
          print("Se ha agregado esta informacion al archivo Script Propagacion de vlan Capa 2.txt")
          break
  new_script.close()
  return vlanchart

def f_remplacevlans(vlans,opc):
  print(opc)
  if opc=='A':
      file =open('template.txt','r')
  else:
      file =open('template2.txt','r')
  new_script=open('second'+".txt","w")
  new_line=''
  for line in file:
      new_line=line
      if "port trunk allow-pass vlan" in line:
          new_line=line.replace('$X',str(vlans))
      new_script.write(new_line)
  file.close()
  new_script.close()

def f_fusiontxt():
  file=open('first.txt','r')
  file2=open('second.txt','r')
  new_script=open('Script L2_Propagacion de Vlans'+'.txt','w')
  for line in file:
      new_script.write(line)
  for line2 in file2:
      new_script.write(line2)
  file.close()
  file2.close()
  new_script.close()

