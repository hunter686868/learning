// Композиция - инвентарь с предметами у юнита
class Inventory {
    private Item[] items;
    private int index = 0;

    public Inventory(int capacity) {
        items = new Item[capacity];
    }

    public void addItem(Item item) {
        if (index >= items.length) {
            System.out.println("Инвентарь переполнен");
            return;
        }
        items[index++] = item;
        System.out.println(item.getName() + " добавлен в инвентарь");
    }

    public void useItem(int slot, Unit unit) {
        if (slot < 0 || slot >= index) {
            System.out.println("Пустой слот");
            return;
        }
        items[slot].use(unit);
    }
}

class Unit {
    private String name;
    private int health;
    private int maxHealth;
    private int mana;
    private int cost;
    private String[] abilities;
    private Weapon weapon;
    private Inventory inventory;

    public Unit(String name, int health, int mana, int cost, String[] abilities) {
        this.name = name;
        this.health = health;
        this.maxHealth = health;
        this.mana = mana;
        this.cost = cost;
        this.abilities = abilities;
        this.inventory = new Inventory(10);
    }

    public Inventory getInventory() {
        return inventory;
    }

//Композиция - персонал в здании
class Headquarters {
    private String name;
    private Unit[] personnel;
    private int index = 0;

    public Headquarters(String name, int capacity) {
        this.name = name;
        this.personnel = new Unit[capacity];
    }

    public void addUnit(Unit unit) {
        if (index >= personnel.length) {
            System.out.println("В штабе больше нет мест");
            return;
        }
        personnel[index++] = unit;
        System.out.println(unit.getName() + " назначен в " + name);
    }

    public void printPersonnel() {
        System.out.println("Персонал " + name + ":");
        for (int i = 0; i < index; i++) {
            System.out.println("- " + personnel[i].getName());
        }
    }
}

///
Пример с двумя видами полиморфизма:
    Полиморфизм подтипов - делаем разную реализацию для одного метода(функции) в зависимости от типа.
    Параметрический полиморфизм - один метод(функция) работает одинаково, вне зависимости от типа данных.
///

class Animal {
    void foo() {
    }
}

    class Cat extends Animal {
        void foo() {
            System.out.println("Кошка мурлычет");
        }
    }

    class Bird extends Animal {
        void foo() {
            System.out.println("Птица поет");
        }
    }

    public class Main {

        // Наполняем список 500 объектами
        static void fillAnimals(Animal[] animals) {
            for (int i = 0; i < animals.length; i++) {
                if (Math.random() < 0.5) {
                    animals[i] = new Cat();
                } else {
                    animals[i] = new Bird();
                }
            }
        }

        public static void main(String[] args) {

            Animal[] animals = new Animal[500]; // вместо List используем простой массив

            fillAnimals(animals);

            for (int i = 0; i < animals.length; i++) {
                animals[i].foo();
            }
        }
    }

    // Вывод корректно работает, т.к. у нас работает полиморфизм.

