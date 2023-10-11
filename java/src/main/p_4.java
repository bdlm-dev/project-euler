package main;

/*
A palindromic number reads the same both ways.
The largest palindrome made from the product of
two 2-digit numbers is: 9009 = 91 x 99.

Find the largest palindrome made from the product of
two 3-digit numbers.
 */

public class p_4 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_4());
    }

    public int run () {

        int max = -1, calc;
        String calcString;

        for (int i=0; i < 1000; i++) {
            for (int j=0; j < 1000; j++) {
                calc = i * j;
                calcString = Integer.toString(calc);
                if (calcString.contentEquals(new StringBuilder(calcString).reverse())) {
                    if (calc > max) max = calc;
                }
            }
        }

        return max;
    }
}
