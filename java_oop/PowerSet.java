import java.util.ArrayList;
import java.util.List;

public class PowerSet {

    private List<String> set;

    public PowerSet() {

        set = new ArrayList<>();
    }

    public int size() {
        // Сложность O(1)
        return set.size();
    }

    public void put(String value) {
        // Сложность O(n)
        if (!set.contains(value)) {
            set.add(value);
        }
    }

    public boolean get(String value) {
        // Сложность O(n)
        return set.contains(value);
    }

    public boolean remove(String value) {
        // Сложность O(n)
        return set.remove(value);
    }

    public PowerSet intersection(PowerSet set2) {
        // Сложность O(n * m)
        PowerSet result = new PowerSet();
        for (String value : set) {
            if (set2.get(value)) {
                result.put(value);
            }
        }
        return result;
    }

    public PowerSet union(PowerSet set2) {
        // Сложность O(n + m * (n + m))
        PowerSet result = new PowerSet();
        result.set.addAll(set);
        for (String value : set2.set) {
            result.put(value);
        }
        return result;
    }

    public PowerSet difference(PowerSet set2) {
        // Сложность O(n * m)
        PowerSet result = new PowerSet();
        for (String value : set) {
            if (!set2.get(value)) {
                result.put(value);
            }
        }
        return result;
    }

    public boolean isSubset(PowerSet set2) {
        // Сложность O(n * m)
        for (String value : set2.set) {
            if (!set.contains(value)) {
                return false;
            }
        }
        return true;
    }

    public boolean equals(PowerSet set2) {
        // Сложность O(n * m)
        if (this.size() != set2.size()) {
            return false;
        }
        return this.isSubset(set2);
    }
}

// Рефлексия по решению задания 8:
// По динамической хэш-таблице: динамическое расширение таблицы реализовано
// через перераспределение элементов при нехватке места,
// а также использовано несколько хэш-функций для уменьшения коллизий.
// По защите от ddos: реализована через статическую соль,
// что хуже рекомендованного подхода.