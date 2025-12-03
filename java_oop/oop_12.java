class Unit {
    String name;
    int health;
    int maxHealth;
    int mana;
    int cost;
    String[] abilities;
    Weapon weapon;

    Unit(String name, int health, int mana, int cost, String[] abilities) {
        this.name = name;
        this.health = health;
        this.maxHealth = health;
        this.mana = mana;
        this.cost = cost;
        this.abilities = abilities;
        this.weapon = null;
    }

    void attack(Unit target) {
        if (weapon == null) {
            System.out.println(name + " не может атаковать без оружия!");
            return;
        }
        int damage = weapon.damage;
        target.takeDamage(damage);
        System.out.println(name + " атакует " + target.name + " и наносит " + damage + " урона");
    }

    void takeDamage(int damage) {
        health -= damage;
        if (health < 0) health = 0;
        System.out.println(name + " получает " + damage + " урона. Осталось здоровья: " + health);
    }

    void equipWeapon(Weapon newWeapon) {
        this.weapon = newWeapon;
        System.out.println(name + " экипировал " + newWeapon.name);
    }

    void display() {
        System.out.println("Юнит: " + name + ", здоровье: " + health + "/" + maxHealth +
                ", мана: " + mana + ", стоимость: " + cost);
        System.out.print("Способности: ");
        for (String ability : abilities) {
            System.out.print(ability + " ");
        }
        System.out.println();
        if (weapon != null) {
            System.out.println("Оружие: " + weapon.name);
        }
    }
}

class Building {
    String name;
    String type;
    int health;
    int maxHealth;
    int armor;
    int resourceProduction;
    Unit[] producesUnits;

    Building(String name, String type, int health, int armor,
             int resourceProduction, Unit[] producesUnits) {
        this.name = name;
        this.type = type;
        this.health = health;
        this.maxHealth = health;
        this.armor = armor;
        this.resourceProduction = resourceProduction;
        this.producesUnits = producesUnits;
    }

    int produceResources() {
        System.out.println(name + " производит " + resourceProduction + " ресурсов");
        return resourceProduction;
    }

    void takeDamage(int damage) {
        health -= damage;
        if (health < 0) health = 0;
        System.out.println(name + " получает " + damage + " урона. Осталось здоровья: " + health);
    }

    void repair(int amount) {
        health += amount;
        if (health > maxHealth) health = maxHealth;
        System.out.println(name + " отремонтировано на " + amount + " единиц");
    }

    void display() {
        System.out.println("Здание: " + name + ", тип: " + type +
                ", здоровье: " + health + "/" + maxHealth + ", броня: " + armor);
        System.out.println("Производит ресурсов: " + resourceProduction);
        System.out.print("Может строить юнитов: ");
        for (Unit unit : producesUnits) {
            System.out.print(unit.name + " ");
        }
        System.out.println();
    }
}

class Weapon {
    String name;
    int damage;
    String quality;
    String[] usableByUnits;
    String damageType;
    int attackSpeed;

    Weapon(String name, int damage, String quality, String[] usableByUnits,
           String damageType, int attackSpeed) {
        this.name = name;
        this.damage = damage;
        this.quality = quality;
        this.usableByUnits = usableByUnits;
        this.damageType = damageType;
        this.attackSpeed = attackSpeed;
    }

    void upgrade() {
        damage = (int)(damage * 1.2);
        System.out.println(name + " улучшено! Новый урон: " + damage);
    }

    double calculateDPS() {
        return damage * attackSpeed / 10.0;
    }

    boolean canBeUsedBy(String unitName) {
        for (String unit : usableByUnits) {
            if (unit.equals(unitName)) {
                return true;
            }
        }
        return false;
    }

    void display() {
        System.out.println("Оружие: " + name + ", урон: " + damage +
                ", качество: " + quality + ", тип урона: " + damageType +
                ", скорость: " + attackSpeed);
        System.out.print("Может использовать: ");
        for (String unitName : usableByUnits) {
            System.out.print(unitName + " ");
        }
        System.out.println();
        System.out.println("DPS: " + calculateDPS());
    }
}

public class Main {
    public static void main(String[] args) {
        // Создание оружия
        Weapon sword = new Weapon("Меч воина", 15, "Редкое",
                new String[]{"Воин", "Рыцарь"}, "физический", 8);

        Weapon staff = new Weapon("Посох мага", 25, "Эпическое",
                new String[]{"Маг", "Жрец"}, "магический", 5);

        // Создание юнитов
        Unit warrior = new Unit("Воин", 100, 30, 50,
                new String[]{"Сила духа", "Защита"});

        Unit mage = new Unit("Маг", 60, 100, 80,
                new String[]{"Огненный шар", "Ледяная стрела"});

        // Создание зданий
        Unit[] barracksUnits = {warrior};
        Building barracks = new Building("Казармы", "Военное", 500, 10, 0, barracksUnits);

        Unit[] mageTowerUnits = {mage};
        Building mageTower = new Building("Башня магов", "Магическое", 300, 5, 10, mageTowerUnits);

        System.out.println("=== СОЗДАНЫ ОБЪЕКТЫ ===");
        warrior.display();
        mage.display();
        barracks.display();
        mageTower.display();
        sword.display();
        staff.display();


        // Тесты
        System.out.println("\n1. Работа с оружием:");
        sword.upgrade();
        System.out.println("Меч может использоваться магом? " + sword.canBeUsedBy("Маг"));

        System.out.println("\n2. Работа с юнитами:");
        warrior.equipWeapon(sword);
        warrior.attack(mage);
        mage.equipWeapon(staff);

        System.out.println("\n3. Работа со зданиями:");
        int resources = mageTower.produceResources();
        System.out.println("Получено ресурсов: " + resources);

        barracks.takeDamage(50);
        barracks.repair(30);

        System.out.println("\n4. Проверка DPS:");
        System.out.println("DPS меча: " + sword.calculateDPS());
        System.out.println("DPS посоха: " + staff.calculateDPS());
    }
}