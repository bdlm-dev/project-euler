package main;

/*
 * There exists exactly one Pythagorean triplet for which
 * a + b + c = 1000
 * Find the product abc
 */

public class p_009 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_009());
    }

    public long run () {
        int c;
        for (int a = 1; a < 999; a++) {
            for (int b = 1; b < 999; b++) {
                c = 1000 - a - b;
                if (a*a + b*b == c*c) {
                    return a * b * c;
                }
            }
        }
        return -1;
    }
}
