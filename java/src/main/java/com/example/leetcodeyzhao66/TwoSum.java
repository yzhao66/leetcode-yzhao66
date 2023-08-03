package com.example.leetcodeyzhao66;

import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

/**
 * 1. 两数之和 (https://leetcode-cn.com/problems/two-sum/)
 */
public class TwoSum {

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int[] nums = {3,2,4};
        int target = 6;
        System.out.println(target);
        int[] result = twoSum(nums, target);
        int[] result2 = twoSum2(nums, target);
        System.out.println(result2.toString());


    }

    public static int[] twoSum(int[] nums, int target) {
//        int[] ints = new int[2];
        for (int i = 0; i < nums.length; i++) {
            for (int j = i + 1; j <= nums.length - 1; j++) {
                if (nums[i] + nums[j] == target) {
                    return new int[]{i, j};
                }
            }
        }
        return null;
    }

    public static int[] twoSum2(int[] nums, int target) {
        Map<Integer, Integer> map = new HashMap<Integer, Integer>();
        for (int i = 0; i < nums.length; i++) {
            if (map.containsKey(target - nums[i])) {
                return new int[]{map.get(target - nums[i]), i};
            }
            map.put(nums[i], i);
        }
        return new int[0];
    }


}
