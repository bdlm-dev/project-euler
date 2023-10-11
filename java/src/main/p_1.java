package main;/*
 Find the sum of all the multiples
 of 3 or 5 below 1000
 */

public class p_1 implements util.IProblem {

	public static void main(String[] args) {
		// time function with main.util timing method
		util.time(new p_1());

		// code of main.util timing method but here instead of via main.util class
		long startTime = System.nanoTime();
		new p_1().run();
		long endTime = System.nanoTime();

		long duration = (endTime - startTime);
		
		System.out.println("main.p_1 took " + (float)duration/1000000f + "ms");
	}
	
	public int run() {
		int sum = 0;
		
		for (int i=0; i<1000; i++) {
			if (i % 3 == 0 || i % 5 == 0) {
				sum += i;
			}
		}
		
		// printing the value destroys performance for some reason
		
		System.out.println(sum);
		
		return sum;
	}
}
