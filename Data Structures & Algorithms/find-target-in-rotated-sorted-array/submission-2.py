class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0  # The left pointer starts at the beginning of the array
        r = len(nums) - 1  # The right pointer starts at the end of the array
        
        while l <= r:  # Continue searching as long as the left pointer is not past the right pointer
            mid = (l + r) // 2  # Calculate the middle index

            # If the target is found at the middle index, return its index
            if nums[mid] == target:  # Check if the element at the mid index is equal to the target
                return mid

            # Determine which side (left or right) of the array is sorted
            if nums[l] <= nums[mid]:  # If the left part of the array is sorted
                # Check if the target is in the sorted left part
                if nums[l] <= target < nums[mid]:  # Target lies between nums[l] and nums[mid], so it's in the left part
                    r = mid - 1  # Move the right pointer to the left side, narrowing the search to the left half
                else:
                    l = mid + 1  # Otherwise, search in the right half
            else:  # The right part of the array is sorted
                # Check if the target is in the sorted right part
                if nums[mid] < target <= nums[r]:  # Target lies between nums[mid] and nums[r], so it's in the right part
                    l = mid + 1  # Move the left pointer to the right side, narrowing the search to the right half
                else:
                    r = mid - 1  # Otherwise, search in the left half
        
        # If the target was not found, return -1
        return -1
