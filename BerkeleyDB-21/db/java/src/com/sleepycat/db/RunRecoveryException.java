/*-
 * See the file LICENSE for redistribution information.
 *
 * Copyright (c) 1997,2008 Oracle.  All rights reserved.
 *
 * $Id: RunRecoveryException.java,v 12.8 2008/01/17 05:04:53 mjc Exp $
 */
package com.sleepycat.db;

import com.sleepycat.db.internal.DbEnv;

/**
Thrown when the database environment needs to be recovered.
 *
Errors can occur in where the only solution is to shut down the
application and run recovery.  When a fatal error occurs, this
exception will be thrown, and all subsequent calls will also fail in
the same way.  When this occurs, recovery should be performed.
*/
public class RunRecoveryException extends DatabaseException {
    /* package */ RunRecoveryException(final String s,
                                   final int errno,
                                   final DbEnv dbenv) {
        super(s, errno, dbenv);
    }
}
