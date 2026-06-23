public class HashTableTest
{
    public static void main(String[] args)
    {
        HashTable table = new HashTable(17, 3);

        // тест hashFun
        int hash = table.hashFun("test");
        if (hash >= 0 && hash < table.size)
            System.out.println("hashFun OK");
        else
            System.out.println("hashFun FAIL");

        // тест put
        int slot = table.put("apple");
        if (slot != -1)
            System.out.println("put OK");
        else
            System.out.println("put FAIL");

        // тест find
        int found = table.find("apple");
        if (found == slot)
            System.out.println("find OK");
        else
            System.out.println("find FAIL");

        // тест коллизий
        table.put("banana");
        table.put("orange");
        table.put("grape");

        if (table.find("banana") != -1 &&
                table.find("orange") != -1 &&
                table.find("grape") != -1)
        {
            System.out.println("collision test OK");
        }
        else
        {
            System.out.println("collision test FAIL");
        }

        // поиск отсутствующего
        if (table.find("not_exist") == -1)
            System.out.println("not found test OK");
        else
            System.out.println("not found test FAIL");
    }
}