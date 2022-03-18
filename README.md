# data_archiver

## Usage

# Archive

Archive a lustre directory to an s3 bucket:

`python3 archive.py -b <bucket_name> -i <lustre_paths_file>`

Optional args:

`--print` `-p` (print commands to be executed)

`--dryrun` `-d` (execute rclone commands as dry run)

`--archive` `-a` (execute rclone archive commands)

`--no-du` `-nd` (don't run disk usage check)

See `lustre_paths.txt` for example data.

# Delete

Delete a folder from an s3 bucket:

`python3 delete.py -i <remote_paths_file>`

Optional args:

`--print` `-p` (print commands to be executed)

`--dryrun` `-dr` (execute rclone commands as dry run)

`--delete` `-d` (execute rclone archive commands)

See `remote_paths.txt` for example data.

Always run `module load ISG/rclone` when using this tool (or `rclone` in general)
