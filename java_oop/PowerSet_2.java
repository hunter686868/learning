import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
// 4.* Добавьте метод, реализующий декартово произведение множеств.
// Возвращайте множество из пар соответствий.
class PairSet {
    private List<String> pairs;

    public PairSet() {
        pairs = new ArrayList<>();
    }

    public void put(String left, String right) {
        String pair = "(" + left + ", " + right + ")";
        if (!pairs.contains(pair)) {
            pairs.add(pair);
        }
    }
}

// 5.* Напишите функцию, которая находит пересечение любых
// трёх и более множеств (принимает количество множеств >= 3 в качестве списка).
class PowerSetStar {

    public static PairSet cartesianProduct(PowerSet a, PowerSet b) {
        PairSet result = new PairSet();

        for (String left : getValues(a)) {
            for (String right : getValues(b)) {
                result.put(left, right);
            }
        }
        return result;
    }

    public static PowerSet intersectionMany(List<PowerSet> sets) {
        PowerSet result = new PowerSet();

        if (sets == null || sets.size() < 3) {
            return result;
        }

        PowerSet first = sets.get(0);

        for (String value : getValues(first)) {
            boolean existsInAll = true;

            for (int i = 1; i < sets.size(); i++) {
                if (!sets.get(i).get(value)) {
                    existsInAll = false;
                    break;
                }
            }

            if (existsInAll) {
                result.put(value);
            }
        }

        return result;
    }

    private static List<String> getValues(PowerSet set) {
        try {
            java.lang.reflect.Field field = PowerSet.class.getDeclaredField("set");
            field.setAccessible(true);
            return (List<String>) field.get(set);
        } catch (Exception e) {
            return new ArrayList<>();
        }
    }
}
// 6.* Реализуйте мульти-множество (Bag), в котором каждый
// элемент может присутствовать несколько раз.
// Добавьте методы добавления элементов, удаления
// одного экземпляра элемента и получения списка всех
// элементов с их частотами (сколько раз встречаются).
class Bag {
    private Map<String, Integer> items;

    public Bag() {
        items = new HashMap<>();
    }

    public void add(String value) {
        if (items.containsKey(value)) {
            items.put(value, items.get(value) + 1);
        } else {
            items.put(value, 1);
        }
    }

    public boolean removeOne(String value) {
        if (!items.containsKey(value)) {
            return false;
        }

        int count = items.get(value);

        if (count == 1) {
            items.remove(value);
        } else {
            items.put(value, count - 1);
        }

        return true;
    }

    public Map<String, Integer> getFrequencies() {
        return items;
    }
}

