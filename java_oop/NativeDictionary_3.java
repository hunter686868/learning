public class NativeDictionaryTest
{
    public static void main(String[] args)
    {
        NativeDictionary<Integer> dict = new NativeDictionary<>(17, Integer.class);

        dict.put("one", 1);
        if (dict.get("one") != null && dict.get("one") == 1) {
            System.out.println("put new key OK");
        } else {
            System.out.println("put new key FAIL");
        }

        dict.put("one", 10);
        if (dict.get("one") != null && dict.get("one") == 10) {
            System.out.println("put existing key OK");
        } else {
            System.out.println("put existing key FAIL");
        }

        if (dict.isKey("one")) {
            System.out.println("isKey existing OK");
        } else {
            System.out.println("isKey existing FAIL");
        }

        if (!dict.isKey("two")) {
            System.out.println("isKey missing OK");
        } else {
            System.out.println("isKey missing FAIL");
        }

        Integer value1 = dict.get("one");
        if (value1 != null && value1 == 10) {
            System.out.println("get existing OK");
        } else {
            System.out.println("get existing FAIL");
        }

        Integer value2 = dict.get("two");
        if (value2 == null) {
            System.out.println("get missing OK");
        } else {
            System.out.println("get missing FAIL");
        }

        dict.put("apple", 100);
        dict.put("banana", 200);
        dict.put("orange", 300);

        if (dict.get("apple") != null && dict.get("apple") == 100 &&
                dict.get("banana") != null && dict.get("banana") == 200 &&
                dict.get("orange") != null && dict.get("orange") == 300) {
            System.out.println("many keys OK");
        } else {
            System.out.println("many keys FAIL");
        }
    }
}