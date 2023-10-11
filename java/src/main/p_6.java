package main;

/*
 * Find the difference between the
 * sum of the squares of the first
 * one hundred natural numbers
 * and the square of the sum.
 */

// template

import java.util.List;
import java.util.ArrayList;

public class p_6 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_6());
    }

    public int run () {
        int lim = 100;

        List<Integer> part_1 = new ArrayList<>();
        int part_2 = 0;

        for (int i = 1; i <= lim; i++) {
            part_1.add(i*i);
            part_2 += i;
        }

        part_2 *= part_2;

        return Math.abs(part_2 - util.sum(part_1));
    }
}
