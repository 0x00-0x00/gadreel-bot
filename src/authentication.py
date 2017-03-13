from telemanager.database import *
master_id = 193665372

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
        if self.requested_id is not master_id and len(results) == 0:
            return -1

        # Exclusive return code for bot master
        if self.requested_id is master_id:
            return 1

        #  Ok.
        return 0
