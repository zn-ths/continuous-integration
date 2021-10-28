import src.string_ops as ops

TEST_WORDS = ["zaid", "alibAbA", "rOgeR_theBunnY", "annA Kaborza alIrO"]


class TestStringOps:
    def test_remove_vowels(self):
        for word in TEST_WORDS:
            assert word != ops.remove_vowels(word)
            assert len(word) != len(ops.remove_vowels(word))

    def test_reverse_string(self):
        for word in TEST_WORDS:
            assert word != ops.reverse_string(word)
            assert len(word) == len(ops.reverse_string(word))
