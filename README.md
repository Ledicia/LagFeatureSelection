Folder containing data and code for selction layer adapted for timeseries.
# ARCHIVOS:

data:
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
        
    
