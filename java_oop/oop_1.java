// Класс для мессенджера
class Message {
    String text;
    String sender;
    String receiver;
    String format; // текст, фото, видео

    Message(String text, String sender, String receiver, String format) {
        this.text = text;
        this.sender = sender;
        this.receiver = receiver;
        this.format = format;
    }

    void display() {
        System.out.println("От: " + sender + ", К: " + receiver + ", Формат: " + format + ", Сообщение: " + text);
    }
}

class Chat {
    String user1;
    String user2;
    String chatName;

    Chat(String user1, String user2, String chatName) {
        this.user1 = user1;
        this.user2 = user2;
        this.chatName = chatName;
    }

    void display() {
        System.out.println("Чат: " + chatName + " между " + user1 + " и " + user2);
    }
}

class Avatar {
    String image;
    String owner;
    String lastUpdate;

    Avatar(String image, String owner, String lastUpdate) {
        this.image = image;
        this.owner = owner;
        this.lastUpdate = lastUpdate;
    }

    void display() {
        System.out.println("Аватар пользователя: " + owner + ", Файл: " + image + ", Обновлён: " + lastUpdate);
    }
}

// Абстрактная стратегия
class Unit {
    String name;
    int health;
    int mana;
    int cost;
    String[] abilities;
    Weapon weapon; // связь с оружием

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
    Unit[] producesUnits; // какие юниты строит

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
    String[] usableByUnits; // какие юниты могут использовать
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

public class Main {
    // Метод для демонстрации побочного эффекта
    static void damageUnit(Unit unit, int damage) {
        unit.health -= damage;
        System.out.println(unit.name + " получил урон " + damage);
    }

    public static void main(String[] args) {
        // === Пример мессенджера ===
        Message msg1 = new Message("Привет!", "Alice", "Bob", "текст");
        Chat chat1 = new Chat("Alice", "Bob", "Друзья");
        Avatar avatar1 = new Avatar("alice.png", "Alice", "2025-11-21");

        System.out.println("=== Мессенджер ===");
        msg1.display();
        chat1.display();
        avatar1.display();

        // === Пример стратегии ===
        Weapon sword = new Weapon("Меч", 15, "Обычный", new String[]{"Воин"}, "Физический", 5);
        Unit warrior = new Unit("Воин", 100, 50, 20, new String[]{"Удар", "Блок"});
        warrior.weapon = sword;

        Building barracks = new Building("Казарма", "Военное здание", 500, 50, 100, new Unit[]{warrior});

        System.out.println("\n=== Стратегия ===");
        sword.display();
        warrior.display();
        barracks.display();

        // === Демонстрация побочного эффекта ===
        System.out.println("\n=== Побочный эффект ===");
        System.out.println("До атаки:");
        warrior.display();

        damageUnit(warrior, 30); // метод изменяет объект

        System.out.println("После атаки:");
        warrior.display();
    }
}
