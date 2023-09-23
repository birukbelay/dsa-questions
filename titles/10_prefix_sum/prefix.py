def find_pre_sum(nums):
    pre_sum = [0]
    for i in range(len(nums)):
                pre_sum.append(pre_sum[i] + nums[i])
    return pre_sum
