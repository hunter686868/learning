public class OrderedListTest {

    private static void ok(boolean cond) {
        if (!cond) throw new RuntimeException("FAIL");
    }

    private static void eq(int a, int b) {
        if (a != b) throw new RuntimeException("FAIL");
    }

    private static void eqObj(Object a, Object b) {
        if (a == null && b == null) return;
        if (a == null || b == null) throw new RuntimeException("FAIL");
        if (!a.equals(b)) throw new RuntimeException("FAIL");
    }

    public static void main(String[] args) {

        OrderedList<Integer> asc = new OrderedList<Integer>(true);

        eq(asc.count(), 0);
        ok(asc.find(1) == null);

        asc.add(5);
        eq(asc.count(), 1);
        ok(asc.find(5) != null);

        asc.add(3);
        asc.add(7);
        asc.add(7);
        asc.add(6);

        java.util.ArrayList<Node<Integer>> a1 = asc.getAll();
        eq(a1.size(), 5);
        eqObj(a1.get(0).value, 3);
        eqObj(a1.get(1).value, 5);
        eqObj(a1.get(2).value, 6);
        eqObj(a1.get(3).value, 7);
        eqObj(a1.get(4).value, 7);

        asc.delete(7);

        java.util.ArrayList<Node<Integer>> a2 = asc.getAll();
        eq(a2.size(), 4);
        eqObj(a2.get(0).value, 3);
        eqObj(a2.get(1).value, 5);
        eqObj(a2.get(2).value, 6);
        eqObj(a2.get(3).value, 7);

        ok(asc.find(2) == null);
        ok(asc.find(100) == null);

        OrderedList<Integer> desc = new OrderedList<Integer>(false);

        desc.add(5);
        desc.add(3);
        desc.add(7);
        desc.add(7);
        desc.add(6);

        java.util.ArrayList<Node<Integer>> d1 = desc.getAll();
        eq(d1.size(), 5);
        eqObj(d1.get(0).value, 7);
        eqObj(d1.get(1).value, 7);
        eqObj(d1.get(2).value, 6);
        eqObj(d1.get(3).value, 5);
        eqObj(d1.get(4).value, 3);

        desc.delete(7);

        java.util.ArrayList<Node<Integer>> d2 = desc.getAll();
        eq(d2.size(), 4);
        eqObj(d2.get(0).value, 7);
        eqObj(d2.get(1).value, 6);
        eqObj(d2.get(2).value, 5);
        eqObj(d2.get(3).value, 3);

        OrderedList<String> s = new OrderedList<String>(true);
        s.add("  b ");
        s.add("a");
        s.add(" c");
        eq(s.count(), 3);
        ok(s.find("b") != null);
        ok(s.find("d") == null);
    }
}