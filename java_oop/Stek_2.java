// Доп. задачи
import java.util.*;

// 4 Написать функцию, которая получает на вход строку,
// состоящую из открывающих и закрывающих скобок
// и проверят сбалансированность
public class Brackets
{
    public static boolean balancedRound(String s)
    {
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);
            if (c == '(')
            {
                st.push(c);
            }
            else if (c == ')')
            {
                if (st.pop() == null) return false;
            }
            else
            {
                return false;
            }
        }
        return st.size() == 0;
    }
}

// 5 Расширить фукнцию из предыдущего примера,
// если скобки могут быть трех типов: (), {}, [].
public class BracketsAll
{
    public static boolean balancedAll(String s)
    {
        Stack<Character> st = new Stack<>();
        for (int i = 0; i < s.length(); i++)
        {
            char c = s.charAt(i);

            if (c == '(' || c == '{' || c == '[')
            {
                st.push(c);
            }
            else if (c == ')' || c == '}' || c == ']')
            {
                Character top = st.pop();
                if (top == null) return false;

                if (c == ')' && top != '(') return false;
                if (c == '}' && top != '{') return false;
                if (c == ']' && top != '[') return false;
            }
            else
            {
                return false;
            }
        }
        return st.size() == 0;
    }
}

// 6 Добавить в стек функцию,
// возвращающую текущий минимальный элемент в нём за O(1)
public class MinStack
{
    private Stack<Integer> main = new Stack<>();
    private Stack<Integer> mins = new Stack<>();

    public int size()
    {
        return main.size();
    }

    public void push(int x)
    {
        main.push(x);
        Integer m = mins.peek();
        if (m == null || x <= m) mins.push(x);
    }

    public Integer pop()
    {
        Integer v = main.pop();
        if (v == null) return null;

        Integer m = mins.peek();
        if (m != null && v.intValue() == m.intValue()) mins.pop();
        return v;
    }

    public Integer peek()
    {
        return main.peek();
    }

    public Integer min()
    {
        return mins.peek();
    }
}

// 7 Добавьте в стек функцию, которая возвращает
// среднее значение всех элементов в стеке.
// Она должна выполняться за O(1)
public class AvgStack
{
    private Stack<Integer> st = new Stack<>();
    private long sum = 0;

    public int size()
    {
        return st.size();
    }

    public void push(int x)
    {
        st.push(x);
        sum += x;
    }

    public Integer pop()
    {
        Integer v = st.pop();
        if (v == null) return null;
        sum -= v;
        return v;
    }

    public Integer peek()
    {
        return st.peek();
    }

    public Double avg()
    {
        int n = st.size();
        if (n == 0) return null;
        return (double) sum / n;
    }
}

// 8 Вычисление постфиксного выражения
public class Postfix
{
    private static Stack<String> buildS1(String expr)
    {
        Stack<String> s1 = new Stack<>();
        String[] t = expr.trim().split("\\s+");
        for (int i = t.length - 1; i >= 0; i--)
            s1.push(t[i]);
        return s1;
    }

    public static Integer eval(String expr)
    {
        Stack<String> s1 = buildS1(expr);
        Stack<Integer> s2 = new Stack<>();

        while (s1.size() > 0)
        {
            String tok = s1.pop();

            if (tok.equals("="))
            {
                return s2.pop();
            }
            else if (tok.equals("+") || tok.equals("*"))
            {
                Integer a = s2.pop();
                Integer b = s2.pop();
                if (a == null || b == null) return null;

                if (tok.equals("+")) s2.push(b + a);
                else s2.push(b * a);
            }
            else
            {
                s2.push(Integer.parseInt(tok));
            }
        }
        return null;
    }

    public static void main(String[] args)
    {
        Integer r = eval("8 2 + 5 * 9 + =");
        System.out.println(r);
    }
}