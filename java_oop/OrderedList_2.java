public class OrderedList<T>
{
    // Метод удаления всех дубликатов из упорядоченного списка
    public static <T> void removeAllDuplicates(OrderedList<T> list)
    {
        if (list.head == null) return;

        Node<T> cur = list.head;
        while (cur != null && cur.next != null)
        {
            if (list.compare(cur.value, cur.next.value) == 0)
            {
                Node<T> del = cur.next;
                Node<T> nx = del.next;

                cur.next = nx;
                if (nx != null) nx.prev = cur;
                else list.tail = cur;
            }
            else
            {
                cur = cur.next;
            }
        }
    }

    // Алгоритм слияния двух упорядоченных списков в один, сохраняя порядок элементов
    public static <T> OrderedList<T> merge(OrderedList<T> a, OrderedList<T> b, boolean asc)
    {
        OrderedList<T> r = new OrderedList<T>(asc);

        Node<T> pa = a.head;
        Node<T> pb = b.head;

        while (pa != null && pb != null)
        {
            int cmp = r.compare(pa.value, pb.value);
            boolean takeA = asc ? (cmp <= 0) : (cmp >= 0);

            if (takeA)
            {
                r.add(pa.value);
                pa = pa.next;
            }
            else
            {
                r.add(pb.value);
                pb = pb.next;
            }
        }

        while (pa != null)
        {
            r.add(pa.value);
            pa = pa.next;
        }

        while (pb != null)
        {
            r.add(pb.value);
            pb = pb.next;
        }

        return r;
    }

    // Метод проверки наличия заданного упорядоченного под-списка
    public static <T> boolean containsSublist(OrderedList<T> list, OrderedList<T> sub)
    {
        if (sub.head == null) return true;
        if (list.head == null) return false;

        Node<T> start = list.head;

        while (start != null)
        {
            Node<T> a = start;
            Node<T> b = sub.head;

            while (a != null && b != null && list.compare(a.value, b.value) == 0)
            {
                a = a.next;
                b = b.next;
            }

            if (b == null) return true;

            start = start.next;
        }

        return false;
    }

    // Метод, который находит наиболее часто встречающееся значение в списке
    public static <T> T mostFrequent(OrderedList<T> list)
    {
        if (list.head == null) return null;

        Node<T> cur = list.head;
        T bestVal = cur.value;
        int bestCnt = 1;

        T runVal = cur.value;
        int runCnt = 0;

        while (cur != null)
        {
            if (list.compare(cur.value, runVal) == 0)
            {
                runCnt++;
            }
            else
            {
                if (runCnt > bestCnt)
                {
                    bestCnt = runCnt;
                    bestVal = runVal;
                }
                runVal = cur.value;
                runCnt = 1;
            }
            cur = cur.next;
        }

        if (runCnt > bestCnt)
        {
            bestCnt = runCnt;
            bestVal = runVal;
        }

        return bestVal;
    }

    // Возможность найти индекс элемента (параметр) в списке
    public static class OrderedArrayIndex<T>
    {
        private java.util.ArrayList<T> a = new java.util.ArrayList<T>();
        private boolean asc;

        public OrderedArrayIndex(boolean asc)
        {
            this.asc = asc;
        }

        public int compare(T v1, T v2)
        {
            if (v1 == null && v2 == null) return 0;
            if (v1 == null) return -1;
            if (v2 == null) return 1;

            if (v1 instanceof Number && v2 instanceof Number)
            {
                double x = ((Number) v1).doubleValue();
                double y = ((Number) v2).doubleValue();
                return (x < y) ? -1 : ((x > y) ? 1 : 0);
            }

            if (v1 instanceof String && v2 instanceof String)
            {
                String x = ((String) v1).trim();
                String y = ((String) v2).trim();
                int c = x.compareTo(y);
                return (c < 0) ? -1 : ((c > 0) ? 1 : 0);
            }

            if (v1 instanceof Comparable && v2 instanceof Comparable)
            {
                @SuppressWarnings("unchecked")
                int c = ((Comparable) v1).compareTo(v2);
                return (c < 0) ? -1 : ((c > 0) ? 1 : 0);
            }

            return 0;
        }

        public void add(T value)
        {
            int l = 0;
            int r = a.size();
            while (l < r)
            {
                int m = (l + r) >>> 1;
                int cmp = compare(value, a.get(m));
                boolean goLeft = asc ? (cmp <= 0) : (cmp >= 0);
                if (goLeft) r = m;
                else l = m + 1;
            }
            a.add(l, value);
        }

        public int indexOf(T value)
        {
            int l = 0;
            int r = a.size() - 1;
            while (l <= r)
            {
                int m = (l + r) >>> 1;
                int cmp = compare(a.get(m), value);
                if (cmp == 0) return m;

                if (asc)
                {
                    if (cmp < 0) l = m + 1;
                    else r = m - 1;
                }
                else
                {
                    if (cmp > 0) l = m + 1;
                    else r = m - 1;
                }
            }
            return -1;
        }

        public int size()
        {
            return a.size();
        }
    }
}