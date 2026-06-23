import java.util.*;

public class StackTest
{
    public static void main(String[] args)
    {
        testSize();
        testPush();
        testPeek();
        testPop();
    }

    private static void testSize()
    {
        Stack<Integer> s = new Stack<>();
        assert s.size() == 0;

        s.push(1);
        assert s.size() == 1;

        s.push(2);
        assert s.size() == 2;

        s.pop();
        assert s.size() == 1;

        s.pop();
        assert s.size() == 0;
    }

    private static void testPush()
    {
        Stack<String> s = new Stack<>();
        s.push("a");
        s.push("b");
        s.push("c");

        assert s.size() == 3;
        assert s.peek().equals("c");
    }

    private static void testPeek()
    {
        Stack<Integer> s = new Stack<>();

        assert s.peek() == null;

        s.push(10);
        assert s.peek() == 10;
        assert s.size() == 1;

        s.push(20);
        assert s.peek() == 20;
        assert s.size() == 2;
    }

    private static void testPop()
    {
        Stack<Integer> s = new Stack<>();

        assert s.pop() == null;

        s.push(1);
        s.push(2);
        s.push(3);

        assert s.pop() == 3;
        assert s.pop() == 2;
        assert s.pop() == 1;
        assert s.pop() == null;
        assert s.size() == 0;
    }
}
