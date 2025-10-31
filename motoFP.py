from typing import NamedTuple
from datetime import datetime, time, timedelta
from pathlib import Path
import csv


Piloto=NamedTuple("Piloto", [("nombre", str),("escuderia", str)])

CarreraFP=NamedTuple("CarreraFP",[
    ("fecha_hora",datetime), #"%Y-%m-%d H:M"
    ("circuito",str),                    
    ("pais",str), 
    ("seco",bool), # True si el asfalto estuvo seco, False si estuvo mojado
    ("tiempo",float), 
    ("podio", list[Piloto])])



def lee_carreras(filename: str) -> list[CarreraFP]:
    with open(filename, encoding="utf-8") as f: 
        reader = csv.reader((f))
        next(reader)

        carrera_fp : list[CarreraFP] = []

        for line in reader:
            l = CarreraFP(
                fecha_hora=datetime.strptime(line[0], "%Y-%m-%d %H:%M"),
                circuito=line[1],
                pais=line[2],
                seco=True if line[3] == "seco" else False,
                tiempo=float(line[4]),
                podio=list(Piloto(nombre=line[5], escuderia=line[6:])) #type:ignore
            )
            carrera_fp.append(l)

        return carrera_fp



def maximo_dias_sin_ganar(carreras: list[CarreraFP], nombre_piloto: str) -> int | None:
    nombre_cerreras : list[CarreraFP]= []

    for carrera in carreras:
        print(carrera.podio[0])
        if nombre_piloto == carrera.podio[0]:
            nombre_cerreras.append(carrera)

    if  len(nombre_cerreras) < 2:
        return None
    delta_time = timedelta(0)
    delta_time_list :list[timedelta]= []
    x = 0

    while x < len(nombre_cerreras):
        delta_time = nombre_cerreras[x-1].fecha_hora - nombre_cerreras[x].fecha_hora
        delta_time_list.append(delta_time)
        x += 1  

    return max(delta_time_list) #type:ignore




def piloto_mas_podios_por_circuito(carreras: list[CarreraFP]) -> dict[str,str]:
    carreras_dict = {}

    for c in carreras:
        carreras_dict[c.circuito] = c.podio[0]

    return carreras_dict







