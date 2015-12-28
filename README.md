pandoc-ymltbl
-------------

a Source block with language identifier `ymltbl`.

~~~~
```ymltbl
-
  - A
  - B
  - A and B
-
  - False
  - False
  - False
-
  - True
  - False
  - False
-
  - False
  - True
  - False
-
  - True
  - True
  - True
~~~~

...will converted to table notation.
(first row as headers.)

| A     | B     | A and B |
|-------|-------|---------|
| False | False | False   |
| True  | False | False   |
| False | True  | False   |
| True  | True  | True    |

Invoke filter command like

```
pandoc source.md --filter ./ymltbl.py -t markdown_github -o result.md
```
