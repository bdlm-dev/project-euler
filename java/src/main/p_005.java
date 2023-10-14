package main;

/*
 * 2520 is the smallest number that can be divided
 * by each of the numbers from 1 to 10
 * without any remainder.
 *
 * What is the smallest positive number that is
 * evenly divisible by all the numbers from 1 to 20
 */

// Replace x with problem number in class name, main

public class p_5 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_5());
    }

    public int run () {
        return util.lcm(new int[] {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20});
    }
}
