# Datrax

A **blazing-fast Python library** for **array** and **string** operations, built from scratch without external dependencies.  
Perfect for learning, portfolio demonstration, or lightweight use cases where you want **full control** over performance.

---

## ✨ Features

### **Array Operations** (`Datrax.arrsenal`)
- `sumup(arr)` → Sum of elements
- `maxout(arr)` → Maximum element
- `minout(arr)` → Minimum element
- `fliparr(arr)` → Reverse array in-place
- `uniqarr(arr)` → Remove duplicates
- `ascend(arr)` / `descend(arr)` → Sort ascending / descending
- `locate(arr, element)` → Find index of element
- `freq(arr, element)` → Count occurrences
- `mergearr(arr1, arr2)` → Merge two arrays
- `cutarr(arr, start, end, step)` → Slice array
- `rotarr(arr, k)` → Rotate array
- `inject(arr, pos, value)` → Insert value at position
- `zapval(arr, value)` → Remove by value
- `zapindex(arr, index)` → Remove by index

### **String Operations** (`Datrax.textsmith`)
- `flipstr(s)` → Reverse string
- `loudify(s)` / `softify(s)` → Uppercase / lowercase
- `vowcount(s)` / `conscount(s)` → Count vowels / consonants
- `ispali(s)` → Check palindrome
- `wordcount(s)` → Count words
- `charfreq(s)` → Character frequency
- `trimspace(s)` → Trim leading/trailing spaces
- `swapstr(s)` → Swap letter case
- `findstr(s, sub)` → Find substring index
- `splitstr(s)` / `joinstr(list, sep)` → Split & join strings
- `capfirst(s)` → Capitalize first letter
- `titlefy(s)` → Capitalize each word's first letter

---

## 🚀 Installation

Once published to PyPI:

```bash
pip install Datrax
