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

##### Two Pointers
* valid-palindrome (easy): string manipulation, reverse array
* two-sum-ii-input-array-is-sorted (medium): two pointers, use sorted property
* 3sum (medium): next step of two-step ii, hash, left & right pointer
* container-with-most-water (medium)

##### Sliding Window
* best-time-to-buy-and-sell-stock (easy): iterate, compare mins and maxs
* longest-substring-without-repeating-characters (medium): great problem, usage of hash to reduce duplicated computing
* longest-repeating-character-replacement (medium): window, efficiency
* permutation-in-string (medium): window, hashmap

##### Stack
* *generate-parentheses (medium): backtracking, recursion, dfs
* car-fleet (medium): stack, monotonic stack, math
* daily-temperature (medium): monotonic decreasing stack, [GOOD]
* valid-parantheses (easy): stack
* min-stack (medium)

##### Trees
* invert-binary-tree (easy): classic, bfs, revisit this for warmup!
* maximum-depth-of-binary-tree (easy): dfs
* lowest-common-ancestor-of-a-binary-search-tree (medium): binary search tree property
* binary-tree-level-order-traversal (medium): bfs
* count-good-nodes-in-binary-tree (medium): dfs keeping track of other variables
* binary-tree-right-side-view (medium): bfs or dfs with trick
* kth-smallest-element-in-a-bst (medium): binary search tree, in-order traversal
* same-tree (blind75, easy)

##### Tries
* implement-trie-prefix-tree (medium): basic prefix trie, oop
* design-add-and-search-words-data-structure (medium): prefix trie, dfs

##### Heap
* kth-largest-element-in-a-stream (easy): basic overview of how heap works
* last-stone-weight (easy): max heap
* k-closest-points-to-origin (medium): min heap
* kth-largest-element-in-an-array (medium): min heap (k-th largest)

##### Binary Search
* binary-search (easy): basic binary search implementation
* search-a-2d-matrix (medium): binary search, 2d
* koko-eating-bananas (medium): binary search, math tricks
* search-in-rotated-sorted-array (medium): binary search with rotation
* find-minimum-in-rotated-sorted-array (medium): binary search but need to check on rotation

##### Linked List
* reverse-linked-list (easy): example how to use linkedlist class and reverse
* merge-two-sorted-list (easy): oof I really do not like linkedlist questions, they're simply but I always seem to mess something up
  * [Why is dummy node changing](https://stackoverflow.com/questions/72588124/why-is-dummy-node-changing-in-this-linked-list-problem-python3) seems to be the best explanation for what's happening under the hood. Super helpful
* reorder (medium): this _seems_ like an easy problem in terms of getting an approach, but actually completing it is a tad confusing for me. I think I'm having troubles understandanding how
manipulation in place is occuring
* remove-nth-node-from-end-of-list (medium): this was more straightforward and pretty much got it, though use of the dummy node is still a bit fuzzy for me
* linked-list-cycle (easy): keep track of visited nodes, if so return Tru
* add-two-numbers (medium): basic traversal of two lists, but need to do some math tricks. nailed this one.

##### Backtracking
* subsets (medium): dfs, recursion, 2^n
* subsets-ii (medium): backtracking using dfs, n*2^n
* combination-sum (medium): backtracking + needing to simplfy exploration space
* permutations (medium): backtracking, permutation, N!/(N-k)!
* combination-sum-ii (medium): backtracking combinations, O(2^N)
* word-search (medium)
* rotting-oranges (medium)

##### Graphs:
* number-of-islands (medium): dfs, O(MxN)
* clone-graph (medium): deep copy, DFS graph
* max-area-of-island (medium): dfs, O(RxC), next version of number-of-islands
* pacific-atlantic-water-flow (medium): dfs or bfs, O(RxC), early stopping
* surrounded-regions (medium): dfs, islands, change board in memory, O(RxC), solved in < 30 min!
* walls-and-gates (medium): trick to explore from gates instead of rooms, then use straightforward BFS

##### Dynamic Programming:
* climbing-stairs (easy): good fundamental problem
* min-cost-climbing-stairs (easy)
* house-robber (medium)
* word-break (medium): can also be dfs + memoization
* coin-change (medium): great problem, do again before interviews!

##### Greedy:
* maximum-subarray (medium): sliding window mixed with dynamic programming
* jump-game (medium): dfs backtracking option, takes tweak to get in time limit

##### Intervals:
* meeting-rooms (easy): sort, basic math
* meeting-rooms-ii (medium): good practice! [DO THIS AGAIN]

##### Math & Geometry:
* plus-one (easy): basic for loop and check condition
* happy-number (easy): basic for loop, detect cycle
* statistics-from-a-large-sample (medium): good practice combining code and math knowledge

##### Bit Manipulation
* single-numer (easy): xor tricky
* number-of-1-bits (easy): bit shift number and use mod to see if ends in 0 or 1
* counting-bits (easy): same as number-of-1-bits, use modulus and bitshift right

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
