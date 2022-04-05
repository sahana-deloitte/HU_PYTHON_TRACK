class StringClass:
    def __init__(self, name):
        self.name = name

    def list(self):
        return (list(self.name))

    def length(self):
        return len(self.name)


class PairsPossible(StringClass):
    def pair(self, test_list):
        res = [(num, object1) for idx, num in enumerate(test_list) for object1 in test_list[idx + 1:]]
        print(res)


class SearchCommonElements(StringClass):
    def common(self, str, name):
        a = list(set(str) & set(name))
        print(a)


class EqualSumPairs:
    def pair2(self, test_list):
        res = [sum((int(num), int(object1))) for idx, num in enumerate(test_list) for object1 in test_list[idx + 1:]]
        print(set(res))
        print(len(set(res)))


num = input("Enter a string :")
object1 = StringClass(num)
print(object1.list())
print(object1.length())
h = object1.list()
object2 = PairsPossible(object1)
object2.pair(h)
st = input("Enter string to compare ")
object3 = SearchCommonElements(object1)
object3.common(num, str)
object4 = EqualSumPairs()
object4.pair2(h)




