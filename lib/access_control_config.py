## $Id$
## CDSware Access Control Config in mod_python.

## This file is part of the CERN Document Server Software (CDSware).
## Copyright (C) 2002 CERN.
##
## The CDSware is free software; you can redistribute it and/or
## modify it under the terms of the GNU General Public License as
## published by the Free Software Foundation; either version 2 of the
## License, or (at your option) any later version.
##
## The CDSware is distributed in the hope that it will be useful, but
## WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
## General Public License for more details.
##
## You should have received a copy of the GNU General Public License
## along with CDSware; if not, write to the Free Software Foundation, Inc.,
## 59 Temple Place, Suite 330, Boston, MA 02111-1307, USA.

"""CDSware Access Control Config. """

<protect> ## okay, rest of the Python code goes below #######

__version__ = "$Id$"

# VALUES TO BE EXPORTED
# CURRENTLY USED BY THE FILES access_control_engine.py access_control_admin.py webaccessadmin_lib.py

# name of the role giving superadmin rights
SUPERADMINROLE      = 'superadmin'
# name of the action allowing roles to access the web administrator interface
WEBACCESSACTION     = 'accesswebadmin'
# name of the action allowing roles to delegate the rights to other roles
# ex: libraryadmin to delegate libraryworker
DELEGATEADDUSERROLE = 'delegate_adduserrole'

</protect>
