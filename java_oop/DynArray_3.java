// Тесты

public class DynArrayTest {

    @org.junit.jupiter.api.Test
    public void testInsert_noResize_capacitySame() {
        DynArray<Integer> a = new DynArray<>(Integer.class);
        a.append(1);
        a.append(2);
        a.append(4);

        int capBefore = a.capacity;

        a.insert(3, 2);

        org.junit.jupiter.api.Assertions.assertEquals(4, a.count);
        org.junit.jupiter.api.Assertions.assertEquals(capBefore, a.capacity);
        org.junit.jupiter.api.Assertions.assertEquals(1, a.getItem(0));
        org.junit.jupiter.api.Assertions.assertEquals(2, a.getItem(1));
        org.junit.jupiter.api.Assertions.assertEquals(3, a.getItem(2));
        org.junit.jupiter.api.Assertions.assertEquals(4, a.getItem(3));
    }

    @org.junit.jupiter.api.Test
    public void testInsert_withResize_capacityDoubles() {
        DynArray<Integer> a = new DynArray<>(Integer.class);

        for (int i = 0; i < 16; i++) a.append(i);

        org.junit.jupiter.api.Assertions.assertEquals(16, a.count);
        org.junit.jupiter.api.Assertions.assertEquals(16, a.capacity);

        a.insert(999, 8);

        org.junit.jupiter.api.Assertions.assertEquals(17, a.count);
        org.junit.jupiter.api.Assertions.assertEquals(32, a.capacity);
        org.junit.jupiter.api.Assertions.assertEquals(999, a.getItem(8));
        org.junit.jupiter.api.Assertions.assertEquals(8, a.getItem(9));
    }

    @org.junit.jupiter.api.Test
    public void testInsert_invalidIndex_throws() {
        DynArray<Integer> a = new DynArray<>(Integer.class);
        a.append(10);

        org.junit.jupiter.api.Assertions.assertThrows(
                IndexOutOfBoundsException.class,
                () -> a.insert(1, -1)
        );

        org.junit.jupiter.api.Assertions.assertThrows(
                IndexOutOfBoundsException.class,
                () -> a.insert(1, 2) // count=1, разрешены только 0..1
        );
    }


    @org.junit.jupiter.api.Test
    public void testRemove_noResize_capacitySame() {
        DynArray<Integer> a = new DynArray<>(Integer.class);
        for (int i = 0; i < 10; i++) a.append(i); // capacity=16

        org.junit.jupiter.api.Assertions.assertEquals(16, a.capacity);

        a.remove(5);

        org.junit.jupiter.api.Assertions.assertEquals(9, a.count);
        org.junit.jupiter.api.Assertions.assertEquals(16, a.capacity);
        org.junit.jupiter.api.Assertions.assertEquals(6, a.getItem(5));
    }

    @org.junit.jupiter.api.Test
    public void testRemove_withResize_capacityShrinksBy1_5() {
        DynArray<Integer> a = new DynArray<>(Integer.class);

        for (int i = 0; i < 17; i++) a.append(i);
        org.junit.jupiter.api.Assertions.assertEquals(32, a.capacity);
        org.junit.jupiter.api.Assertions.assertEquals(17, a.count);

        a.remove(0);
        org.junit.jupiter.api.Assertions.assertEquals(32, a.capacity);

        a.remove(0);
        org.junit.jupiter.api.Assertions.assertEquals(21, a.capacity);
        org.junit.jupiter.api.Assertions.assertEquals(15, a.count);

        org.junit.jupiter.api.Assertions.assertEquals(2, a.getItem(0)); // удалили 0 и 1
        org.junit.jupiter.api.Assertions.assertEquals(16, a.getItem(14));
    }

    @org.junit.jupiter.api.Test
    public void testRemove_invalidIndex_throws() {
        DynArray<Integer> a = new DynArray<>(Integer.class);
        a.append(1);

        org.junit.jupiter.api.Assertions.assertThrows(
                IndexOutOfBoundsException.class,
                () -> a.remove(-1)
        );

        org.junit.jupiter.api.Assertions.assertThrows(
                IndexOutOfBoundsException.class,
                () -> a.remove(1) // count=1, последний индекс 0
        );
    }
}
