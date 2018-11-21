import sys
sys.path.append('./')
from Hash_Tables.hash_tables import HashMap

class DictADT(HashMap):

    def _iter_slot(self):
        for slot in self._table:
            if slot not in (HashMap.EMPTY, HashMap.UNUSED):
                yield slot
        
    def __setitem__(self, key, value):
        self.add(key, value)

    def __getitem__(self, key):
        if key not in self:
            raise KeyError()
        else:
            return self.valueOf(key)

    def items(self):
        for slot in self._iter_slot():
            yield (slot.key, slot.value)

    def keys(self):
        for slot in self._iter_slot():
            yield slot.key

    def values(self):
        for slot in self._iter_slot():
            yield slot.value


def test_dict_adt():
    import random
    d = DictADT()

    d['a'] = 1
    assert d['a'] == 1
    d.remove('a')

    l = list(range(30))
    random.shuffle(l)
    for i in l:
        d.add(i, i)

    for i in range(30):
        assert d.valueOf(i) == i

    assert sorted(list(d.keys())) == sorted(l)

if __name__ == '__main__':
    test_dict_adt()