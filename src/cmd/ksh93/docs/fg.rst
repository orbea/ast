.. default-role:: code

:index:`fg` -- move jobs to the foreground
==========================================

Synopsis
--------
| fg [job ...]

Description
-----------
`fg` places the given *job*\ s into the foreground and sends them a `CONT` signal to start them running. If *job* is omitted, the most recently started or stopped background job is moved to the foreground.

Each *job* can be specified in one of the following ways:

   :*int*: refers to a process id (pid).
   :`-`\ *int*: refers to a process group id.
   :`%`\ *int*: refers to a job number.
   :`%`\ *str*: refers to a job whose name begins with *str*.
   :`%?`\ *str*: refers to a job whose name contains *str*.
   :`%+` or `%%`: refers to the current job.
   :`%-`: refers to the previous job.

Exit Status
-----------
If `fg` brings one or more jobs into the foreground, the exit status of `fg` will be that of the last job. If one or more jobs does not exist or has completed, `fg` will return a non-zero exit status.

See Also
--------
`wait`\(1), `bg`\(1), `disown`\(1), `jobs`\(1)
