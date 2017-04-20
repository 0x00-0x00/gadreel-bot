from shemutils.logger import Logger
from telemanager.database import *
from time import time
import re
master_id = 193665372  # the master ID -- configure it by hand to ensure security

logger = Logger("tele-manager")

class MemberRegexHandler(object):
    def __init__(self, message):
        self.message = message
        self._parse_regex()

    def _parse_regex(self):
        req = self._request_regex()
        acc = self._accept_regex()

        #  Returns if no match.
        if not acc and not req:
            return 0

        if req:
            obj = RequestMember(req["id"])
            if obj.status is True:
                logger.debug("User #{0} request successfully added.".format(req["id"]))
                return 0
            else:
                return -1

        if acc:
            obj = AcceptMember(req["id"])
            if obj.status is True:
                logger.debug("User #{0} acceptance successfully done.".format(req["id"]))
                return 0
            else:
                return -1

    def _request_regex(self):
        """
        Tries to identify the message using one regular expression.
        """
        regex = "^(register?|registrar)\s+(?P<id>[\d]+)"
        m = re.match(regex, self.message.decode())
        if not m:
            return None
        return m.groupdict()

    def _accept_regex(self):
        """
        Tries to identify the message using one regular expression.
        """
        regex = "^(acc?|accept?|aceitar)\s+(?P<id>[\d]+)"
        m = re.match(regex, self.message.decode())
        if not m:
            return None
        return m.groupdict()

class RequestMember(object):
    """
    Object to realize member requesting.
    """
    def __init__(self, id):
        self.id = int(id)
        self.status = False
        if self._register_new_member() == 0:
            self.status = False

    def _register_new_member(self):
        """
        Creates a row into database with 'PENDING' status
        """
        try:
            db.controller.execute(t4.insert_data([self.id, "PENDING", str(time())]))
            db.save()
        except Exception as e:

        return 0


class AcceptMember(object):
    """
    Object to realize member acceptance.
    """
    def __init__(self, id):
        self.id = id
        self._accept_member()

    def _accept_member(self):
        """
        Accept a member from the MEMBERS table which status is 'PENDING'
        """
        search_SQL = t4.search("USER_ID", self.id)
        db.controller.execute(search_SQL)
        results = db.controller.get()
        if len(results) == 0:
            return -1
        else:
            for result in results:
                user_id, status, timestamp = result[1], result[2], result[3]
                if status == "PENDING":
                    update_SQL = t4.update()
        return 0


class AuthenticationCheck(object):
    """
    Simple authentication checkage to use the bot.
    This is intented to block unknown people posting/uploading data into
    bot folder, ensuring only rightfull data will be disposable.
    """
    def __init__(self, id):
        self.requested_id = int(id)  # User ID

    def _get_members(self):
        """
        Execute the query and return the list of results.
        """
        db.controller.execute(t4.search("USER_ID", self.requested_id))
        return db.controller.get()

    def check(self):
        """
        Perform master id and member table checkage
        """
        results = self._get_members()

        # Unregistered bot member
        if self.requested_id != master_id and len(results) == 0:
            return -1

        # Exclusive return code for bot master
        if self.requested_id is master_id:
            return 1

        #  Ok.
        return 0
