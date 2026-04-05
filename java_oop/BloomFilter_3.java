public class BloomFilterTest {

    @org.junit.jupiter.api.Test
    public void testHashFunctions_knownValue() {
        BloomFilter filter = new BloomFilter(32);

        org.junit.jupiter.api.Assertions.assertEquals(13, filter.hash1("0123456789"));
        org.junit.jupiter.api.Assertions.assertEquals(5, filter.hash2("0123456789"));
    }

    @org.junit.jupiter.api.Test
    public void testAdd_valueBecomesPresent() {
        BloomFilter filter = new BloomFilter(32);

        filter.add("0123456789");

        org.junit.jupiter.api.Assertions.assertTrue(filter.isValue("0123456789"));
    }

    @org.junit.jupiter.api.Test
    public void testAdd_severalValues_allPresent() {
        BloomFilter filter = new BloomFilter(32);

        String[] values = {
                "0123456789",
                "1234567890",
                "2345678901",
                "3456789012",
                "4567890123",
                "5678901234",
                "6789012345",
                "7890123456",
                "8901234567",
                "9012345678"
        };

        for (String value : values) {
            filter.add(value);
        }

        for (String value : values) {
            org.junit.jupiter.api.Assertions.assertTrue(filter.isValue(value));
        }
    }

    @org.junit.jupiter.api.Test
    public void testEmptyFilter_valueAbsent() {
        BloomFilter filter = new BloomFilter(32);

        org.junit.jupiter.api.Assertions.assertFalse(filter.isValue("0123456789"));
    }

    @org.junit.jupiter.api.Test
    public void testAnotherValueUsuallyAbsentAfterOneInsert() {
        BloomFilter filter = new BloomFilter(32);
        filter.add("0123456789");

        org.junit.jupiter.api.Assertions.assertFalse(filter.isValue("abcdefghij"));
    }
}
