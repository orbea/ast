/***********************************************************************
 *                                                                      *
 *               This software is part of the ast package               *
 *          Copyright (c) 1982-2012 AT&T Intellectual Property          *
 *                      and is licensed under the                       *
 *                 Eclipse Public License, Version 1.0                  *
 *                    by AT&T Intellectual Property                     *
 *                                                                      *
 *                A copy of the License is available at                 *
 *          http://www.eclipse.org/org/documents/epl-v10.html           *
 *         (with md5 checksum b35adb5213ca9657e911e9befb180842)         *
 *                                                                      *
 *              Information and Software Systems Research               *
 *                            AT&T Research                             *
 *                           Florham Park NJ                            *
 *                                                                      *
 *                    David Korn <dgkorn@gmail.com>                     *
 *                                                                      *
 ***********************************************************************/
#include "config_ast.h"  // IWYU pragma: keep

#include <getopt.h>
#include <stdlib.h>

#include "builtins.h"
#include "defs.h"
#include "error.h"
#include "jobs.h"
#include "sfio.h"
#include "shcmd.h"

#ifdef JOBS

static const char *short_options = "+:";
static const struct option long_options[] = {
    {"help", no_argument, NULL, 1},  // all builtins supports --help
    {NULL, 0, NULL, 0}};

//
// Builtin `fg` command.
//
int b_fg(int argc, char *argv[], Shbltin_t *context) {
    UNUSED(argc);
    int opt;
    Shell_t *shp = context->shp;
    char *cmd = argv[0];

    optind = opterr = 0;
    while ((opt = getopt_long(argc, argv, short_options, long_options, NULL)) != -1) {
        switch (opt) {
            case 1: {
                builtin_print_help(shp, cmd);
                return 0;
            }
            case ':': {
                builtin_missing_argument(shp, cmd, argv[optind - 1]);
                return 2;
            }
            case '?': {
                builtin_unknown_option(shp, cmd, argv[optind - 1]);
                return 2;
            }
            default: { abort(); }
        }
    }

    argv += optind;
    if (!sh_isoption(shp, SH_MONITOR) || !job.jobcontrol) {
        if (sh_isstate(shp, SH_INTERACTIVE)) {
            errormsg(SH_DICT, ERROR_exit(1), e_no_jctl);
            __builtin_unreachable();
        }
        return 1;
    }
    if (job_walk(shp, sfstdout, job_switch, 'f', argv)) {
        errormsg(SH_DICT, ERROR_exit(1), e_no_job);
        __builtin_unreachable();
    }
    return shp->exitval;
}

#endif  // JOBS
