package main;

/*
What is the largest prime factor of the number
600851475143
 */

public class p_003 implements util.IProblem {

    public static void main(String[] args) {
        util.time(new p_003());
    }

    public long run () {
        long n = 600851475143L;
        int max = -1;

        for (int i = 2; i < (int) Math.sqrt(n)+1; i++ ) {
            if (n % i == 0) {
                if (i > max && util.isPrime(i)) max = i;
            }
        }

        return max;
    }
}
