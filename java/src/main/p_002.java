package main;

/*
By considering the terms in the Fibonacci sequence
whose values do not exceed four million,
find the sum of the even-valued terms.
 */

public class p_002 implements util.IProblem {

    int lim = 4000000;
    int total = 0;
    int[] nums = {1, 1};

    public static void main(String[] args) {
        util.time(new p_002());
    }

    public long run () {
        while (nums[1] < lim) {
            if(nums[1] % 2 == 0) {
                total += nums[1];
            }

            int old = nums[0];
            nums[0] = nums[1];
            nums[1] = nums[0] + old;
        }
        return total;
    }
}
