// Оружие и его наследники
class Weapon {
    private String name;
    private int damage;
    private String quality;
    private String[] usableByUnits;
    private String damageType;
    private int attackSpeed;

    public Weapon(String name, int damage, String quality, String[] usableByUnits,
                  String damageType, int attackSpeed) {
        this.name = name;
        this.damage = damage;
        this.quality = quality;
        this.usableByUnits = usableByUnits;
        this.damageType = damageType;
        this.attackSpeed = attackSpeed;
    }

    public void upgrade() {
        damage = (int)(damage * 1.2);
        System.out.println(name + " улучшено! Новый урон: " + damage);
    }

    public double calculateDPS() {
        return damage * attackSpeed / 10.0;
    }

    public boolean canBeUsedBy(String unitName) {
        for (String unit : usableByUnits) {
            if (unit.equals(unitName)) {
                return true;
            }
        }
        return false;
    }

    // Метод отображения информации
    public void display() {
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

    // Геттеры
    public String getName() { return name; }
    public int getDamage() { return damage; }
    public String getDamageType() { return damageType; }
}

// Ближнее оружие
class MeleeWeapon extends Weapon {
    private int range; // Дистанция атаки
    private boolean canBlock; // Может ли блокировать

    public MeleeWeapon(String name, int damage, String quality, String[] usableByUnits,
                       String damageType, int attackSpeed, int range, boolean canBlock) {
        super(name, damage, quality, usableByUnits, damageType, attackSpeed);
        this.range = range;
        this.canBlock = canBlock;
    }

    // Блокирование атаки
    public void blockAttack() {
        if (canBlock) {
            System.out.println(getName() + " блокирует атаку!");
        } else {
            System.out.println(getName() + " не может блокировать атаки");
        }
    }

    // Ближний удар
    public void meleeStrike(Unit target) {
        System.out.println(getName() + " наносит ближний удар на дистанции " + range + " единиц");
        System.out.println("Нанесен урон: " + getDamage());
    }

    public void displayMeleeInfo() {
        display();
        System.out.println("Дистанция атаки: " + range);
        System.out.println("Может блокировать: " + canBlock);
    }
}

// Дальнее оружие
class RangedWeapon extends Weapon {
    private int maxRange; // Максимальная дальность
    private int ammo; // Количество боеприпасов

    public RangedWeapon(String name, int damage, String quality, String[] usableByUnits,
                        String damageType, int attackSpeed, int maxRange, int ammo) {
        super(name, damage, quality, usableByUnits, damageType, attackSpeed);
        this.maxRange = maxRange;
        this.ammo = ammo;
    }

    // Выстрел на дистанцию
    public void shootAtRange(Unit target, int distance) {
        if (distance > maxRange) {
            System.out.println("Цель слишком далеко! Максимальная дальность: " + maxRange);
            return;
        }
        if (ammo <= 0) {
            System.out.println("Нет боеприпасов!");
            return;
        }
        ammo--;
        System.out.println(getName() + " стреляет на дистанцию " + distance + " единиц");
        System.out.println("Осталось боеприпасов: " + ammo);
    }

    // Перезарядка
    public void reload(int newAmmo) {
        ammo += newAmmo;
        System.out.println(getName() + " перезаряжен. Боеприпасов: " + ammo);
    }

    public void displayRangedInfo() {
        display();
        System.out.println("Максимальная дальность: " + maxRange);
        System.out.println("Боеприпасы: " + ammo);
    }
}

// Здания и его наследники
class Building {
    private String name;
    private String type;
    private int health;
    private int maxHealth;
    private int armor;
    private int resourceProduction;

    public Building(String name, String type, int health, int armor,
                    int resourceProduction) {
        this.name = name;
        this.type = type;
        this.health = health;
        this.maxHealth = health;
        this.armor = armor;
        this.resourceProduction = resourceProduction;
    }

    public int produceResources() {
        System.out.println(name + " производит " + resourceProduction + " ресурсов");
        return resourceProduction;
    }

    public void takeDamage(int damage) {
        health -= damage;
        if (health < 0) health = 0;
        System.out.println(name + " получает " + damage + " урона. Осталось здоровья: " + health);
    }

