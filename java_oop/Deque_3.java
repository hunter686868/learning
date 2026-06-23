public class DequeTest {
    private static void assertTrue(boolean cond, String msg) {
        if (!cond) throw new RuntimeException("ASSERT FAIL: " + msg);
    }

    private static void assertEqInt(int a, int b, String msg) {
        if (a != b) throw new RuntimeException("ASSERT FAIL: " + msg + " (got " + a + ", want " + b + ")");
    }

    private static void assertEqObj(Object a, Object b, String msg) {
        if (a == null && b == null) return;
        if (a == null || b == null) throw new RuntimeException("ASSERT FAIL: " + msg + " (one is null)");
        if (!a.equals(b)) throw new RuntimeException("ASSERT FAIL: " + msg + " (got " + a + ", want " + b + ")");
    }

    public static void main(String[] args) {
        Deque<String> d = new Deque<String>();

        assertEqInt(d.size(), 0, "empty size");
        assertTrue(d.removeFront() == null, "removeFront empty => null");
        assertTrue(d.removeTail() == null, "removeTail empty => null");
        assertEqInt(d.size(), 0, "empty size after removes");

        d.addFront("A");
        assertEqInt(d.size(), 1, "size after addFront");
        assertEqObj(d.removeFront(), "A", "removeFront returns added");
        assertEqInt(d.size(), 0, "size after removeFront");

        d.addTail("B");
        assertEqInt(d.size(), 1, "size after addTail");
        assertEqObj(d.removeTail(), "B", "removeTail returns added");
        assertEqInt(d.size(), 0, "size after removeTail");

        d.addFront("f1");
        assertEqInt(d.size(), 1, "size f1");
        d.addTail("t1");
        assertEqInt(d.size(), 2, "size t1");
        d.addFront("f2");
        assertEqInt(d.size(), 3, "size f2");
        d.addTail("t2");
        assertEqInt(d.size(), 4, "size t2");

        assertEqObj(d.removeFront(), "f2", "removeFront gets f2");
        assertEqInt(d.size(), 3, "size after removeFront f2");
        assertEqObj(d.removeTail(), "t2", "removeTail gets t2");
        assertEqInt(d.size(), 2, "size after removeTail t2");
        assertEqObj(d.removeFront(), "f1", "removeFront gets f1");
        assertEqInt(d.size(), 1, "size after removeFront f1");
        assertEqObj(d.removeTail(), "t1", "removeTail gets t1");
        assertEqInt(d.size(), 0, "size after removeTail t1");

        assertTrue(d.removeFront() == null, "removeFront empty again");
        assertTrue(d.removeTail() == null, "removeTail empty again");

    }
}
