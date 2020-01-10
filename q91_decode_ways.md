# Solutions

* DP Solution
  * Thoughts: 
    * 这道题有三个难点：
      * 初始值：`previous_two_chars_count`的初始值必须是1，这点从逻辑上没想通
      * 判断条件：要判断第i个数能不能与前一个数结合，还要判断该数是不是0，是0就必须与前一个数结合，Solution中用到的这个判断条件很巧妙，一次性解决了前面两个判断
        * 注意0的处理方式：第一个数字是0，肯定就解不了，如果中间某个数字是0，0前面的数又大于了2，那也解不了
      * 判断后的操作：当前值应该是之前值累加的，因为实际上求的是有多少种方式
  * Time complexity: $O(n)$
  * Space complexity: $O(1)$