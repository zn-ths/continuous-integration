import src.string_ops as ops

TEST_WORDS = ["zaid", "alibAbA", "rOgeR_theBunnY", "annA Kaborza alIrO"]


class TestStringOps:
    def test_remove_vowels(self):
        for word in TEST_WORDS:
            modified_word = ops.remove_vowels(word)
            assert word != modified_word
            assert len(word) != len(modified_word)

    def test_reverse_string(self):
        for word in TEST_WORDS:
            reversed_word = ops.reverse_string(word)
            assert word != reversed_word
            assert len(word) == len(reversed_word)

    def test_convert_to_robbers_lang(self):
        for word in TEST_WORDS:
            converted_word = ops.convert_to_robbers_lang(word)
            assert word != converted_word
            assert len(word) != len(converted_word)
