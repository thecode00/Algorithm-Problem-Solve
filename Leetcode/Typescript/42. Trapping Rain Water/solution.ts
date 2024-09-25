// https://leetcode.com/problems/trapping-rain-water/description/

function trap(height: number[]): number {
  let left = 0,
    right = height.length - 1,
    leftMax = 0,
    rightMax = 0,
    water = 0;

  while (left < right) {
    leftMax = Math.max(leftMax, height[left]);
    rightMax = Math.max(rightMax, height[right]);

    // If
    if (rightMax > leftMax) {
      water += leftMax - height[left];
      left += 1;
    } else {
      water += rightMax - height[right];
      right -= 1;
    }
  }

  return water;
}
