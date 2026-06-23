public class PowerSetTest {

    public static void main(String[] args) {
        testPut();
        testRemove();
        testIntersection();
        testUnion();
        testDifference();
        testIsSubset();
        testEquals();
        testPerformance();
    }

    public static void testPut() {
        PowerSet set = new PowerSet();

        set.put("a");
        set.put("a");

        if (!(set.size() == 1 && set.get("a"))) {
            System.out.println("put FAIL");
        }
    }

    public static void testRemove() {
        PowerSet set = new PowerSet();
        set.put("a");
        boolean removed = set.remove("a");

        if (!(removed && !set.get("a") && set.size() == 0)) {
            System.out.println("remove FAIL");
        }
    }

    public static void testIntersection() {
        PowerSet a = new PowerSet();
        PowerSet b = new PowerSet();

        a.put("a");
        a.put("b");
        b.put("b");
        b.put("c");

        PowerSet result1 = a.intersection(b);

        PowerSet c = new PowerSet();
        PowerSet d = new PowerSet();
        c.put("x");
        d.put("y");

        PowerSet result2 = c.intersection(d);

        if (!(result1.size() == 1 && result1.get("b") && result2.size() == 0)) {
            System.out.println("intersection FAIL");
        }
    }

    public static void testUnion() {
        PowerSet a = new PowerSet();
        PowerSet b = new PowerSet();
        PowerSet empty = new PowerSet();

        a.put("a");
        b.put("b");

        PowerSet result1 = a.union(b);
        PowerSet result2 = a.union(empty);

        if (!(result1.size() == 2 && result1.get("a") && result1.get("b")
                && result2.size() == 1 && result2.get("a"))) {
            System.out.println("union FAIL");
        }
    }

    public static void testDifference() {
        PowerSet a = new PowerSet();
        PowerSet b = new PowerSet();

        a.put("a");
        a.put("b");
        b.put("b");

        PowerSet result1 = a.difference(b);
        PowerSet result2 = b.difference(a);

        if (!(result1.size() == 1 && result1.get("a") && result2.size() == 0)) {
            System.out.println("difference FAIL");
        }
    }

    public static void testIsSubset() {
        PowerSet a = new PowerSet();
        PowerSet b = new PowerSet();
        PowerSet c = new PowerSet();

        a.put("a");
        a.put("b");
        a.put("c");

        b.put("a");
        b.put("b");

        c.put("a");
        c.put("b");
        c.put("d");

        boolean case1 = a.isSubset(b);
        boolean case2 = b.isSubset(a);
        boolean case3 = a.isSubset(c);

        if (!(case1 && !case2 && !case3)) {
            System.out.println("isSubset FAIL");
        }
    }

    public static void testEquals() {
        PowerSet a = new PowerSet();
        PowerSet b = new PowerSet();
        PowerSet c = new PowerSet();

        a.put("a");
        a.put("b");

        b.put("b");
        b.put("a");

        c.put("a");
        c.put("c");

        if (!(a.equals(b) && !a.equals(c))) {
            System.out.println("equals FAIL");
        }
    }

    public static void testPerformance() {
        PowerSet a = new PowerSet();
        PowerSet b = new PowerSet();

        long start = System.currentTimeMillis();

        for (int i = 0; i < 20000; i++) {
            a.put("a" + i);
            b.put("a" + i);
        }

        PowerSet result = a.intersection(b);

        long finish = System.currentTimeMillis();

        if (result.size() != 20000 || (finish - start) > 2000) {
            System.out.println("performance FAIL");
        }
    }
}