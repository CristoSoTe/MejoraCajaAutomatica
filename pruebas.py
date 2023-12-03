def carton_salida(self, series, carton, salida_cierre, etiqueta_rango1, salida, precio):

        #-------------------- Carton salida del rango 2 ---------------------------------
        serie_rango1 = etiqueta_rango1.cget("text")
        numero_carton = (int(serie_rango1)*6) + int(salida)
        if precio == "1.5":
            if series[0].cget("text") == "0":
                carton[0].config(text="0")
            else:
                carton[0].config(text=numero_carton)
            indice_destino = 4
        elif precio == "2":
            if series[0].cget("text") == "0":
                carton[1].config(text="0")
            else:
                carton[1].config(text=numero_carton)
            indice_destino = 5
        elif precio == "3":
            if series[0].cget("text") == "0":
                carton[2].config(text="0")
            else:
                carton[2].config(text=numero_carton)
            indice_destino = 6
        else:
            if series[0].cget("text") == "0":
                carton[3].config(text="0")
            else:
                carton[3].config(text=numero_carton)
            indice_destino = 7

        # #---------------------Carton salida del rango 3 al 9 -------------------------
        indice_origen = 1
        rango_con_serie = 1
        for i in series[:7]:
            if series[indice_origen].cget("text") == "0":
                carton[indice_destino].config(text="0")
                indice_origen += 1
                indice_destino += 4
                rango_con_serie +=1
            else:
                numero_series = series[indice_origen - rango_con_serie].cget("text")
                numero_carton_siguiente = int(numero_series) * 6 + numero_carton 
                carton[indice_destino].config(text=numero_carton_siguiente)
                numero_carton = numero_carton_siguiente
                indice_origen += 1
                indice_destino += 4

                #-------------- Carton salida del cierre ----------------------------
                if precio == "1.5":
                    ultima_serie = series[indice_origen - 1].cget("text")
                    carton_salida_cierre= (int(ultima_serie) * 6) + numero_carton_siguiente
                    salida_cierre[0].config(text=carton_salida_cierre)
                elif precio== "2":
                    ultima_serie = series[indice_origen - 1].cget("text")
                    carton_salida_cierre= (int(ultima_serie) * 6) + numero_carton_siguiente
                    salida_cierre[1].config(text=carton_salida_cierre)
                elif precio== "3":
                    ultima_serie = series[indice_origen - 1].cget("text")
                    carton_salida_cierre= (int(ultima_serie) * 6) + numero_carton_siguiente
                    salida_cierre[2].config(text=carton_salida_cierre)
                else:
                    ultima_serie = series[indice_origen - 1].cget("text")
                    carton_salida_cierre= (int(ultima_serie) * 6) + numero_carton_siguiente
                    salida_cierre[3].config(text=carton_salida_cierre)

                rango_con_serie = 1