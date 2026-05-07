# orbit

A binary-based esoteric programming language where every program is a fractal
of 3×3 tables. Execution walks a clockwise spiral; operators can drop into
sub-tables that recurse to arbitrary depth.

By Zander & Carson.

```
   ┌─────┬─────┬─────┐
   │  1  │  2  │  3  │      execution order:
   ├─────┼─────┼─────┤      top-left → clockwise → center
   │  8  │  9  │  4  │      (cell 9 runs last)
   ├─────┼─────┼─────┤
   │  7  │  6  │  5  │
   └─────┴─────┴─────┘
```

## Core model

Each table maintains three pieces of state:

| Var | Meaning | Initial value |
|---|---|---|
| `x` | the previous value | `null` |
| `t` | type `x` is interpreted as | `binary` |
| `q` | saved-data queue | empty |

`t` can be `string`, `int`, or `binary` — set with the `W`, `N`, `B` operators.
`t` is bound to the instance of `x`: as long as `x` lives, so does `t`.

When the walker hits a **drop operator**, it descends into a 3×3 sub-table,
runs that sub-table, and the resulting `x` from the sub-table feeds the parent
operator. Sub-tables can hold drop operators of their own — that's where the
fractal property comes from.

A program must start with a **letter drop operator** at the outermost top-left.

## Operators

### Drop operators (lowercase / symbol — they recurse into a sub-table)

| Op | Effect |
|---|---|
| `x` | set `x` to sub-table value |
| `c` | continue: set sub's `x` to current `x`, then run sub, then take its value |
| `p` | print sub-table value |
| `s` | save `x` to address held in sub-table value |
| `g` | get `x` from address held in sub-table value |
| `=` | if sub-table value == `x`, run next op; else skip it |
| `+ - * /` | arithmetic: combine `x` with sub-table value |
| `\| & ^` | bitwise or / and / xor with sub-table value |

### In-place operators (uppercase / digit — operate on `x` directly)

| Op | Effect |
|---|---|
| `L` | loop back to start of this table without changing `x` |
| `S` | skip next operation |
| `K` | keep: use current `x` as starting value for the next drop op |
| `C` | clear: set `x` to null |
| `R` | return: skip the rest of this table |
| `P` | print `x` |
| `I` | input: read user input into `x` |
| `0` `1` | append a binary 0 / 1 to the end of `x`'s binary representation |
| `W` `N` `B` | set type `t` to string / int / binary |
| `\` | null (no-op) |

Standard logical operators (`<`, `>`, `==`, etc.) work identically to `=` and
are accepted as aliases.

## Example: print user input

```
   p
   |
   v

  I,\,\
  \,\,\
  \,\,\
```

The outer cell `p` (print drop) drops into the sub-table. `I` reads input into
`x`. The eight `\` cells are no-ops. When the sub-table completes, `p` prints
`x`.

## Run

```bash
cd interpreter
python main.py input.orbit         # run a program
python ide.py                      # launch the table-aware IDE
```

## Repository layout

```
interpreter/
  main.py              # entry point
  orbit.py             # core execution engine
  orbit_parser.py      # table parser
  orbit_operator.py    # operator definitions
  operator_function.py # operator implementations
  input_handler.py     # I/O
  ide.py               # tkinter IDE
  input.orbit          # sample program (input demo)
```

## Status

- [x] Language design
- [x] Documentation
- [x] Interpreter
- [x] IDE (tkinter, table-aware)
- [x] Beta build
- [ ] OS installer so `.orbit` files open in the IDE on double-click

## License

See [`license.txt`](license.txt).
