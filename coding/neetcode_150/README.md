# neetcode_150
* https://neetcode.io/practice

#### Questions

##### Array & Hashing
* contains-duplicate (easy): array, hashing
* two-sum (easy): array, addition
* top-k-frequent-elements (medium): bucket sort, bubble sort, array, hashing
* encode-and-decode-strings (medium): array, hashing, pretty easy
* *longest-consecutive-sequence (medium/hard): array, hashing, O(n) time constraint, tricky to start then easy
* *product-of-array-except (medium/hard): array, hashing, O(n) time constraint, tricky then easy
* valid-anagram (easy)
* group-anagrams (medium)
* find-duplicate-file-in-system (medium): tagged dropbox
* valid-sudoku (medium): basic iterating through grid and adding to hash + checking for collisons
* sort-colors (medium): straightforward bubble sort
* brick-wall (medium): i was there with the idea of keeping a cumulative sum for each row and had a working solution, but with admitted large complexity of O(n^2), needed to know that I can continually hash how often that width mark appears and use that to deduce answer

##### Two Pointers
* valid-palindrome (easy): string manipulation, reverse array
* two-sum-ii-input-array-is-sorted (medium): two pointers, use sorted property
* 3sum (medium): next step of two-step ii, hash, left & right pointer
* container-with-most-water (medium)
* rotate-array (medium): not really two pointers? use a helper array to update new values
* boats-to-save-people (medium): set pointer at front and back, check constraint and update left pointer while always decrementing right pointer. remember that at most this is O(n) in scan. do this for left_pointer <= right_pointer
* 4sum (medium): we need to find combinations of four numbers, this can be done by abstacting from the general 2sum problem. what we do is take all combinations of the matrix minus the last 3 elements and then find what those combination targets need to be, then perform 2sum on the remaining portion. time = O(n^3), space O(n) due to recursive calls.

##### Sliding Window
* best-time-to-buy-and-sell-stock (easy): iterate, compare mins and maxs
* longest-substring-without-repeating-characters (medium): great problem, usage of hash to reduce duplicated computing
* longest-repeating-character-replacement (medium): window, efficiency
* permutation-in-string (medium): window, hashmap
* frequency-of-the-most-frequent-element (medium): this appears to be a basic sliding window problem with constraints, but there are subtle steps needed to meet time constaints which I do not think anyone would get in an actual interview
* find-the-index-of-the-first-occurence-in-a-string (medium): sliding window, looking for a target word within a larger. use a sliding window of length target word and check for match

##### Stack
* *generate-parentheses (medium): backtracking, recursion, dfs
* car-fleet (medium): stack, monotonic stack, math
* daily-temperature (medium): monotonic decreasing stack, [GOOD]
* valid-parantheses (easy): stack
* min-stack (medium)
* asteroid-collison (medium): need to understand that all asteroid move same speed, so collisions will happen right to left. therefore need to identify that using a stack is best as it will be O(1)

##### Trees
* invert-binary-tree (easy): classic, bfs, revisit this for warmup!
* maximum-depth-of-binary-tree (easy): dfs
* lowest-common-ancestor-of-a-binary-search-tree (medium): binary search tree property
* binary-tree-level-order-traversal (medium): bfs
* count-good-nodes-in-binary-tree (medium): dfs keeping track of other variables
* binary-tree-right-side-view (medium): bfs or dfs with trick
* kth-smallest-element-in-a-bst (medium): binary search tree, in-order traversal
* same-tree (blind75, easy)
* sum-root-to-leaf-numbers (medium): recall how stack, frames, and variables work in recursion. if done incorrectly, you can reference the same object location in memory which will not allow you to access the "version" of variables you want within the DFS

##### Tries
* implement-trie-prefix-tree (medium): basic prefix trie, oop
* design-add-and-search-words-data-structure (medium): prefix trie, dfs

