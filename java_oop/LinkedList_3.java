// Тесты

import org.junit.Test;
import static org.junit.Assert.*;

public class LinkedListTest {

    private LinkedList listOf(int... a) {
        LinkedList l = new LinkedList();
        for (int x : a) l.addInTail(new Node(x));
        return l;
    }

    private int[] toArray(LinkedList l) {
        int[] r = new int[l.count()];
        int i = 0;
        Node n = l.head;
        while (n != null) {
            r[i++] = n.value;
            n = n.next;
        }
        return r;
    }

    @Test
    public void testCountEmptyOneMany() {
        assertEquals(0, new LinkedList().count());
        assertEquals(1, listOf(10).count());
        assertEquals(5, listOf(1,2,3,4,5).count());
    }

    @Test
    public void testFind() {
        LinkedList l = listOf(12, 55, 128);
        assertNotNull(l.find(55));
        assertNull(l.find(999));
        assertEquals(12, l.find(12).value);
    }

    @Test
    public void testFindAll() {
        LinkedList l = listOf(1, 2, 2, 3, 2);
        assertEquals(3, l.findAll(2).size());
        assertEquals(0, l.findAll(999).size());
    }

    @Test
    public void testRemoveEmpty() {
        LinkedList l = new LinkedList();
        assertFalse(l.remove(1));
        assertNull(l.head);
        assertNull(l.tail);
    }

    @Test
    public void testRemoveHead() {
        LinkedList l = listOf(7, 8, 9);
        assertTrue(l.remove(7));
        assertArrayEquals(new int[]{8,9}, toArray(l));
        assertEquals(8, l.head.value);
        assertEquals(9, l.tail.value);
    }

    @Test
    public void testRemoveTail() {
        LinkedList l = listOf(7, 8, 9);
        assertTrue(l.remove(9));
        assertArrayEquals(new int[]{7,8}, toArray(l));
        assertEquals(8, l.tail.value);
        assertNull(l.tail.next);
    }

    @Test
    public void testRemoveMiddle() {
        LinkedList l = listOf(7, 8, 9);
        assertTrue(l.remove(8));
        assertArrayEquals(new int[]{7,9}, toArray(l));
        assertEquals(7, l.head.value);
        assertEquals(9, l.tail.value);
    }

    @Test
    public void testRemoveOnlyElementMakesEmpty() {
        LinkedList l = listOf(42);
        assertTrue(l.remove(42));
        assertNull(l.head);
        assertNull(l.tail);
        assertEquals(0, l.count());
    }

    @Test
    public void testRemoveAll() {
        LinkedList l = listOf(1, 2, 2, 3, 2, 4);
        l.removeAll(2);
        assertArrayEquals(new int[]{1,3,4}, toArray(l));
        assertEquals(1, l.head.value);
        assertEquals(4, l.tail.value);
    }

    @Test
    public void testRemoveAllAllElements() {
        LinkedList l = listOf(5,5,5);
        l.removeAll(5);
        assertNull(l.head);
        assertNull(l.tail);
        assertEquals(0, l.count());
    }

    @Test
    public void testClear() {
        LinkedList l = listOf(1,2,3);
        l.clear();
        assertNull(l.head);
        assertNull(l.tail);
        assertEquals(0, l.count());
    }

    @Test
    public void testInsertAfterNullIntoEmpty() {
        LinkedList l = new LinkedList();
        l.insertAfter(null, new Node(10));
        assertArrayEquals(new int[]{10}, toArray(l));
        assertEquals(10, l.head.value);
        assertEquals(10, l.tail.value);
    }

    @Test
    public void testInsertAfterNullIntoNonEmpty() {
        LinkedList l = listOf(2,3);
        l.insertAfter(null, new Node(1));
        assertArrayEquals(new int[]{1,2,3}, toArray(l));
        assertEquals(1, l.head.value);
    }

    @Test
    public void testInsertAfterMiddle() {
        LinkedList l = listOf(1,2,4);
        Node after = l.find(2);
        l.insertAfter(after, new Node(3));
        assertArrayEquals(new int[]{1,2,3,4}, toArray(l));
        assertEquals(4, l.tail.value);
    }

    @Test
    public void testInsertAfterTailUpdatesTail() {
        LinkedList l = listOf(1,2);
        l.insertAfter(l.tail, new Node(3));
        assertArrayEquals(new int[]{1,2,3}, toArray(l));
        assertEquals(3, l.tail.value);
        assertNull(l.tail.next);
    }

    @Test
    public void testSumListsEqualLength() {
        LinkedList a = listOf(1,2,3);
        LinkedList b = listOf(10,20,30);
        LinkedList s = LinkedList.sumLists(a,b);
        assertNotNull(s);
        assertArrayEquals(new int[]{11,22,33}, toArray(s));
    }

    @Test
    public void testSumListsNotEqualLength() {
        LinkedList a = listOf(1,2,3);
        LinkedList b = listOf(10,20);
        assertNull(LinkedList.sumLists(a,b));
    }
}
