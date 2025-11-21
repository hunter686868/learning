// 1.1 Классы
//Мессенджер.
//Класс Message - в нем текст, отправитель, получатель, формат
//Класс Chat - в нем пользователь1, пользователь2, название чата
//Класс Аватар - в нем изображение, пользователь, последняя дата обновления

// Банковское приложение
// Класс User - в нем Имя, Фамилия, ID, список счетов
// Класс Account - в нем номер, тип, баланс, валюта
// Класс Card - в нем номер, срок действия, привязанный счет, тип



// 1.2 Игра - стратегия

class Unit {
    String name;
    int health;
    int mana;
    int cost;
    String[] abilities;
    Weapon weapon;

    Unit(String name, int health, int mana, int cost, String[] abilities) {
        this.name = name;
        this.health = health;
        this.mana = mana;
        this.cost = cost;
        this.abilities = abilities;
    }

    void display() {
        System.out.println("Юнит: " + name + ", здоровье: " + health + ", мана: " + mana + ", стоимость: " + cost);
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
    int armor;
    int resourceProduction;
    Unit[] producesUnits;

    Building(String name, String type, int health, int armor, int resourceProduction, Unit[] producesUnits) {
        this.name = name;
        this.type = type;
        this.health = health;
        this.armor = armor;
        this.resourceProduction = resourceProduction;
        this.producesUnits = producesUnits;
    }

    void display() {
        System.out.println("Здание: " + name + ", тип: " + type + ", здоровье: " + health + ", броня: " + armor);
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
    int attack;
    String quality;
    String[] usableByUnits;
    String damageType;
    int attackSpeed;

    Weapon(String name, int attack, String quality, String[] usableByUnits, String damageType, int attackSpeed) {
        this.name = name;
        this.attack = attack;
        this.quality = quality;
        this.usableByUnits = usableByUnits;
        this.damageType = damageType;
        this.attackSpeed = attackSpeed;
    }

    void display() {
        System.out.println("Оружие: " + name + ", атака: " + attack + ", качество: " + quality + ", тип урона: " + damageType + ", скорость: " + attackSpeed);
        System.out.print("Может использовать: ");
        for (String unitName : usableByUnits) {
            System.out.print(unitName + " ");
        }
        System.out.println();
    }
}

// 1.3 Побочный эффект, в методе получения урона изменяется состояние warrior

public class Main {
    static void damageUnit(Unit unit, int damage) {
        unit.health -= damage;
        System.out.println(unit.name + " получил урон " + damage);
    }

    public static void main(String[] args) {
        Weapon sword = new Weapon("Меч", 15, "Обычный", new String[]{"Воин"}, "Физический", 5);
        Unit warrior = new Unit("Воин", 100, 50, 20, new String[]{"Удар", "Блок"});
        warrior.weapon = sword;
        Building barracks = new Building("Казарма", "Военное здание", 500, 50, 100, new Unit[]{warrior});

        sword.display();
        warrior.display();
        barracks.display();

        System.out.println("До атаки:");
        warrior.display();

        damageUnit(warrior, 30);

        System.out.println("После атаки:");
        warrior.display();
    }
}
