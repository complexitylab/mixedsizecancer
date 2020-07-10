# -*- coding: utf-8 -*-

# Współczynik proliferacji lini B16:

B16_growth_rate = 1.0

# WARUNKI GRY O ŻYCIE
######################## B16 ####################################
## @ B16: 1 >>> 0: komórka UMIERA z SAMOTNOŚCI z prawdopodobieństwem:
prawdop_B16_1_0sam =  0.0
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_1_0sam_p =  0
############ i mniejsza lub równa:
B16_1_0sam_k =  2
## @ B16: 1 >>> 0: komórka umiera z PRZELUDNIENIA z prawdopodobieństwem:
prawdop_B16_1_0prz =  0.7
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_1_0prz_p = 7
############ i mniejsza lub równa:
B16_1_0prz_k =  8

## @ B16: 1 >>> 1: komórka B16 pozostaje przy ŻYCIU
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_1_1p = 3
############ i mniejsza lub równa:
B16_1_1k = 6

##@ B16: 0 >>> 0: puste pole zostaje NIEZASIEDLONA przez nową komórkę B16
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_0_0p = 0
############ i mniejsza lub równa:
B16_0_0k = 0
 
##@ B16: 0 >>> 1: puste pole zostaje ZASIEDLONE z prawdopodobieństwem (1):
prawdop_B16_0_1a = 0.2
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_0_1sam_p = 1
############ i mniejsza lub równa:
B16_0_1sam_k = 2
##@ B16: 0 >>> 1: puste pole zostaje zasiedlone z prawdopodobieństwem (2):
prawdop_B16_0_1b = 0.5 
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_0_1sam1_p = 3
############ i mniejsza lub równa:
B16_0_1sam1_k = 5
##@ B16: 0 >>> 1: puste pole zostaje zasiedlone z prawdopodobieństwem (3):
prawdop_B16_0_1c = 0.8 
############ gdy liczba komórek B16 w sąsiedztwie jest większa lub równa:
B16_0_1prz_p =6
############ i mniejsza lub równa:
B16_0_1prz_k  = 8

######################## LLC ####################################
## @ LLC: 1 >>> 0: komórka UMIERA z SAMOTNOŚCI z prawdopodobieństwem:
prawdop_LLC_1_0sam =  0.0
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_1_0sam_p =  0
############ i mniejsza lub równa:
LLC_1_0sam_k =  2
## @ LLC: 1 >>> 0: komórka umiera z PRZELUDNIENIA z prawdopodobieństwem:
prawdop_LLC_1_0prz = 0.7 
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_1_0prz_p = 7
############ i mniejsza lub równa:
LLC_1_0prz_k =  8

 ## @ LLC: 1 >>> 1: komórka LLC pozostaje przy ŻYCIU
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_1_1p = 3
############ i mniejsza lub równa:
LLC_1_1k = 6

##@ LLC: 0 >>> 0: puste pole zostaje NIEZASIEDLONA przez nową komórkę LLC
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_0_0p = 0
############ i mniejsza lub równa:
LLC_0_0k = 0

##@ LLC: 0 >>> 1: puste pole zostaje ZASIEDLONE z prawdopodobieństwem (1):
prawdop_LLC_0_1a = 0.2
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_0_1sam_p = 1
############ i mniejsza lub równa:
LLC_0_1sam_k = 3
##@ LLC: 0 >>> 1: puste pole zostaje zasiedlone z prawdopodobieństwem (2):
prawdop_LLC_0_1b = 0.5
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_0_1sam1_p = 4
############ i mniejsza lub równa:
LLC_0_1sam1_k = 6
##@ LLC: 0 >>> 1: puste pole zostaje zasiedlone z prawdopodobieństwem (3):
prawdop_LLC_0_1c = 0.8
############ gdy liczba komórek LLC w sąsiedztwie jest większa lub równa:
LLC_0_1prz_p = 7
############ i mniejsza lub równa:
LLC_0_1prz_k  = 8

