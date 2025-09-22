# Pagination Project

This project implements pagination mechanisms for large datasets using Python. It covers simple pagination, hypermedia-style pagination (HATEOAS), and deletion-resilient pagination, using a dataset of popular baby names.

## Learning Objectives

- Paginate a dataset using `page` and `page_size` parameters  
- Add hypermedia pagination metadata (HATEOAS-style)  
- Handle deletion-resilient pagination for dynamic datasets  

## Requirements

- Python 3.9 on Ubuntu 20.04 LTS  
- All files must:  
  - Start with `#!/usr/bin/env python3`  
  - End with a new line  
  - Follow `pycodestyle` (version 2.5.*)  
  - Include proper docstrings and type annotations  

## Project Structure

```
atlas-web_back_end/
└── pagination/
    ├── 0-simple_helper_function.py
    ├── 1-simple_pagination.py
    ├── 2-hypermedia_pagination.py
    ├── 3-hypermedia_del_pagination.py
    ├── Popular_Baby_Names.csv
    └── README.md
```

## Tasks

### Task 0: Simple Helper Function

**File**: `0-simple_helper_function.py`  
Implement `index_range(page: int, page_size: int) -> Tuple[int, int]`  
- Returns a tuple with start and end indexes for pagination  
- Page is 1-indexed  

**Example:**
```python
index_range(1, 7)  # (0, 7)
index_range(3, 15) # (30, 45)
```

---

### Task 1: Simple Pagination

**File**: `1-simple_pagination.py`  
Create a `Server` class with:  
- `dataset()` – loads and caches the CSV data  
- `get_page(page: int = 1, page_size: int = 10) -> List[List]`  

**Details:**  
- Use `assert` to validate `page` and `page_size`  
- Use `index_range` to determine slice range  
- Return correct slice from the dataset  
- Return an empty list if page is out of range  

---

### Task 2: Hypermedia Pagination

**File**: `2-hypermedia_pagination.py`  
Add method: `get_hyper(page: int = 1, page_size: int = 10) -> Dict`  
Returns a dictionary with pagination metadata:

```json
{
  "page_size": 10,
  "page": 1,
  "data": [...],
  "next_page": 2,
  "prev_page": null,
  "total_pages": 971
}
```

**Tips:**  
- Reuse `get_page()`  
- Use `math.ceil(len(dataset) / page_size)` for `total_pages`  
- Set `next_page` and `prev_page` to `None` if out of bounds  

---

### Task 3: Deletion-Resilient Pagination

**File**: `3-hypermedia_del_pagination.py`  
Add method: `get_hyper_index(index: int = None, page_size: int = 10) -> Dict`  

**Details:**  
- Uses an indexed dataset (dictionary) to handle deletions  
- Skips missing rows while preserving expected page size  
- Returns:

```json
{
  "index": 3,
  "next_index": 5,
  "page_size": 2,
  "data": [...]
}
```

**Requirements:**  
- Validate that `index` is within bounds using `assert`  
- If data is missing (e.g., row deleted), skip and continue collecting until `page_size` is met  
- `next_index` is the position of the next item to request  

---

## Dataset: Popular_Baby_Names.csv

CSV file with ~19,000 rows and the following columns:  
- Year of Birth  
- Gender  
- Ethnicity  
- Child's First Name  
- Count  
- Rank  

---

## Example Usage

```python
server = Server()
server.get_page(2, 10)
server.get_hyper(1, 5)
server.get_hyper_index(3, 2)
```

---

## Author

**Ari Murphy**  
Atlas School – Backend Development Track  
GitHub: [https://github.com/ari-rainbow](https://github.com/ari-rainbow)