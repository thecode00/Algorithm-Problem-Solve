// https://leetcode.com/problems/group-anagrams/description/

class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String, List<String>> wordHash = new HashMap<>();

        for (String word: strs){
            char[] chars = word.toCharArray();
            Arrays.sort(chars);
            String key = String.valueOf(chars);

            if (!wordHash.containsKey(key)){
                wordHash.put(key, new ArrayList<>());
            }
            wordHash.get(key).add(String.valueOf(word));
        }

        return new ArrayList<>(wordHash.values()); 
    }
}