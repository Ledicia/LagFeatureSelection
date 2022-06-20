Folder containing data and code for selction layer adapted for timeseries.
# ARCHIVOS:

Ambos archivos están ordenados de tal manera que la fila 1 es la más antigua, ergo la medida de la fila 1 de la variable X1 puede causar la medida de la fila 15 de la variable Y1.

mixed/data:
    - Las variables X1,..., X8 son señales reales normalizadas.
    - Las variables Y1,..., Y6 son variables creadas a partir de funciones no lineales.
    - REDUNDANCIAS:
        X3 = forrester(X1)
        X5 = cheng_sandu(X1, X2)
        X7 = branin(X4,X6)
        
    - CAUSED:
        Y1 = grlee12(X1)
        Y2 = higdon(X1) + holsclaw(X6)
        Y3 = lim(X1, X6)
        Y4 = lim(X1, X6) + noise
        Y5 = franke(X1, X7)
        Y6 = lim(X1, X6) for some periods and lim_modified(X1, X6) for other periods
   
    - Variables shifteadas al pasado:
        Mean lag of target X1 is 28.45  Hum
        Mean lag of target X2 is 20.32  Bas
        Mean lag of target X3 is 15.31  Sie
        Mean lag of target X4 is 11.64  Alt
        Mean lag of target X5 is 7.96   Vel
        Mean lag of target X6 is 4.97   T11
        Mean lag of target X7 is 2.51   Pot
        Mean lag of target X8 is 0.49   T12
        
        
sim2/TLD_r0_d2nu_s2_p10_T15:
    - Conjunto de datos con 10 variables causales sampleadas de distribuciones normales y uniformes de media y variaza aleatorias.
    - No hay redundancias en las variables
    - Lag máximo es 15.
    - Combinación lineal.
        
    