    public void repair(int amount) {
        health += amount;
        if (health > maxHealth) health = maxHealth;
        System.out.println(name + " отремонтировано на " + amount + " единиц");
    }

    public void display() {
        System.out.println("Здание: " + name + ", тип: " + type +
                ", здоровье: " + health + "/" + maxHealth + ", броня: " + armor);
        System.out.println("Производит ресурсов: " + resourceProduction);
    }

    // Геттеры
    public String getName() { return name; }
    public int getHealth() { return health; }
    public int getMaxHealth() { return maxHealth; }
}

// Военное здание
class MilitaryBuilding extends Building {
    private Unit[] trainableUnits;
    private int trainingSpeed;

    public MilitaryBuilding(String name, int health, int armor,
                            int resourceProduction, Unit[] trainableUnits, int trainingSpeed) {
        super(name, "Военное", health, armor, resourceProduction);
        this.trainableUnits = trainableUnits;
        this.trainingSpeed = trainingSpeed;
    }

    // Тренировка юнитов
    public void trainUnit(String unitName) {
        System.out.println(getName() + " начинает тренировку " + unitName);
        System.out.println("Скорость тренировки: " + trainingSpeed + " единиц/час");
    }

    // Укрепление защиты
    public void fortify() {
        System.out.println(getName() + " укрепляет свои защитные сооружения");
        System.out.println("Броня увеличена на время");
    }

    public void displayMilitaryInfo() {
        display();
        System.out.print("Может тренировать: ");
        for (Unit unit : trainableUnits) {
            System.out.print(unit.getName() + " ");
        }
        System.out.println();
        System.out.println("Скорость тренировки: " + trainingSpeed);
    }
}

// Экономическое здание
class EconomicBuilding extends Building {
    private String resourceType;
    private int storageCapacity;

    public EconomicBuilding(String name, int health, int armor,
                            int resourceProduction, String resourceType, int storageCapacity) {
        super(name, "Экономическое", health, armor, resourceProduction);
        this.resourceType = resourceType;
        this.storageCapacity = storageCapacity;
    }

    // Хранение ресурсов
    public void storeResources(int amount) {
        if (amount > storageCapacity) {
            System.out.println("Слишком много ресурсов! Вместимость: " + storageCapacity);
        } else {
            System.out.println("Ресурсы (" + amount + " " + resourceType + ") сохранены в " + getName());
        }
    }

    // Продажа ресурсов
    public int sellResources(int amount) {
        System.out.println("Продано " + amount + " " + resourceType + " из " + getName());
        int profit = amount * 10; // Простая формула для примера
        System.out.println("Получено золота: " + profit);
        return profit;
    }

