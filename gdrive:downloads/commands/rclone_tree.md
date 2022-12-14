---
date: 2022-09-23T22:05:46+05:00
title: "rclone tree"
slug: rclone_tree
url: /commands/rclone_tree/
---
## rclone tree

List the contents of the remote in a tree like fashion.

### Synopsis


rclone tree lists the contents of a remote in a similar way to the
unix tree command.

For example

    $ rclone tree remote:path
    /
    ├── file1
    ├── file2
    ├── file3
    └── subdir
        ├── file4
        └── file5
    
    1 directories, 5 files

You can use any of the filtering options with the tree command (eg
--include and --exclude).  You can also use --fast-list.

The tree command has many options for controlling the listing which
are compatible with the tree command.  Note that not all of them have
short options as they conflict with rclone's short options.


```
rclone tree remote:path [flags]
```

### Options

```
  -a, --all             All files are listed (list . files too).
  -C, --color           Turn colorization on always.
  -d, --dirs-only       List directories only.
      --dirsfirst       List directories before files (-U disables).
      --full-path       Print the full path prefix for each file.
  -h, --help            help for tree
      --human           Print the size in a more human readable way.
      --level int       Descend only level directories deep.
  -D, --modtime         Print the date of last modification.
  -i, --noindent        Don't print indentation lines.
      --noreport        Turn off file/directory count at end of tree listing.
  -o, --output string   Output to file instead of stdout.
  -p, --protections     Print the protections for each file.
  -Q, --quote           Quote filenames with double quotes.
  -s, --size            Print the size in bytes of each file.
      --sort string     Select sort: name,version,size,mtime,ctime.
      --sort-ctime      Sort files by last status change time.
  -t, --sort-modtime    Sort files by last modification time.
  -r, --sort-reverse    Reverse the order of the sort.
  -U, --unsorted        Leave files unsorted.
      --version         Sort files alphanumerically by version.
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.

