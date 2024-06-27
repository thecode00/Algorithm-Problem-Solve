// https://leetcode.com/problems/jewels-and-stones/description/

class Solution {
    public int numJewelsInStones(String jewels, String stones) {
        Set<Character> jewelSet = new HashSet<>();
        // Save jewels to jewelSet and find jewel in the stones
        for (char jewel: jewels.toCharArray()){
            jewelSet.add(jewel);
        }

        int count = 0;
        for (char stone: stones.toCharArray()){
            if (jewelSet.contains(stone)){
                count += 1;
            }
        }

        return count;
    }
}