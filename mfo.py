#PSEUDOCODIGO

# INICIALIZAR POBLACION POLILLAS

# while iter < maxIter:
#     actualizar numero llamas segun ecuacion 4
#     calcular fitness de las polillas
#     if iter ==1:
#         OF = sort (OM1)
#         F = sort (M1)
#     else:
#         OF = sort (OMiter-1,OMiter)
#         F = sort (Miter-1,Miter)
    
#     Determinar mejor llama
#     for i=1 hasta N:
#         for j = 1 hasta dim:
#             actualizar r y t
#             calcular D usando ecuacion 3
#             actualizar polilla M(i,j) usando ecuacion 1 y ecuacion 2
    
#     calcular el valor de probabilidad de la polilla M(i,j) usando TFs en ecuacion 5, TFv en ecuación 7 y TFu en ecuacion 9
#     actualizar nuevas posisiones usando ecuacion 6, ecuacion 8 y ecuacion 10
#     iter = iter+1

# return optimo global ( la mejor llama)

#ecuacion 1
#position updating of each moth relative to the corresponding flame
# Mi = S (Mi,Fj)        
# where S is the spiral function and Mi and Fj representh the i-th and j-th flame

#ecuacion 2
# S(Mi,Fj) = Di  * e^bt * cos(2pi) + Fj
#   b constante para la forma de la espiral
#   t numero aleatorio entre [-r,1] donde r es un factor de convergencia y deree linearlmente desde -1 a -2 durante el curso de la iteraciones

#ecuacion 3
# Di = abs( Mi - Fj)
# distancia entre polilla i y llama j

#ecuacion 4
#reducir la cantidad de llamas cada iteración 
# Flameno = round( N - iter*(N-1)/maxIter)

#Binarizar 

#fitness
#fitness = mu.CE + lambda(Nsf/Ntf)
#   CE : classification error
#   Nsf : number of selected features
#   Ntf : number of total features
#   mu : significance of classification quality
#   lambda(1-mu): significance of feaure reduction








