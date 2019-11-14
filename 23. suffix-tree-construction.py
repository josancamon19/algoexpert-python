# Do not edit the class below except for the
# populateSuffixTrieFrom and contains methods.
# Feel free to add new properties and methods
# to the class.

# AlgoExpert solution is too inefficient
# I think this one is better
class SuffixTrie:
    def __init__(self, string):
        self.root = {}
        self.endSymbol = "*"
        self.populateSuffixTrieFrom(string)

    def populateSuffixTrieFrom(self, string):
        # Write your code here.
        node = self.root
        for char in string:
            if char not in node:
                node[char] = {}
            node = node[char]
        node["*"] = True

    def contains(self, string):
        # Write your code here.
        node = self.root
        for char in string:
            if char not in node:
                return False
            node = node[char]

        # print(node)
        return '*' in node

    def get_prefix_node(self, prefix):
        # Write your code here.
        node = self.root
        for char in prefix:
            if char not in node:
                return None
            node = node[char]

        return node

    def get_suffixes(self, prefix):
        node = self.get_prefix_node(prefix)
        return suffixes_from_node(node, '')


def suffixes_from_node(node, previous):
    results = []
    for key, child in node.items():
        if type(child) == dict:
            if '*' in child:
                results.append(previous + key)
            results += suffixes_from_node(child, previous + key)
    return results


if __name__ == '__main__':
    test1 = SuffixTrie('test')
    test1.populateSuffixTrieFrom('test2')
    test1.populateSuffixTrieFrom('testsito')
    print(test1.get_suffixes('te'))
