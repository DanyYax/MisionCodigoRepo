#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 10:15:30 2022

Algorithms

@author: dany
"""

def binary_search(nums: list[int], target: int) -> int:
    '''
    Binary search is a textbook algorithm based on the idea to compare the target value
    to the middle element of the array.

    If the target value is equal to the middle element - we're done.
    If the target value is smaller - continue to search on the left.
    If the target value is larger - continue to search on the right.
    
    Implementation
    use 2 pointers
    left: the first item
    right: last item
    calculate the pivot to be in the middle of the array
    
    if the value of the array at pivot is the target then we are done
    if it is greater then search on ly in the right half. Move the left pointer to pivot +1
    if the value of array at pivot is smaller than the target move the right pointer to pivot -1
    
    '''
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = left + (right - left) // 2
        if nums[pivot] == target:
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
    return -1


def two_pointers():
    '''
    Two pointers is really an easy and effective technique that is typically used for searching pairs 
    in a sorted array.
    Given a sorted array A (sorted in ascending order), having N integers, 
    find if there exists any pair of elements (A[i], A[j]) such that their sum is equal to X.
    
    Keep 2 pointers
    left = First item
    right = Last Item
    
    If the sum is greater than target move left pointer to the right
    if the sum is smaller than the target move right pointer to the left
    '''
    