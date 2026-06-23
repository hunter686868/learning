import org.junit.jupiter.api.Test;
import java.util.*;
import static org.junit.jupiter.api.Assertions.*;

public class LinkedList2Test {

    private LinkedList2 listOf(int... values) {
        LinkedList2 ll = new LinkedList2();
        for (int v : values) ll.addInTail(new Node(v));
        return ll;
    }

    private List<Integer> toForward(LinkedList2 ll) {
        List<Integer> res = new ArrayList<>();
        Node cur = ll.head;
        while (cur != null) {
            res.add(cur.value);
            cur = cur.next;
        }
        return res;
    }

    private List<Integer> toBackward(LinkedList2 ll) {
        List<Integer> res = new ArrayList<>();
        Node cur = ll.tail;
        while (cur != null) {
            res.add(cur.value);
            cur = cur.prev;
        }
        return res;
    }

    private void assertIntegrity(LinkedList2 ll) {
        if (ll.head == null || ll.tail == null) {
            assertNull(ll.head);
            assertNull(ll.tail);
            return;
        }

        assertNull(ll.head.prev);
        assertNull(ll.tail.next);

        Node cur = ll.head;
        Node prev = null;
        int guard = 0;

        while (cur != null) {
            assertEquals(prev, cur.prev);
            if (cur.next != null) assertEquals(cur, cur.next.prev);
            prev = cur;
            cur = cur.next;

            guard++;
            assertTrue(guard < 10_000, "Похоже на цикл в списке");
        }

        assertEquals(prev, ll.tail);
    }

    @Test
    public void testFind_empty() {
        LinkedList2 ll = new LinkedList2();
        assertNull(ll.find(10));
        assertIntegrity(ll);
    }

    @Test
    public void testFind_singleAndMany() {
        LinkedList2 ll1 = listOf(5);
        assertNotNull(ll1.find(5));
        assertNull(ll1.find(99));
        assertIntegrity(ll1);

        LinkedList2 ll2 = listOf(1, 2, 3, 2, 5);
        assertEquals(2, ll2.find(2).value);
        assertSame(ll2.head.next, ll2.find(2)); // первый найденный "2"
        assertIntegrity(ll2);
    }

    @Test
    public void testFindAll() {
        LinkedList2 ll = listOf(1, 2, 3, 2, 2, 5);
        ArrayList<Node> found = ll.findAll(2);
        assertEquals(3, found.size());
        assertEquals(Arrays.asList(1,2,3,2,2,5), toForward(ll)); // список не меняется
        assertIntegrity(ll);
    }

    @Test
    public void testRemove_emptyAndAbsent() {
        LinkedList2 ll = new LinkedList2();
        assertFalse(ll.remove(1));
        assertIntegrity(ll);

        LinkedList2 ll2 = listOf(1,2,3);
        assertFalse(ll2.remove(99));
        assertEquals(Arrays.asList(1,2,3), toForward(ll2));
        assertIntegrity(ll2);
    }

    @Test
    public void testRemove_single() {
        LinkedList2 ll = listOf(7);
        assertTrue(ll.remove(7));
        assertNull(ll.head);
        assertNull(ll.tail);
        assertEquals(0, ll.count());
        assertIntegrity(ll);
    }

    @Test
    public void testRemove_head() {
        LinkedList2 ll = listOf(1,2,3);
        assertTrue(ll.remove(1));
        assertEquals(Arrays.asList(2,3), toForward(ll));
        assertEquals(Arrays.asList(3,2), toBackward(ll));
        assertEquals(2, ll.head.value);
        assertEquals(3, ll.tail.value);
        assertIntegrity(ll);
    }

    @Test
    public void testRemove_tail() {
        LinkedList2 ll = listOf(1,2,3);
        assertTrue(ll.remove(3));
        assertEquals(Arrays.asList(1,2), toForward(ll));
        assertEquals(Arrays.asList(2,1), toBackward(ll));
        assertEquals(1, ll.head.value);
        assertEquals(2, ll.tail.value);
        assertIntegrity(ll);
    }

    @Test
    public void testRemove_middle() {
        LinkedList2 ll = listOf(1,2,3,4);
        assertTrue(ll.remove(3));
        assertEquals(Arrays.asList(1,2,4), toForward(ll));
        assertEquals(Arrays.asList(4,2,1), toBackward(ll));
        assertIntegrity(ll);
    }

    @Test
    public void testRemoveAll() {
        LinkedList2 ll = listOf(2,1,2,3,2,4,2);
        ll.removeAll(2);
        assertEquals(Arrays.asList(1,3,4), toForward(ll));
        assertEquals(Arrays.asList(4,3,1), toBackward(ll));
        assertIntegrity(ll);

        LinkedList2 ll2 = listOf(9,9,9);
        ll2.removeAll(9);
        assertNull(ll2.head);
        assertNull(ll2.tail);
        assertEquals(0, ll2.count());
        assertIntegrity(ll2);
    }

    @Test
    public void testClear() {
        LinkedList2 ll = listOf(1,2,3);
        ll.clear();
        assertNull(ll.head);
        assertNull(ll.tail);
        assertEquals(0, ll.count());
        assertIntegrity(ll);
    }

    @Test
    public void testCount() {
        LinkedList2 ll = new LinkedList2();
        assertEquals(0, ll.count());

        LinkedList2 ll2 = listOf(1,2,3,4);
        assertEquals(4, ll2.count());
        ll2.remove(2);
        assertEquals(3, ll2.count());
        assertIntegrity(ll2);
    }

    @Test
    public void testInsertAfter_nullIntoEmpty() {
        LinkedList2 ll = new LinkedList2();
        Node n = new Node(10);
        ll.insertAfter(null, n);
        assertEquals(Arrays.asList(10), toForward(ll));
        assertSame(ll.head, ll.tail);
        assertIntegrity(ll);
    }

    @Test
    public void testInsertAfter_nullIntoNonEmpty_becomesHead() {
        LinkedList2 ll = listOf(1,2,3);
        Node n = new Node(99);
        ll.insertAfter(null, n);
        assertEquals(Arrays.asList(99,1,2,3), toForward(ll));
        assertEquals(Arrays.asList(3,2,1,99), toBackward(ll));
        assertEquals(99, ll.head.value);
        assertEquals(3, ll.tail.value);
        assertIntegrity(ll);
    }

    @Test
    public void testInsertAfter_middle() {
        LinkedList2 ll = listOf(1,2,4);
        Node after = ll.find(2);
        Node ins = new Node(3);
        ll.insertAfter(after, ins);
        assertEquals(Arrays.asList(1,2,3,4), toForward(ll));
        assertEquals(Arrays.asList(4,3,2,1), toBackward(ll));
        assertIntegrity(ll);
    }

    @Test
    public void testInsertAfter_tail() {
        LinkedList2 ll = listOf(1,2,3);
        Node ins = new Node(4);
        ll.insertAfter(ll.tail, ins);
        assertEquals(Arrays.asList(1,2,3,4), toForward(ll));
        assertEquals(4, ll.tail.value);
        assertIntegrity(ll);
    }
}