##### Heap
* kth-largest-element-in-a-stream (easy): basic overview of how heap works
* last-stone-weight (easy): max heap
* k-closest-points-to-origin (medium): min heap
* kth-largest-element-in-an-array (medium): min heap (k-th largest)
* task-scheduler: need to think of a clever way to use both a heap and a queue. increase time counter, extract element from root of heap, push onto queue, extract from queue based on time counter constraint. O(n) because can only have size 26 nodes in heap.

##### Binary Search
* binary-search (easy): basic binary search implementation
* search-a-2d-matrix (medium): binary search, 2d
* koko-eating-bananas (medium): binary search, math tricks
* search-in-rotated-sorted-array (medium): binary search with rotation
* find-minimum-in-rotated-sorted-array (medium): binary search but need to check on rotation
* single-element-in-sorted-array (medium): perform binary search but need to locate which side of array is odd-numbered, then search that direction to figure out single element
* find-first-and-last-position-of-element-in-sorted-array (medium): straightforward practice of key concept, minimal tricks, perform binary search then do some extra searching on top. O(logn)
* time-based-key-value-store (medium): straightfowartd OOP and binary search problem, need to pay attention that timestamps are always increasing
* search-in-a-sorted-array-of-unknown-size (medium): need to figure size of array first which is O(log(2**31)) = constant, then normal binary search = O(logt) for t size of array

