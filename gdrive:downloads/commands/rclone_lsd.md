---
date: 2022-09-23T22:05:46+05:00
title: "rclone lsd"
slug: rclone_lsd
url: /commands/rclone_lsd/
---
## rclone lsd

List all directories/containers/buckets in the path.

### Synopsis


Lists the directories in the source path to standard output. Does not
recurse by default.  Use the -R flag to recurse.

This command lists the total size of the directory (if known, -1 if
not), the modification time (if known, the current time if not), the
number of objects in the directory (if known, -1 if not) and the name
of the directory, Eg

    $ rclone lsd swift:
          494000 2018-04-26 08:43:20     10000 10000files
              65 2018-04-26 08:43:20         1 1File

Or

    $ rclone lsd drive:test
              -1 2016-10-17 17:41:53        -1 1000files
              -1 2017-01-03 14:40:54        -1 2500files
              -1 2017-07-08 14:39:28        -1 4000files

If you just want the directory names use "rclone lsf --dirs-only".


Any of the filtering options can be applied to this command.

There are several related list commands

  * `ls` to list size and path of objects only
  * `lsl` to list modification time, size and path of objects only
  * `lsd` to list directories only
  * `lsf` to list objects and directories in easy to parse format
  * `lsjson` to list objects and directories in JSON format

`ls`,`lsl`,`lsd` are designed to be human readable.
`lsf` is designed to be human and machine readable.
`lsjson` is designed to be machine readable.

Note that `ls` and `lsl` recurse by default - use "--max-depth 1" to stop the recursion.

The other list commands `lsd`,`lsf`,`lsjson` do not recurse by default - use "-R" to make them recurse.

Listing a non existent directory will produce an error except for
remotes which can't have empty directories (eg s3, swift, gcs, etc -
the bucket based remotes).


```
rclone lsd remote:path [flags]
```

### Options

```
  -h, --help        help for lsd
  -R, --recursive   Recurse into the listing.
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.

