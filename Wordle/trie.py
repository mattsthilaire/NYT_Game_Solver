from typing import Dict


class TrieNode:
    def __init__(self) -> None:
        self.children: Dict[str, TrieNode] = {}
        self.is_end_of_word: bool = False


class Trie:
    def __init__(self) -> None:
        self.root: TrieNode = TrieNode()

    def insert(self, word: str) -> None:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def delete(self, word: str) -> None:
        def delete_helper(node: TrieNode, word: str, index: int) -> bool:
            if index == len(word):
                if node.is_end_of_word:
                    node.is_end_of_word = False
                    return len(node.children) == 0
                return False

            char = word[index]
            if char in node.children:
                child = node.children[char]
                should_delete_child = delete_helper(child, word, index + 1)
                if should_delete_child:
                    del node.children[char]
                    return len(node.children) == 0
            return False

        delete_helper(self.root, word, 0)

    def search(self, word: str) -> bool:
        node: TrieNode = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end_of_word

    def starts_with(self, prefix: str) -> bool:
        node: TrieNode = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True

    def prune(self, letter: str, position: int) -> None:
        def prune_helper(node: TrieNode, depth: int) -> None:
            if depth == position:
                if letter in node.children:
                    node.children = {letter: node.children[letter]}
                else:
                    node.children = {}
                return

            for char in list(node.children.keys()):
                prune_helper(node.children[char], depth + 1)
                if (
                    len(node.children[char].children) == 0
                    and not node.children[char].is_end_of_word
                ):
                    del node.children[char]

        prune_helper(self.root, 0)
