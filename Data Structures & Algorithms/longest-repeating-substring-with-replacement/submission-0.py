class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        conteo = {}
        izq = 0
        max_frecuencia = 0
        max_longitud = 0
        
        for der in range(len(s)):
            letra_der = s[der]
            conteo[letra_der] = conteo.get(letra_der, 0) + 1
            
            max_frecuencia = max(max_frecuencia, conteo[letra_der])
            
            if (der - izq + 1) - max_frecuencia > k:
                letra_izq = s[izq]
                conteo[letra_izq] -= 1
                izq += 1
                
            max_longitud = max(max_longitud, der - izq + 1)
            
        return max_longitud

