
import unittest
import prime_test
import glb


class TestPrimeNumberTest(unittest.TestCase):
    def test_basic_prime_test(self):
        primes = [2, 3, 5, 7, 11, 37, 67, 17, 43]
        for num in primes:
            self.assertTrue(prime_test.basic_prime_test(num))


class TestGeneratedNumber(unittest.TestCase):
    def test_generated_prime_umber(self):
        with open('data/primes.txt', 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), glb.TOTAL_PRIME_NUM)
            for num in map(int, lines):
                self.assertTrue(prime_test.basic_prime_test(num))

    def test_generated_non_prime_umber(self):
        with open(glb.none_prime_file_name, 'r') as f:
            lines = f.readlines()
            self.assertEqual(len(lines), glb.TOTAL_NON_PRIME_NUM)
            for num in map(int, lines):
                self.assertFalse(prime_test.basic_prime_test(num))


if __name__ == '__main__':
    unittest.main()