##### Linked List
* reverse-linked-list (easy): example how to use linkedlist class and reverse
* merge-two-sorted-list (easy): oof I really do not like linkedlist questions, they're simply but I always seem to mess something up
  * [Why is dummy node changing](https://stackoverflow.com/questions/72588124/why-is-dummy-node-changing-in-this-linked-list-problem-python3) seems to be the best explanation for what's happening under the hood. Super helpful
* reorder (medium): this _seems_ like an easy problem in terms of getting an approach, but actually completing it is a tad confusing for me. I think I'm having troubles understandanding how
manipulation in place is occuring
* remove-nth-node-from-end-of-list (medium): this was more straightforward and pretty much got it, though use of the dummy node is still a bit fuzzy for me
* linked-list-cycle (easy): keep track of visited nodes, if so return Tru
* add-two-numbers (medium): basic traversal of two lists, but need to do some math tricks. nailed this one.
* copy-list-with-random-pointer (medium): need to take 2 passes through the linked list. on the first one map the old node to a new node with same value via a dict. one second pass then update new nodes' next and random attributes to appropriate nodes
* swap-nodes-in-pairs (medium): typical linked list medium problem which I really just hate doing

##### Backtracking
* subsets (medium): dfs, recursion, 2^n
* subsets-ii (medium): backtracking using dfs, n*2^n
* combination-sum (medium): backtracking + needing to simplfy exploration space
* permutations (medium): backtracking, permutation, N!/(N-k)!
* combination-sum-ii (medium): backtracking combinations, O(2^N)
* word-search (medium)
* rotting-oranges (medium)
* combinations (medium): remember to be careful with how you are passing params in recursive calls and/or reusing variable names (i.e., .copy(), .append(), .pop()) as needed. Remember that for a tree there are typically (number choices)^(height) nodes, so for binary tree there are 2^(height) nodes

##### Graphs:
* number-of-islands (medium): dfs, O(MxN)
* clone-graph (medium): deep copy, DFS graph
* max-area-of-island (medium): dfs, O(RxC), next version of number-of-islands
* pacific-atlantic-water-flow (medium): dfs or bfs, O(RxC), early stopping
* surrounded-regions (medium): dfs, islands, change board in memory, O(RxC), solved in < 30 min!
* walls-and-gates (medium): trick to explore from gates instead of rooms, then use straightforward BFS
* number-of-islands (medium): efficient trick to reduce complexity but then DFS over a grid of islands
* reorder-routes-to-make-all-paths-lead-to-the-city (medium): figure out all neighbors (whether correct direction or not) if an edge leads away from a path-to-0 then increment counter because we need more changes
* course-scheduled-ii (medium): topological sort, sort through courses, detect cycles via a set that we remove and add from, visit which we mark as having been explored, and output array

##### Dynamic Programming:
* climbing-stairs (easy): good fundamental problem
* min-cost-climbing-stairs (easy)
* house-robber (medium)
* word-break (medium): can also be dfs + memoization
* coin-change (medium): great problem, do again before interviews!
* decode-ways (medium): recursive way is obvious, iterative way less so. as usual find a base case to a subproblem and then iterate to find additional solutions. here as we iterate in the string we know at minimum the solution is dp[i-1] but also that if this character and the one prior can form a solution of itself then you also add dp[i-2]

##### Greedy:
* maximum-subarray (medium): sliding window mixed with dynamic programming
* jump-game (medium): dfs backtracking option, takes tweak to get in time limit
* gas-station (medium): there is an easy O(~n^2) solution via brute force, but to meet this time complexity you need to identify some simplifications of the problem. problem states if a solution exists it is unique. you create a diff array which is gas[i] - cost[i] for all i. then you iterate through with different starting points and need to establish the understanding that if you iterate through diff array then the result is the first index for which you can continue through the rest of the array without cumulative gas dipping below 0

##### Intervals:
* meeting-rooms (easy): sort, basic math
* meeting-rooms-ii (medium): good practice! [DO THIS AGAIN]
* insert-interval (medium): here the brute-force approach is actually the best, and you need to come to this realization by comparing time complexity for binary-search + linear search, vs. just doing linear. you'll see it is easier to just iterate linearly. from here you need to deduce some basic logic to figure out if we insert the interval at a position, combine it with the existing, etc.

##### Math & Geometry:
* plus-one (easy): basic for loop and check condition
* happy-number (easy): basic for loop, detect cycle
* statistics-from-a-large-sample (medium): good practice combining code and math knowledge
* spiral-matrix (medium): go slow in the example/approach section to figure out logic, then code up and 90% of the way there. there is a testcase that fails, so step through and see slight gap in solution and update. boom.
* random weight number (medium): integer of weights representing prob of selecting that ind. recall that we can create a cumulative sum of this array and then index into it by doing random*total sum where random [0, 1] and then find the first position in the cumulative array where target < val

##### Bit Manipulation
* single-numer (easy): xor tricky
* number-of-1-bits (easy): bit shift number and use mod to see if ends in 0 or 1
* counting-bits (easy): same as number-of-1-bits, use modulus and bitshift right
* reverse-bits (easy): need to combine bitshift left, bitshift right, logic and (&) logic or (|). to reverse start with 32bit number of all zeros. figure out what the ith position is in the number by bit-shifting by i and & with 1. then add to result by bit-shifting the bit by 31-i and or with current solution

##### Matrix
* toeplitz-matrix (easy): easy once you realize you only need to two inner loops and you only need to compare [r][c] to [r+1][c+1] go slow on these
* diagonal-traverse (medium): same idea with these matrix problems, go slow, it almost always boils down to 2 inner loops

##### Object Oriented Programming
* design-a-text-editor (hard): example past dropbox oa

\* needed significant hints

#### Resources
* [Cracking the Coding Skills](https://drive.google.com/file/d/0BxTvoZCNzGBoRGIyUU5jSDY4RzA/view?resourcekey=0-q2yVDnZo-m2pjgxmXMKgAA)
* [Meta Technical Screen Interview Prep Guide](https://drive.google.com/file/d/18Gn89EHYjFIhFk9vGgnb9m5EIEjZa40I/view)
* [Tweep-Sourced MLE Prep](https://docs.google.com/document/d/1IlI5vOsJbYhvxSdIb5fpwebtyo9vmmgZZBwZEqWpSZo/edit)
* [System Design Interview by Alex Xu](https://bytebytego.com/courses/system-design-interview/scale-from-zero-to-millions-of-users)
* [Towards Data Science: How to get an MLE job](https://towardsdatascience.com/how-to-get-a-machine-learning-job-in-6-months-5aaa61b13af2)

#### Questions
* recall python foundational data structures as well as how python uses linked lists to implement other data structures
* remember the time/space complexity for heapq heap build, insert, remove
* practice other sort/search algos
* backtracking: need to clear up space/time complexity for some approachs. also remember permutation and combination equations
