---
date: 2022-09-23T22:05:46+05:00
title: "rclone moveto"
slug: rclone_moveto
url: /commands/rclone_moveto/
---
## rclone moveto

Move file or directory from source to dest.

### Synopsis


If source:path is a file or directory then it moves it to a file or
directory named dest:path.

This can be used to rename files or upload single files to other than
their existing name.  If the source is a directory then it acts exactly
like the move command.

So

    rclone moveto src dst

where src and dst are rclone paths, either remote:path or
/path/to/local or C:\windows\path\if\on\windows.

This will:

    if src is file
        move it to dst, overwriting an existing file if it exists
    if src is directory
        move it to dst, overwriting existing files if they exist
        see move command for full details

This doesn't transfer unchanged files, testing by size and
modification time or MD5SUM.  src will be deleted on successful
transfer.

**Important**: Since this can cause data loss, test first with the
--dry-run flag.

**Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics.


```
rclone moveto source:path dest:path [flags]
```

### Options

```
  -h, --help   help for moveto
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.