    public void displayEconomicInfo() {
        display();
        System.out.println("Тип ресурса: " + resourceType);
        System.out.println("Вместимость: " + storageCapacity);
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

    public Unit(String name, int health, int mana, int cost, String[] abilities) {
        this.name = name;
        this.health = health;
        this.maxHealth = health;
        this.mana = mana;
        this.cost = cost;
        this.abilities = abilities;
        this.weapon = null;
    }

    // Метод атаки
    public void attack(Unit target) {
        if (weapon == null) {
            System.out.println(name + " не может атаковать без оружия!");
            return;
        }
        int damage = weapon.getDamage();
        target.takeDamage(damage);
        System.out.println(name + " атакует " + target.getName() + " и наносит " + damage + " урона");
    }

    // Метод получения урона
    public void takeDamage(int damage) {
        health -= damage;
        if (health < 0) health = 0;
        System.out.println(name + " получает " + damage + " урона. Осталось здоровья: " + health);
    }

    // Метод экипировки оружия
    public void equipWeapon(Weapon newWeapon) {
        if (newWeapon.canBeUsedBy(name)) {
            this.weapon = newWeapon;
            System.out.println(name + " экипировал " + newWeapon.getName());
        } else {
            System.out.println(name + " не может использовать " + newWeapon.getName());
        }
    }

    // Отображение информации
    public void display() {
        System.out.println("Юнит: " + name + ", здоровье: " + health + "/" + maxHealth +
                ", мана: " + mana + ", стоимость: " + cost);
        System.out.print("Способности: ");
        for (String ability : abilities) {
            System.out.print(ability + " ");
        }
        System.out.println();
        if (weapon != null) {
            System.out.println("Оружие: " + weapon.getName());
        }
    }

    // Геттеры
    public String getName() { return name; }
    public int getHealth() { return health; }
    public int getCost() { return cost; }
}

public class Main {
    public static void main(String[] args) {

        // Создаем оружие разных типов
        MeleeWeapon sword = new MeleeWeapon("Двуручный меч", 20, "Редкое",
                new String[]{"Воин", "Паладин"}, "физический", 6, 2, true);

        RangedWeapon bow = new RangedWeapon("Длинный лук", 15, "Обычное",
                new String[]{"Лучник", "Охотник"}, "физический", 8, 30, 20);

        RangedWeapon staff = new RangedWeapon("Огненный посох", 25, "Эпическое",
                new String[]{"Маг", "Чародей"}, "магический", 4, 20, 50);

        // Методы ближнего оружия
        System.out.println("\n1. Демонстрация ближнего оружия:");
        sword.displayMeleeInfo();
        sword.upgrade();
        sword.blockAttack();
        sword.meleeStrike(null);

        // Методоы дальнего оружия
        System.out.println("\n2. Демонстрация дальнего оружия:");
        bow.displayRangedInfo();
        bow.shootAtRange(null, 25);
        bow.shootAtRange(null, 35);
        bow.reload(10);

        System.out.println("DPS меча: " + sword.calculateDPS());
        System.out.println("DPS лука: " + bow.calculateDPS());
        System.out.println("DPS посоха: " + staff.calculateDPS());

        System.out.println("\n=== ВТОРАЯ ИЕРАРХИЯ: ЗДАНИЯ ===");

        // Создаем юнитов
        Unit warrior = new Unit("Воин", 100, 30, 50,
                new String[]{"Сила духа", "Защита"});

        Unit archer = new Unit("Лучник", 70, 20, 40,
                new String[]{"Меткий выстрел", "Уклонение"});

        Unit mage = new Unit("Маг", 60, 100, 80,
                new String[]{"Огненный шар", "Ледяная стрела"});

        // Создаем здания разных типов
        Unit[] militaryUnits = {warrior, archer};
        MilitaryBuilding barracks = new MilitaryBuilding("Казармы", 500, 15,
                0, militaryUnits, 5);

        EconomicBuilding farm = new EconomicBuilding("Ферма", 200, 5,
                50, "Еда", 1000);

        EconomicBuilding mine = new EconomicBuilding("Шахта", 300, 10,
                30, "Золото", 500);

        // Методы военного здания
        barracks.displayMilitaryInfo();
        barracks.trainUnit("Воин");
        barracks.fortify();
        barracks.takeDamage(50);
        barracks.repair(20);

        // Методы экономического здания
        farm.displayEconomicInfo();
        farm.storeResources(800);
        farm.storeResources(1200);
        int gold = farm.sellResources(100);

        mine.displayEconomicInfo();
        mine.produceResources();
        mine.storeResources(300);

        System.out.println("\n1. Воин экипирует оружие:");
        warrior.equipWeapon(sword);
        mage.equipWeapon(staff);

        System.out.println("\n2. Юниты тренируются в зданиях:");
        barracks.trainUnit("Лучник");

        System.out.println("\n3. Экипировка оружия из инвентаря здания:");
        archer.equipWeapon(bow);
        bow.shootAtRange(null, 15);


        System.out.println("\nСоздано объектов:");
        System.out.println("- Оружие: " + sword.getName() + ", " + bow.getName() + ", " + staff.getName());
        System.out.println("- Здания: " + barracks.getName() + ", " + farm.getName() + ", " + mine.getName());
        System.out.println("- Юниты: " + warrior.getName() + ", " + archer.getName() + ", " + mage.getName());

        Weapon[] weapons = {sword, bow, staff};
        for (Weapon w : weapons) {
            System.out.println(w.getName() + " имеет DPS: " + w.calculateDPS());
        }

        Building[] buildings = {barracks, farm, mine};
        int totalResources = 0;
        for (Building b : buildings) {
            totalResources += b.produceResources();
        }
        System.out.println("Всего произведено ресурсов за ход: " + totalResources);
    }
}