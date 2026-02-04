public class QueueTest {
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
        Queue<Integer> q = new Queue<Integer>();
        assertEqInt(q.size(), 0, "size empty");
        assertTrue(q.dequeue() == null, "dequeue empty returns null");

        q.enqueue(1);
        q.enqueue(2);
        q.enqueue(3);
        assertEqInt(q.size(), 3, "size after 3 enq");

        assertEqObj(q.dequeue(), 1, "fifo 1");
        assertEqObj(q.dequeue(), 2, "fifo 2");
        assertEqObj(q.dequeue(), 3, "fifo 3");
        assertEqInt(q.size(), 0, "size after draining");
        assertTrue(q.dequeue() == null, "dequeue empty after draining returns null");

        q.enqueue(10);
        q.enqueue(20);
        assertEqObj(q.dequeue(), 10, "mixed 10");
        q.enqueue(30);
        assertEqInt(q.size(), 2, "mixed size");
        assertEqObj(q.dequeue(), 20, "mixed 20");
        assertEqObj(q.dequeue(), 30, "mixed 30");
        assertEqInt(q.size(), 0, "mixed final size");

        Queue<String> qs = new Queue<String>();
        qs.enqueue(null);
        qs.enqueue("a");
        assertEqInt(qs.size(), 2, "null elem size");
        assertTrue(qs.dequeue() == null, "null elem preserved");
        assertEqObj(qs.dequeue(), "a", "after null");
        assertEqInt(qs.size(), 0, "null elem final size");

        System.out.println("OK");
    }
}
