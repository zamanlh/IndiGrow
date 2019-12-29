from user_classes.nklandscape import *
from user_classes.fujilandscape import fuji
from random import randint
from copy import deepcopy
from backports.functools_lru_cache import lru_cache
import numpy


class nk_fuji_class:
    nklandscape = nklandscape(10, 5, numpy.random.RandomState(3))
    fujilandscape = fuji()

    def __init__(self):
        self.bitstring = randint(0, (2**self.nklandscape.n) - 1)
        self.landscape_state = 'nk'

    def __fitness__(self):
        return self.nklandscape.fitness(self.bitstring) if self.landscape_state == 'nk' \
                                                        else self.fujilandscape.fitness(self.bitstring)

    def __mutate__(self):
        bstr = binary(self.bitstring, self.nklandscape.n)[2:]
        for _ in range(1):
            bstr = list(bstr)
            flip_index = randint(0, self.nklandscape.n - 1)
            bstr[flip_index] = '0' if bstr[flip_index] == '1' else '1'
            bstr = ''.join(bstr)
        self.bitstring = int(bstr, 2)
    
    @lru_cache(maxsize=64)
    def __mutational_neighborhood__(self):
        neighborhood = []
        for i in range(self.nklandscape.n):
            neighbor = deepcopy(self)
            bstr = list(binary(neighbor.bitstring, self.nklandscape.n)[2:])
            bstr[i] = '0' if bstr[i] == '1' else '1'
            bstr = ''.join(bstr)
            neighbor.bitstring = int(bstr, 2)
            neighborhood.append(neighbor)
        return neighborhood





# b = nkclass()
# print(b.bitstring)
# print([m.bitstring for m in b.__mutational_neighborhood__()])
# b.mutate()
# print(b.bitstring)
# # c = nkclass()

# print(b.fitness(), c.fitness())