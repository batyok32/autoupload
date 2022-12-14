---
date: 2022-09-23T22:05:46+05:00
title: "rclone move"
slug: rclone_move
url: /commands/rclone_move/
---
## rclone move

Move files from source to dest.

### Synopsis


Moves the contents of the source directory to the destination
directory. Rclone will error if the source and destination overlap and
the remote does not support a server side directory move operation.

If no filters are in use and if possible this will server side move
`source:path` into `dest:path`. After this `source:path` will no
longer longer exist.

Otherwise for each file in `source:path` selected by the filters (if
any) this will move it into `dest:path`.  If possible a server side
move will be used, otherwise it will copy it (server side if possible)
into `dest:path` then delete the original (if no errors on copy) in
`source:path`.

If you want to delete empty source directories after move, use the --delete-empty-src-dirs flag.

See the [--no-traverse](/docs/#no-traverse) option for controlling
whether rclone lists the destination directory or not.  Supplying this
option when moving a small number of files into a large destination
can speed transfers up greatly.

**Important**: Since this can cause data loss, test first with the
--dry-run flag.

**Note**: Use the `-P`/`--progress` flag to view real-time transfer statistics.


```
rclone move source:path dest:path [flags]
```

### Options

```
      --create-empty-src-dirs   Create empty source dirs on destination after move
      --delete-empty-src-dirs   Delete empty source dirs after move
  -h, --help                    help for move
```

See the [global flags page](/flags/) for global options not listed here.

### SEE ALSO

* [rclone](/commands/rclone/)	 - Show help for rclone commands, flags and backends.

