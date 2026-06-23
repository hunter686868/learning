import java.util.*;

public class BloomFilter {

    // 2.* Слияние нескольких фильтров Блюма.
    public static int mergeFilters(int... filters) {
        int merged = 0;
        for (int filter : filters) {
            merged |= filter;
        }
        return merged;
    }

    public static double falsePositiveProbability(int m, int k, int insertedCount) {
        return Math.pow(1 - Math.exp(-1.0 * k * insertedCount / m), k);
    }
}

// 3.* Поддержка удаления
class CountingBloomFilter {
    public int filter_len;
    public int[] counters;

    public CountingBloomFilter(int f_len) {
        filter_len = f_len;
        counters = new int[f_len];
    }

    public int hash1(String str1) {
        int result = 0;
        for (int i = 0; i < str1.length(); i++) {
            int code = (int) str1.charAt(i);
            result = (result * 17 + code) % filter_len;
        }
        return result;
    }

    public int hash2(String str1) {
        int result = 0;
        for (int i = 0; i < str1.length(); i++) {
            int code = (int) str1.charAt(i);
            result = (result * 223 + code) % filter_len;
        }
        return result;
    }

    public void add(String str1) {
        counters[hash1(str1)]++;
        counters[hash2(str1)]++;
    }

    public boolean isValue(String str1) {
        return counters[hash1(str1)] > 0 && counters[hash2(str1)] > 0;
    }

    public void remove(String str1) {
        if (!isValue(str1)) {
            return;
        }

        int h1 = hash1(str1);
        int h2 = hash2(str1);

        if (counters[h1] > 0) {
            counters[h1]--;
        }
        if (counters[h2] > 0) {
            counters[h2]--;
        }
    }
}

// 4.* Попытка восстановить множество.
class BloomFilterRecovery {

    public static List<String> recoverCandidates(BloomFilter filter, List<String> dictionary) {
        List<String> result = new ArrayList<>();
        for (String candidate : dictionary) {
            if (filter.isValue(candidate)) {
                result.add(candidate);
            }
        }
        return result;
    }

    public static List<String> recoverCandidates(CountingBloomFilter filter, List<String> dictionary) {
        List<String> result = new ArrayList<>();
        for (String candidate : dictionary) {
            if (filter.isValue(candidate)) {
                result.add(candidate);
            }
        }
        return result;
    }
}
