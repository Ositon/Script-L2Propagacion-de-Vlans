import myfunc as func

print(""""----Script para propagacion de vlans Capa 2----""")
a = input(""""----¿Swith A ó B? (A/B)------\n""")
vlanchart = func.f_vlanbuild()
func.f_remplacevlans(vlanchart, a)
func.f_fusiontxt()
input("Presiona enter para salir...")
