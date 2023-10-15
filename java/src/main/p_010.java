package main;

/*
 * Find the sum of all the primes below two million.
 */

public class p_010 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_010());
    }

    public long run () {
        int lim = 2000000;
        return util.sum(util.getPrimes(lim));
    }
}
