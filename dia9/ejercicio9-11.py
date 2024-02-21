""" Ejercicios con el módulo re, útil para buscar en cadenas de texto
A diferencia de como lo hacíamos antes, aquí podemos busar con patrones mas elaborados y complicados."""

""" Algunos ejemplos
caracter                descripción                     ejemplo
/d                      digito numérico                 v\\d.\\d\\d (en la práctica solo es con 1 barra)
                                                        v1.20
/w                      caracter ALFANUMERICO           \\w\\w\\w - \\w\\w 
                                                        ABC - 25
/s                      espacio en blanco               número\\s\\d\\d
                                                        número 25
/D                      NO es un dígito                 \\D\\D\\D\\D
                                                        abc?
/W                      NO es alfanumerico              \\W\\W\\W
                                                        ?*? 
/S                      NO tiene espacio en blanco      \\S\\S\\S\\S
                                                        1234, O abcd, etc etc
"""

""" También existen los cuantificadores
caracter                descripcion                     ejemplo
 +                      1 o más veces                   código_\\d-\\d+
                                                        código_5-5938539
 {n}                    se repite n veces               \\d-\\d{4}
                                                        5-7777
 {n, m}                 repite entre n y m veces        \\w{3, 5}
                                                        hola, sol, mundo, yo123
 {n, }                  desde n hasta infinito          -\\d{4, }-
                                                        -32450204-
 *                      puede ser 0 o mas veces         \\w\\s*\\w
                                                        a b, Ó ab, Ó a     b
 ?                      1 Ó 0 veces                     casas?                                                
 """