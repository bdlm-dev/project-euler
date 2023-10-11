package main;

/*
 * What is the 10001st prime number?
 */

public class p_7 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_7());
    }

    public int run () {
        int lim = 1000000, index = 10000;
        return util.getPrimes(lim).get(index);
        // best lim is 104745, *but* that requires knowing the answer beforehand
        // so isn't reasonable - so just using 1 million
    }
}
