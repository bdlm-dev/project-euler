package main;

import java.util.ArrayList;
import java.util.List;

public class util {
	public interface IProblem {
		long run();
	}

	/**
	 * Time the execution of a given problem,
	 * displaying return value and time to execute
	 * @param prob instance of problem to run
	 */
	public static void time(IProblem prob) {
		
		long out;
		
		long startTime = System.nanoTime();
		out = prob.run();
		long endTime = System.nanoTime();

		float duration = (endTime - startTime) / 1000000f;
		// cast to float to prevent integer calculation which truncates decimals
		System.out.println(prob.getClass().getName() + "\n - Returned: " + out + "\n - Took: " + duration + "ms");
	}

	/**
	 * Returns whether a given integer is prime
	 * @param n integer to check
	 * @return whether input is prime
	 */
	public static boolean isPrime(int n) {
		if (n <= 1) return false;
		for (int i=2; i < (int) Math.sqrt(n)+1; i++ ) {
			if (n % i == 0) {
				return false;
			}
		}
		return true;
	}

	/**
	 * Returns an array of all primes
	 * below a given number, n
	 * @param n upper bound
	 * @return all prime numbers below n
	 */
	public static List<Integer> getPrimes(int n) {
		/*
		 * Sieve of Eratosthenes
		 * Initialize array of 2 through n
		 * ( 0 through n in java )
		 */
		boolean[] array = new boolean[n];

		for (int i = 2; i < n-1; i++ ) {
			if ( array[i] ) continue;
			int p = i*2;
			while (p < n-1) {
				array[p] = true;
				p += i;
			}
		}

		List<Integer> primes = new ArrayList<>();

		for (int i=2; i < n-1; i++ ) {
			if (!array[i])
				primes.add(i);
		}

		return primes;
	}


	/**
	 * Computes the greatest common divisor
	 * of two integers using the Euclidean algorithm
	 * @param a integer one
	 * @param b integer two
	 * @return gcd(a, b)
	 */
	public static int gcd(int a, int b) {
		int t;
		while (b != 0) {
			t = b;
			b = a % b;
			a = t;
		}
		return a;
	}

	// recursive gcd
	public static int gcd_r(int a, int b) {
		if (b == 0) return a;
		return gcd_r(b, a % b);
	}

	/**
	 * Computes the lowest common multiple
	 * of two integers
	 * @param a integer one
	 * @param b integer two
	 * @return LCM of a and b
	 */
	public static int lcm(int a, int b) {
		return a * (b / gcd(a, b));
	}

	/**
	 * Computes the lowest common multiple
	 * of an array of integers,
	 * using gcd
	 * @param n array of integers
	 * @return lowest common multiple
	 */
	public static int lcm(int[] n) {
		int result = n[0];
		for (int i = 1; i < n.length; i++) {
			result = lcm(result, n[i]);
		}
		return result;
	}

	/**
	 * Returns the sum of a list of integers
	 * @param n list of integers
	 * @return sum
	 */
	public static long sum(List<Integer> n) {
		long sum = 0;

        for (Integer integer : n) {
            sum += integer;
        }

		return sum;
	}
}
